from flask_restful import Resource



class Bills(Resource):
    def get(self, id):
        return {"get": id}, 201

    def post(self):
        return {"post": "this is posting"}

