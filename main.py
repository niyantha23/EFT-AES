from flask import Flask, request,jsonify
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

class UserData(Resource):
    def get(self,username,password):
        pwd=db.getpwd(username)
        hashedpwd=util.get_sha256(password)
        if(hashedpwd.hexdigest()==pwd):
            record=db.getAll(username)
            return {"username":record.name,"dob":record.dob,"email":record.email,"amount":record.amount}
        else:
            return {"status":"Invalid credential"}


# make endpoint to store tag nonce and encrypted data in db
class StoreEncrypted(Resource):
    def post(self,tag,nonce,cyphertext):
        insert=db.insert_transactions(tag,nonce,cyphertext)
        return {"status"}        

api.add_resource(HelloWorld,'/')
api.add_resource(Auth,'/auth/<string:username>/<string:password>')
api.add_resource(UserData,'/user/<string:username>/<string:password>')
#api.add_resource(StoreEncrypted,'/store/<string:tag>/<string:nonce>/<string:cyphertext>')

if __name__=='__main__':
    app.run(debug=True)


    