import math
import random
import smtplib

digits="0123456789"
OTP=""

for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    
otp = OTP + " is your OTP. Please do not share this with anybody."
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login("nabhan.a2@gmail.com", "bmfdactsbvpuifwp")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")

if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again.")