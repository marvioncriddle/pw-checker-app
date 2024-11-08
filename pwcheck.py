# pwcheck.py

import re
from zxcvbn import zxcvbn

# Function to check password using regex rules
def regex_check(password):
    if len(password) < 24:
        return "Password must be at least 24 characters long."
    if not re.search("[A-Z]", password):
        return "Password must have at least one uppercase letter (A-Z)."
    if not re.search("[a-z]", password):
        return "Password must have at least one lowercase letter (a-z)."
    if not re.search("[0-9]", password):
        return "Password must have at least one number (0-9)."
    if not re.search("[!@#$%^&*]", password):
        return "Password must have at least one special character (!@#$%^&*)."
    return "Password meets basic requirements."

# Function to use zxcvbn for more advanced strength checking
def zxcvbn_check(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    return {
        'strength_score': score,
        'feedback': feedback
    }
