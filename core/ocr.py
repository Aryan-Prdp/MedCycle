import pytesseract
from PIL import Image
import re


# ------------------------------
# Extract Expiry Date from Image
# ------------------------------
def extract_expiry_date(image_path):
    """
    Reads the text from the uploaded medicine image
    and tries to detect expiry date.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)

        # Full date format DD/MM/YYYY or DD-MM-YYYY
        pattern_full = r'(\d{2}[\/\-]\d{2}[\/\-]\d{4})'
        match_full = re.search(pattern_full, text)

        if match_full:
            return match_full.group(1)

        # Month-year MM/YYYY or MM-YYYY
        pattern_month_year = r'(\d{2}[\/\-]\d{4})'
        match_my = re.search(pattern_month_year, text)

        if match_my:
            return "01/" + match_my.group(1)

        return None

    except Exception as e:
        return None
