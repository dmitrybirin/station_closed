def get_reason_from_text(text):
    if 'бесхозный' in text and 'закрыт' in text:
        return 'из-за бесхозного предмета'
    else:
        return None
    
    