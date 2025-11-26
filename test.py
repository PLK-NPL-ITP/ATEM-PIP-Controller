import re

def validate_email(email):
    return bool(re.match(r'^(?!\.)(?!.*\.\.)(?!.*\.$)[a-zA-Z0-9.+]+@(?!\.)(?!.*\.\.)(?!.*\.$)(?!.*-\.)(?!.*\.-)(?=.*\.)[a-zA-Z0-9.-]{3,}$', email))