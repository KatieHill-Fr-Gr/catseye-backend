import deepl

AUTH_KEY='2cfeb217-6d14-4ba0-9c1e-458c8a7f19c5:fx'
DEEPL_CLIENT = deepl.DeepLClient(AUTH_KEY)

result = DEEPL_CLIENT.translate_text("Hello, world!", target_lang="DE")
print(result.text)
