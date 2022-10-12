#!/usr/local/bin python3
# -*- coding: utf8 -*-

from dataclasses import replace
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import macro_config as mc
import glob
import CaptchaCracker as cc
import urllib.request
import os

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

now = time


# print("현재 : ", now)
# print("현재 : ", now.localtime())
# print("timestamp : ", now.time())
# print("년 : ", now.localtime().tm_year)
# print("월 : ", now.localtime().tm_mon)
# print("일 : ", now.localtime().tm_mday)
# print("시 : ", now.localtime().tm_hour)
# print("분 : ", now.localtime().tm_min)
# print("초 : ", now.localtime().tm_sec)
# print("요일 : ", now.localtime().tm_wday)
# print("올해로부터 경과된 일 : ", now.localtime().tm_yday)
bot_on = False
while True:
    time.sleep(1)
    if now.localtime().tm_wday == 5 and now.strftime("%H:%M:%S") == "11:59:00":
        bot_on = True

    if bot_on:
        print("문자열 변환 : ", now.strftime("%Y-%m-%d %H:%M:%S"))
        if now.localtime().tm_wday == 5 and now.strftime("%H:%M:%S") == "11:59:40":
            print("bot start!!")

            chrome_options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=chrome_options
            )

            # chrome driver 세팅(사용하는 크롬 버전에 맞춰서 다운로드 필요, 다운로드 사이트: https://chromedriver.chromium.org/downloads)
            # driver = webdriver.Chrome("./chromedriver")
            wait = WebDriverWait(driver, 10)

            # 로그인 페이지 접속
            driver.get(mc.login_url)

            print(driver)

            # ID, PASSWD 입력
            id_elem = wait.until(EC.element_to_be_clickable((By.ID, "userid")))
            pass_elem = driver.find_element(By.ID, "userpwd")
            id_elem.clear()
            pass_elem.clear()
            id_elem.send_keys(mc.my_id)
            pass_elem.send_keys(mc.my_pw)

            # 로그인 실행
            login_elem = driver.find_element(By.CLASS_NAME, "btn_login")
            login_elem.click()

            able_day_ok = False
            iam_lose = False
            loop = True
            while loop:
                time.sleep(0.2)
                month_elem = wait.until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "cal_top"))
                )
                year_month_txt = month_elem.find_element(By.CLASS_NAME, "txt1")
                month = year_month_txt.text
                yyyymm = ((month.replace("년", "")).replace("월", "")).replace(" ", "")

                print(yyyymm, mc.reserve_day[:6])

                if yyyymm == mc.reserve_day[:6]:
                    print(yyyymm, "검색 시작!")

                    # 달력의 날짜 선택(macro_config.py 에서 reserve_day 값에 설정한 날짜)
                    calendar_elem = driver.find_element(By.ID, "calendar")
                    able_list = calendar_elem.find_elements(By.CLASS_NAME, "able")

                    reserve_count = calendar_elem.find_element(
                        By.ID, "div_cal_" + mc.reserve_day
                    ).text[0:1]

                    total_count = calendar_elem.find_element(
                        By.ID, "div_cal_" + mc.reserve_day
                    ).text[2:3]

                    print(reserve_count, total_count)

                    if reserve_count == total_count:
                        print("이미 예약이 완료되었습니다. 우리가 졌습니다.")
                        iam_lose = True
                        break

                    for div_able_day in able_list:
                        able_day = div_able_day.get_attribute("id").replace(
                            "calendar_", ""
                        )
                        print("가능일자:", able_day)

                        if able_day == mc.reserve_day:
                            print(able_day, "가능!!")
                            able_day_ok = True
                            break

                    if able_day_ok:
                        try:
                            wait = WebDriverWait(driver, 1)
                            day_elem = wait.until(
                                EC.element_to_be_clickable(
                                    (By.ID, "cal_" + mc.reserve_day)
                                )
                            )
                            day_elem.click()
                        except:
                            driver.refresh()

                        try:
                            # 예약 페이지로 이동
                            reserve_elem = driver.find_element(
                                By.XPATH,
                                "/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[2]/div/div/a[1]",
                            )
                            reserve_elem.click()
                            loop = False
                        except:
                            driver.refresh()
                    else:
                        print("예약가능한 날짜가 없음!")
                        driver.refresh()
                else:
                    month_next_elem = driver.find_element(
                        By.XPATH,
                        "/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[1]/div[2]/div/div/button",
                    )
                    # month_next_elem.click()
                    driver.execute_script("arguments[0].click();", month_next_elem)

            if not iam_lose and able_day_ok:
                # 회차 목록 찾기
                unit_group_elem = driver.find_element(By.ID, "useUnit")
                unit_list_elem = unit_group_elem.find_elements(By.TAG_NAME, "li")

                # 회차 선택(macro_config.py 에서 unit_time 값에 설정한 회차)
                for unit in unit_list_elem:
                    if mc.unit_time in unit.text:
                        try:
                            # 설정한 회차 선택
                            unit.click()

                            # 0.5초 딜레이
                            time.sleep(0.3)

                            # 이용인원 추가
                            useteam_elem = driver.find_element(
                                By.CLASS_NAME, "user_plus"
                            )
                            useteam_elem.click()

                            # 이용자 정보(이름, 휴대폰) 입력
                            name_elem = driver.find_element(By.ID, "form_name2")
                            phone_elem = driver.find_element(By.ID, "moblphone2")
                            name_elem.clear()
                            phone_elem.clear()
                            name_elem.send_keys(mc.my_name)
                            phone_elem.send_keys(mc.my_phone)

                            # 이미지 다운로드
                            capcha_img_elem = driver.find_element(By.ID, "captchaImg")
                            capcha_img = capcha_img_elem.screenshot_as_png
                            with open("./data/target.png", "wb") as file:
                                file.write(capcha_img)
                            # os.system("curl " + capcha_url + " > ./data/target.png")
                            # urllib.request.urlretrieve(capcha_url, "./data/target.jpg")

                            # 학습 이미지 데이터 경로
                            train_img_path_list = glob.glob(
                                "./train_numbers_only/*.png"
                            )

                            # 학습 이미지 데이터 크기
                            img_width = 237
                            img_height = 87

                            # # 모델 생성 인스턴스
                            # CM = cc.CreateModel(train_img_path_list, img_width, img_height)

                            # # 모델 학습
                            # model = CM.train_model(epochs=100)

                            # # 모델이 학습한 가중치 파일로 저장
                            # model.save_weights("./model/weights.h5")

                            # 타겟 이미지 라벨 길이
                            max_length = 6
                            # 타겟 이미지 라벨 구성요소
                            characters = {
                                "0",
                                "1",
                                "2",
                                "3",
                                "4",
                                "5",
                                "6",
                                "7",
                                "8",
                                "9",
                            }

                            # 모델 가중치 파일 경로
                            weights_path = "./model/weights.h5"

                            # 모델 적용 인스턴스
                            AM = cc.ApplyModel(
                                weights_path,
                                img_width,
                                img_height,
                                max_length,
                                characters,
                            )

                            # 타겟 이미지 경로
                            target_img_path = "./data/target.png"

                            # 예측값
                            pred = AM.predict(target_img_path)

                            print("pred:" + pred)

                            # 캡차 인증번호 입력
                            capcha_answer_elem = driver.find_element(
                                By.ID, "simplecaptcha_answer"
                            )
                            capcha_answer_elem.clear()
                            capcha_answer_elem.send_keys(pred)

                            # 캡차 인증 확인
                            capcha_answer_btn = driver.find_element(
                                By.ID, "btn_captcha_accept"
                            )
                            capcha_answer_btn.click()

                            time.sleep(0.1)

                            try:
                                result = driver.switch_to.alert()
                                result.accept()
                            except:
                                pass

                            # 전체동의 클릭
                            all_agree_elem = driver.find_element(
                                By.XPATH,
                                "/html/body/div/div[3]/div[2]/div/div[2]/form/div[3]/div[2]/div[6]/div[3]/span/input",
                            )
                            driver.execute_script(
                                "arguments[0].click();", all_agree_elem
                            )

                            time.sleep(0.3)

                            quick_btn_elem = driver.find_element(
                                By.CLASS_NAME, "btn_quick"
                            )
                            quick_btn_elem.click()

                            time.sleep(0.2)

                            # 예약하기 버튼 목록 검색 (8개 버튼중에 랜덤하게 나와서 검색 필요)
                            reserve_btn_group_elem = driver.find_element(
                                By.CLASS_NAME, "book_btn_box"
                            )
                            reserve_btn_list_elem = (
                                reserve_btn_group_elem.find_elements(By.TAG_NAME, "li")
                            )

                            # 예약하기 실행
                            for reserve_btn in reserve_btn_list_elem:
                                if reserve_btn.text == "예약하기":
                                    reserve_btn.click()

                                    time.sleep(0.3)

                                    # try:
                                    #     result = driver.switch_to.alert()
                                    #     result.accept()
                                    # except:
                                    #     pass

                                    try:
                                        WebDriverWait(driver, 3).until(
                                            EC.alert_is_present()
                                        )
                                        alert = driver.switch_to.alert

                                        # 취소하기(닫기)
                                        # alert.dismiss()

                                        # 확인하기
                                        alert.accept()
                                    except:
                                        pass
                        except:
                            driver.refresh()

            print("bot break!!")
            bot_on = False
