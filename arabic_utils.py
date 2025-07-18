import arabic_reshaper
from bidi.algorithm import get_display

def fix_arabic(text):
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    return bidi_text
