import re
from datetime import time

TIME_REGEXP = r"([\d]+)[ч :\-.]+([\d]+)[ мин]*"
    
def get_time_from_text(text):
    time_result = re.search(TIME_REGEXP, text)
    if time_result is not None:
        try:
            results = time_result.groups()
            return time(int(results[0]), int(results[1]))            
        except Exception as e:
            print('Exception', e)
            return None
    else:
        return None

def get_text_without_time(text):
    return re.sub(TIME_REGEXP, '', text)