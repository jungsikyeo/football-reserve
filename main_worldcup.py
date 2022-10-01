#!/usr/local/bin python3
# -*- coding: utf8 -*-

from dataclasses import replace
from sys import exec_prefix
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import macro_config as mc
import glob
import CaptchaCracker as cc
import urllib.request
import os

options = Options()
options.add_extension("./1.3.2_0.crx")


def IsChecked(driver):
    check = driver.find_element(By.ID, "recaptcha-anchor")
    if check.get_attribute("aria-checked") == "true":
        return True
    else:
        return False


def IsExistByCss(driver, cssQuery):
    try:
        driver.find_element(By.CSS_SELECTOR, cssQuery)
    except:
        return False
    return True


# chrome driver 세팅(사용하는 크롬 버전에 맞춰서 다운로드 필요, 다운로드 사이트: https://chromedriver.chromium.org/downloads)
driver = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(driver, 10)

login_url = "https://yeyak.seoul.go.kr/web/loginForm.do?ru=aHR0cHM6Ly95ZXlhay5zZW91bC5nby5rci93ZWIvcmVzZXJ2YXRpb24vc2VsZWN0UmVzZXJ2Vmlldy5kbz9yc3Zfc3ZjX2lkPVMyMTEyMzAxNzU0MjcxNDQ5ODAmY29kZT1UMTAwJmRDb2RlPVQxMDkmc2NoX29yZGVyPTEmc2NoX2Nob29zZV9saXN0PSZzY2hfdHlwZT0mc2NoX3RleHQ9JUVDJTlCJTk0JUVCJTkzJTlDJUVDJUJCJUI1JnNjaF9yZWNwdF9iZWdpbl9kdD0mc2NoX3JlY3B0X2VuZF9kdD0mc2NoX3VzZV9iZWdpbl9kdD0mc2NoX3VzZV9lbmRfZHQ9JnNjaF9yZXFzdF92YWx1ZT0="

# 로그인 페이지 접속
driver.get(login_url)

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

time.sleep(1)
try:
    notice_elem = driver.find_element(
        By.XPATH, "/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button"
    )
    notice_elem.click()
except:
    pass

able_day_ok = False
iam_lose = False
loop = True
while loop:
    time.sleep(0.5)
    month_elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cal_top")))
    year_month_txt = month_elem.find_element(By.CLASS_NAME, "txt1")
    month = year_month_txt.text
    yyyymm = ((month.replace("년", "")).replace("월", "")).replace(" ", "")

    print(yyyymm, mc.reserve_day[:6])

    if yyyymm == mc.reserve_day[:6]:
        print(yyyymm, "검색 시작!")

        # 달력의 날짜 선택(macro_config.py 에서 reserve_day 값에 설정한 날짜)
        calendar_elem = driver.find_element(By.ID, "calendar")
        able_list = calendar_elem.find_elements(By.CLASS_NAME, "able")

        reserve_count_text = wait.until(
            EC.element_to_be_clickable((By.ID, "div_cal_" + mc.reserve_day))
        ).text
        print(reserve_count_text)
        reserve_count = reserve_count_text.split("/")[0]
        total_count = reserve_count_text.split("/")[1]

        print(reserve_count)

        if reserve_count == total_count:
            print("이미 예약이 완료되었습니다. 우리가 졌습니다.")
            iam_lose = True
            break

        for div_able_day in able_list:
            time.sleep(0.05)
            able_day_temp = div_able_day.get_attribute("id")
            able_day = able_day_temp.replace("calendar_", "")
            print("가능일자:", able_day)

            if able_day == mc.reserve_day:
                print(able_day, "가능!!")
                able_day_ok = True
                break

        if able_day_ok:
            try:
                wait = WebDriverWait(driver, 1)
                day_elem = wait.until(
                    EC.element_to_be_clickable((By.ID, "cal_" + mc.reserve_day))
                )
                day_elem.click()
            except:
                driver.refresh()

            try:
                time.sleep(0.1)
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
        if "(1/1)" in unit.text:
            continue

        print(unit.text)
        if mc.unit_time in unit.text:
            time.sleep(0.1)

            # 설정한 회차 선택
            unit.click()

            # 0.5초 딜레이
            time.sleep(0.1)

            # 이용인원 추가
            useteam_elem = driver.find_element(By.CLASS_NAME, "user_plus")
            useteam_elem.click()

            time.sleep(0.1)

            # 전체동의 클릭
            all_agree_elem = driver.find_element(
                By.XPATH,
                "/html/body/div/div[3]/div[2]/div/div[2]/form/div[3]/div[2]/div[5]/div[4]/span/label/span",
            )
            driver.execute_script("arguments[0].click();", all_agree_elem)

            time.sleep(0.1)

            # 신청자 정보와 동일 클릭
            same_person_elem = driver.find_element(
                By.XPATH,
                "/html/body/div/div[3]/div[2]/div/div[2]/form/div[3]/div[2]/div[4]/h5/span/label/span",
            )
            driver.execute_script("arguments[0].click();", same_person_elem)

            # 캡차 인증 확인
            time.sleep(0.1)

            if IsExistByCss(driver, "iframe[title='reCAPTCHA']"):
                first = driver.find_element(
                    By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"
                )
                driver.switch_to.frame(first)
                captchaCheckbox = driver.find_element(
                    By.CLASS_NAME, "recaptcha-checkbox"
                )
                driver.execute_script("arguments[0].click();", captchaCheckbox)

            try:
                driver.switch_to.default_content()
                result = driver.switch_to.alert()
                result.accept()
            except:
                pass

            time.sleep(0.3)

            # quick_btn_elem = driver.find_element(By.CLASS_NAME, "btn_quick")
            # quick_btn_elem.click()

            # time.sleep(0.1)

            # 예약하기 버튼 목록 검색 (8개 버튼중에 랜덤하게 나와서 검색 필요)
            driver.switch_to.default_content()
            reserve_btn_group_elem = driver.find_element(By.CLASS_NAME, "book_btn_box")
            reserve_btn_list_elem = reserve_btn_group_elem.find_elements(
                By.TAG_NAME, "li"
            )

            # 예약하기 실행
            for reserve_btn in reserve_btn_list_elem:
                if reserve_btn.text == "예약하기":
                    reserve_btn.click()

                    time.sleep(0.1)

                    try:
                        result = driver.switch_to.alert()
                        result.accept()
                    except:
                        pass

                    try:
                        WebDriverWait(driver, 3).until(EC.alert_is_present())
                        alert = driver.switch_to.alert

                        # 취소하기(닫기)
                        # alert.dismiss()

                        # 확인하기
                        alert.accept()
                    except:
                        pass
