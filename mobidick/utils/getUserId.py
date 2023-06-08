import jwt


def getUserId(jwtToken, key) :
    _jwt =  jwt.decode(jwtToken, key, algorithms="HS256")['userId'];
    return _jwt