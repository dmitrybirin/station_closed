def get_state_from_text(text):
    if 'закрыт' in text and 'открыт' in text:
        return 'unknown'
    if 'закрыт' in text:
        return 'closed'
    if 'открыт' in text:
        return 'open'
    else:
        return None
    
    