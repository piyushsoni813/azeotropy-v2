import random
import string

def generate_azeoid(name, email):
    unique_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{name[:3].upper()}{unique_str}"
