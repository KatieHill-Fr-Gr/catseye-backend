import json
from typing import Dict, List, Any
from ..services.deepl_service import get_deepl_client, translate_text

def extract_text_nodes(node: Dict[str, Any], texts: List[Dict]) -> None:
    """
    Recursively extract text nodes from Lexical JSON structure.
    Stores reference to the text node so we can update it later.
    """
    if node.get('type') == 'text' and 'text' in node:
        texts.append(node)
    
    if 'children' in node:
        for child in node['children']:
            extract_text_nodes(child, texts)


def translate_lexical_json(lexical_data: dict, target_lang: str) -> dict:
    """
    Translate all text nodes in Lexical JSON structure.
    Returns the modified dictionary with translated text.
    """
    # No need to parse - it's already a dict
    # Make a copy to avoid modifying the original
    import copy
    data = copy.deepcopy(lexical_data)
    
    # Extract all text nodes
    text_nodes = []
    extract_text_nodes(data['root'], text_nodes)
    
    if not text_nodes:
        return data
    
    # Collect all text content
    texts_to_translate = [node['text'] for node in text_nodes if node['text'].strip()]
    
    if not texts_to_translate:
        return data
    
    # Translate all texts in one API call
    client = get_deepl_client()
    results = client.translate_text(texts_to_translate, target_lang=target_lang)
    
    # Handle single vs multiple results
    if not isinstance(results, list):
        results = [results]
    
    # Update the text nodes with translations
    result_idx = 0
    for node in text_nodes:
        if node['text'].strip():
            node['text'] = results[result_idx].text
            result_idx += 1
    
    return data