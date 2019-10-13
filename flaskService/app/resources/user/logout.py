from flask_restful          import Resource
from flask                  import request
from flask_jwt_extended     import (
    get_jwt_identity,
    jwt_required,
    get_raw_jwt
)
from app.blacklist          import BLACKLIST

class UserLogout(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        user_id = get_jwt_identity()
        BLACKLIST.add(jti)
        return {"message": "The user {} has loged out".format(user_id)}, 200