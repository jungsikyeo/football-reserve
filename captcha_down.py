import os
import time

os.system("curl " + "https://yeyak.seoul.go.kr/web/captchaImg.do?ran=0.11323284418015866" +
          " > ./captcha_study_img/" + str(1) + ".png")

# for i in range(600):
#     time.sleep(3)
#     os.system("curl " + "https://yeyak.seoul.go.kr/web/captchaImg.do?ran=0.11323284418015866" +
#               " > ./captcha_study_img/" + str(i) + ".png")
