import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Проверка пароля
def check_password(hashed_password, user_password):
    return hashed_password == hash_password(user_password)
