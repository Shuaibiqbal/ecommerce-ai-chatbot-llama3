def get_context(question: str) -> str:
    q = question.lower()
    if "iphone" in q:
        return "The iPhone 14 features a 6.1-inch display, A15 chip, dual camera, and 5G support."
    elif "return policy" in q:
        return "Our return policy allows returns within 30 days for a full refund."
    elif "order" in q and "12345" in q:
        return "Order #12345 was shipped on June 30 and will arrive by July 5."
    else:
        return ""
