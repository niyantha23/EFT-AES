import math
import random
import smtplib
import db

def send_otp(email):    
    digits="0123456789"
    OTP=""

    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otps=OTP    
    otp = OTP + " is your OTP. Please do not share this with anybody."
    msg = otp

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    s.login("nabhan.a2@gmail.com", "bmfdactsbvpuifwp")
    #emailid = input("Enter your email: ")
    emailid=email
    s.sendmail('&&&&&&&&&&&',emailid,msg)
    db.insert_otp(email,otps)

def verify_otp(email,otp):
    #a = input("Enter Your OTP >>: ")
    OTP=db.get_otp(email)
    a=otp
    if a == OTP:
        status="Verified"
    else:
        status="Please Check your OTP again."
    return status
