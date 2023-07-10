import jwt
from mobidick.settings import JWT_SECRET_KEY
def getUserId(jwtToken) :
    key = JWT_SECRET_KEY
    _jwt =  jwt.decode(jwtToken, key, algorithms="HS256")['userId'];
    return _jwt