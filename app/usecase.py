import re

def cnj_validator(cnj: str) -> bool:
    pattern = r'^\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}$'

    return bool(re.match(pattern, cnj))
