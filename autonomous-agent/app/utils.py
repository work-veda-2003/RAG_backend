import json

MAX_ITERATIONS = 5

def safe_json_parse(text):
    try:
        return json.loads(text)
    except:
        return None