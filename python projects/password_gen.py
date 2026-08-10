import secrets
import string


def generate_password(length=16):
    if length < 8:
        raise ValueError("length Should be at least 8 for Strong password")

    alphabet = string.ascii_letters + string.digits +string.punctuation

    while True:
      password = ''.join(secrets.choice(alphabet) for _ in range(length))
    #Make sure at least one character of each type 
      if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
        return password
    
print(generate_password(16))
    
