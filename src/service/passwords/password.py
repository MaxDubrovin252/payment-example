import bcrypt


def hash_password(password:str)->bytes:
    return bcrypt.hashpw(password=password.encode(),salt=bcrypt.gensalt())

def dehash_password(password:str,hash_password:bytes):
    return bcrypt.checkpw(password=password.encode(),hashed_password=hash_password)