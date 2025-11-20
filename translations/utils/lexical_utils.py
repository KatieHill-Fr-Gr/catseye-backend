import json
from typing import Dict, List, Any

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


def translate_lexical_json(lexical_json: str, target_lang: str) -> str:
    """
    Translate all text nodes in Lexical JSON structure.
    Returns the modified JSON string with translated text.
    """
    # Parse the JSON
    data = json.loads(lexical_json)
    
    # Extract all text nodes (these are references, so we can modify them)
    text_nodes = []
    extract_text_nodes(data['root'], text_nodes)
    
    if not text_nodes:
        return lexical_json  # No text to translate
    
    # Collect all text content
    texts_to_translate = [node['text'] for node in text_nodes if node['text'].strip()]
    
    if not texts_to_translate:
        return lexical_json  # Only whitespace
    
    # Translate all texts in one API call (more efficient)
    client = get_deepl_client()
    results = client.translate_text(texts_to_translate, target_lang=target_lang)
    
    # Handle single vs multiple results
    if not isinstance(results, list):
        results = [results]
    
    # Update the text nodes with translations
    result_idx = 0
    for node in text_nodes:
        if node['text'].strip():  # Only translate non-empty text
            node['text'] = results[result_idx].text
            result_idx += 1
    
    # Return the modified JSON
    return json.dumps(data)