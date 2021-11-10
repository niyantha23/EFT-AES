from flask import Flask, request
from flask_restful import Resource, Api
import db,util

app=Flask(__name__)
api =Api(app)

class HelloWorld(Resource):
    def get(self):
        return{'about':"Hello"}  

class Auth(Resource):
    def get(self,username,password):
        pwd=db.getpwd(username)
        hashedpwd=util.get_sha256(password)
        if(hashedpwd.hexdigest()==pwd):
            return {"status":"success"}
        else:
            return {"status":"fail"}



api.add_resource(HelloWorld,'/')
api.add_resource(Auth,'/auth/<string:username>/<string:password>')

if __name__=='__main__':
    app.run(debug=True)


    