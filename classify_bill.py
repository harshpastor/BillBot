import re
from datetime import datetime

def classify(text):
    text_lower = text.lower()

    # OTT subscriptions
    if any(word in text_lower for word in ["netflix", "hotstar", "prime video", "sonyliv", "zee5", "aha", "disney+"]):
        bill_type = "ott"

    # Mobile recharge & telecom
    elif any(word in text_lower for word in ["jio", "airtel", "vodafone", "vi ", "bsnl", "mobile recharge"]):
        bill_type = "mobile_recharge"

    # Food delivery
    elif any(word in text_lower for word in ["swiggy", "zomato", "eatsure", "domino", "pizza hut", "kfc", "mcdonald"]):
        bill_type = "food_delivery"

    # Groceries & daily essentials
    elif any(word in text_lower for word in ["instamart", "blinkit", "dunzo", "zepto", "bigbasket", "grofers"]):
        bill_type = "groceries"

    # Ride-hailing / travel
    elif any(word in text_lower for word in ["ola", "uber", "rapido", "redbus"]):
        bill_type = "ride_hailing"

    # E-commerce purchases
    elif any(word in text_lower for word in ["amazon", "flipkart", "myntra", "ajio", "meesho", "snapdeal"]):
        bill_type = "ecommerce"

    # Utilities (Electricity/Water/Gas)
    elif any(word in text_lower for word in ["electricity", "bses", "water", "gas bill", "indane", "hp gas"]):
        bill_type = "utilities"

    else:
        bill_type = "others"

    # Extract date (any format like DD-MM-YYYY, DD/MM/YYYY, etc.)
    match = re.search(r'(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})', text)
    bill_date = None
    if match:
        for fmt in ("%d-%m-%Y", "%d/%m/%Y", "%d-%m-%y", "%d/%m/%y"):
            try:
                bill_date = datetime.strptime(match.group(1), fmt)
                break
            except ValueError:
                continue

    return bill_type, bill_date
