def cleaner(s: str):
    import re
    return re.sub(r'[^a-zA-Z0-9_]', '', s)