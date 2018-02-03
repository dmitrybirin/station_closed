import re
from datetime import time

TIME_REGEXP = r"([\d]{2})[-.]([\d]{2})"
    
def get_time_from_text(text):
    time_result = re.search(TIME_REGEXP, text)
    if time_result is not None:
        results = time_result.groups()
        return time(int(results[0]), int(results[1]))            
    else:
        return None

def get_text_without_time(text):
    return re.sub(TIME_REGEXP, '', text)