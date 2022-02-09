# WELCOME BACK 
# LETS GET started

import os
import math
import random
import smtplib

digits="1234567890"
OTP=""
for i in range(8):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"your otp is: "
msg=otp
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("YOUr_gmail id","your gamil pass")
emailid=input("Enter your email id: ")
s.sendemail('reciever_email',emailid,msg)
a= input("Please enter your otp: ")

if a==OTP:
    print("Verified")
else:
    print("Wrong please check again ")
# working  then bye eeeee !