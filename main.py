from flask import Flask, request,jsonify
from flask_restful import Resource, Api
import db,util,AES, otp_auth

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
      

class PostTransaction(Resource):
    def get(self,username,to,amount):
        util.encrypt_and_store(username,to,amount)
        util.decrypt_and_update()
        return {"status":"success"}

    def post(self):
    
        #insert=db.insert_transactions(tag,nonce,cyphertext)
        return request.get_json(force=True) 

class SendOtp(Resource):
    def get(self,email):
        otp_auth.send_otp(email)
        return{'status':"Success"}  

class VerifyOtp(Resource):
    def get(self,email,otp):
        status=otp_auth.verify_otp(email,otp)
        return{'about':status} 

api.add_resource(HelloWorld,'/')
api.add_resource(Auth,'/auth/<string:username>/<string:password>')
api.add_resource(UserData,'/user/<string:username>/<string:password>')
api.add_resource(PostTransaction,'/store/<string:username>/<string:to>/<string:amount>')
api.add_resource(SendOtp,'/otpsend/<string:email>')
api.add_resource(VerifyOtp,'/otpverify/<string:email>/<string:otp>')


#api.add_resource(StoreEncrypted,'/store/<string:tag>/<string:nonce>/<string:cyphertext>')

if __name__=='__main__':
    app.run(debug=True)


    