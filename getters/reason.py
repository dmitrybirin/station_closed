def get_reason_from_text(text):
    if ('бесхозн' in text.lower() or 'безнадзор' in text.lower()) and 'закрыт' in text:
        return 'из-за бесхозного предмета'
    else:
        return None