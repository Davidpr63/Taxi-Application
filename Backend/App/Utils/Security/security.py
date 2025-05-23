import bcrypt
from Backend.App.Utils.Security.i_security import ISecurity


class Security(ISecurity):

    def __init__(self):
        pass

    def hash_password(self, plain_password: str)  -> str:
        try:
            password_bytes = plain_password.encode('utf-8')
            hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            return hashed.decode('utf-8')
        except Exception as e:
            print('Hash password error: ', e)


    def verify_password(self, plain_password: str, hashed_password):
        try:
            return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
        except Exception as e:
            print('Verify password error: ', e)
