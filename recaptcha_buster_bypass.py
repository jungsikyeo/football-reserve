# https://github.com/teal33t/captcha_bypass
# Dont use this code for spy.

import unittest
import sys
import time

import numpy as np
import scipy.interpolate as si

from datetime import datetime
from time import sleep, time
from random import uniform, randint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import macro_config as mc

# Randomization Related
MIN_RAND = 0.24
MAX_RAND = 0.63
LONG_MIN_RAND = 0.78
LONG_MAX_RAND = 1.87

# Update this list with proxybroker http://proxybroker.readthedocs.io
PROXY = [
    {
        "host": "34.65.217.248",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.15,
        "error_rate": 0.0,
    },
    {
        "host": "198.46.160.38",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.36,
        "error_rate": 0.0,
    },
    {
        "host": "18.162.100.154",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.62,
        "error_rate": 0.0,
    },
    {
        "host": "18.210.69.172",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.22,
        "error_rate": 0.0,
    },
    {
        "host": "204.12.202.198",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.3,
        "error_rate": 0.0,
    },
    {
        "host": "23.237.100.74",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.32,
        "error_rate": 0.0,
    },
    {
        "host": "206.189.192.5",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.63,
        "error_rate": 0.0,
    },
    {
        "host": "23.237.173.109",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.4,
        "error_rate": 0.0,
    },
    {
        "host": "167.71.83.150",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.41,
        "error_rate": 0.0,
    },
    {
        "host": "34.93.171.222",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.92,
        "error_rate": 0.0,
    },
    {
        "host": "157.245.67.128",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.61,
        "error_rate": 0.0,
    },
    {
        "host": "18.162.89.135",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.71,
        "error_rate": 0.0,
    },
    {
        "host": "198.98.55.168",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.65,
        "error_rate": 0.0,
    },
    {
        "host": "157.245.124.217",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.7,
        "error_rate": 0.0,
    },
    {
        "host": "129.146.181.251",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.76,
        "error_rate": 0.0,
    },
    {
        "host": "134.209.188.111",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.78,
        "error_rate": 0.0,
    },
    {
        "host": "68.183.191.140",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.82,
        "error_rate": 0.0,
    },
    {
        "host": "35.192.138.9",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.29,
        "error_rate": 0.0,
    },
    {
        "host": "157.245.207.112",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.85,
        "error_rate": 0.0,
    },
    {
        "host": "68.183.191.248",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.87,
        "error_rate": 0.0,
    },
    {
        "host": "165.22.54.37",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.88,
        "error_rate": 0.0,
    },
    {
        "host": "71.187.28.75",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.34,
        "error_rate": 0.0,
    },
    {
        "host": "157.245.205.81",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.92,
        "error_rate": 0.0,
    },
    {
        "host": "45.76.255.157",
        "port": 808,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.45,
        "error_rate": 0.0,
    },
    {
        "host": "157.245.197.92",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 1.01,
        "error_rate": 0.0,
    },
    {
        "host": "159.203.87.130",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.47,
        "error_rate": 0.0,
    },
    {
        "host": "50.195.185.171",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 1.03,
        "error_rate": 0.0,
    },
    {
        "host": "144.202.20.56",
        "port": 808,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.51,
        "error_rate": 0.0,
    },
    {
        "host": "157.230.250.116",
        "port": 8080,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 1.14,
        "error_rate": 0.0,
    },
    {
        "host": "104.196.70.154",
        "port": 3128,
        "geo": {
            "country": {"code": "US", "name": "United States"},
            "region": {"code": "Unknown", "name": "Unknown"},
            "city": "Unknown",
        },
        "types": [{"type": "HTTPS", "level": ""}],
        "avg_resp_time": 0.64,
        "error_rate": 0.0,
    },
]

index = int(uniform(0, len(PROXY)))
PROXY = PROXY[index]["host"] + ":" + str(PROXY[index]["port"])


class SyncMe(unittest.TestCase):

    number = None
    headless = False
    options = None
    profile = None
    capabilities = None

    # Setup options for webdriver
    def setUpOptions(self):
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("extensions.lastAppBuildId", "<apppID> -1 ")
        # self.options.add_option('useAutomationExtension', False)
        self.options.headless = self.headless

    # Setup profile with buster captcha solver
    def setUpProfile(self):
        self.profile = webdriver.FirefoxProfile(
            profile_directory="/Users/yjs/Library/Application Support/Firefox/Profiles/5duo75wh.auto-profile"
        )
        self.profile.add_extension(extension="buster_captcha_solver-1.3.1.xpi")
        # self.profile._install_extension("buster_captcha_solver-1.3.1.xpi", unpack=False)

        self.profile.set_preference("security.fileuri.strict_origin_policy", False)
        self.profile.update_preferences()

    # Enable Marionette, An automation driver for Mozilla's Gecko engine

    def setUpCapabilities(self):
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.capabilities["marionette"] = True

    # Setup proxy
    def setUpProxy(self):
        self.log(PROXY)
        self.capabilities["proxy"] = {
            "proxyType": "MANUAL",
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
        }

    # Setup settings
    def setUp(self):
        # self.setUpProfile()
        self.setUpOptions()
        self.setUpCapabilities()
        # self.setUpProxy() # comment this line for ignore proxy

        # On Linux?
        # https://github.com/mozilla/geckodriver/issues/1756
        # binary = FirefoxBinary('/usr/lib/firefox-esr/firefox-esr')
        # self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile, executable_path='./geckodriver_linux', firefox_binary=binary)
        self.driver = webdriver.Firefox(
            options=self.options,
            capabilities=self.capabilities,
            firefox_profile=self.profile,
            executable_path="./geckodriver_macOS",
        )

    # Simple logging method
    def log(s, t=None):
        now = datetime.now()
        if t == None:
            t = "Main"
        print("%s :: %s -> %s " % (str(now), t, s))

    # Use time.sleep for waiting and uniform for randomizing
    def wait_between(self, a, b):
        rand = uniform(a, b)
        sleep(rand)

    # Using B-spline for simulate humane like mouse movments
    def human_like_mouse_move(self, action, start_element, move):
        points = [[6, 2], [3, 2], [0, 0], [0, 2]]
        points = np.array(points)
        x = points[:, 0]
        y = points[:, 1]

        t = range(len(points))
        ipl_t = np.linspace(0.0, len(points) - 1, 100)

        x_tup = si.splrep(t, x, k=1)
        y_tup = si.splrep(t, y, k=1)

        x_list = list(x_tup)
        xl = x.tolist()
        x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

        y_list = list(y_tup)
        yl = y.tolist()
        y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

        x_i = si.splev(ipl_t, x_list)
        y_i = si.splev(ipl_t, y_list)

        startElement = start_element

        action.move_to_element(startElement)
        action.perform()

        c = move  # change it for more move
        i = 0
        for mouse_x, mouse_y in zip(x_i, y_i):
            action.move_by_offset(mouse_x, mouse_y)
            action.perform()
            self.log("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
            i += 1
            if i == c:
                break

    def do_captcha(self, driver):

        driver.switch_to.default_content()
        self.log("Switch to new frame")
        iframes = driver.find_elements_by_tag_name("iframe")
        driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

        self.log("Wait for recaptcha-anchor")
        check_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
        )

        self.log("Wait")
        self.wait_between(MIN_RAND, MAX_RAND)

        action = ActionChains(driver)
        self.human_like_mouse_move(action, check_box, 3)

        self.log("Click")
        check_box.click()

        self.log("Wait")
        self.wait_between(MIN_RAND, MAX_RAND)

        self.log("Mouse movements")
        action = ActionChains(driver)
        self.human_like_mouse_move(action, check_box, 3)

        self.log("Switch Frame")
        driver.switch_to.default_content()
        iframes = driver.find_elements_by_tag_name("iframe")
        driver.switch_to.frame(iframes[1])

        self.log("Wait")
        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        # self.log("Find audio button")
        # audio_btn = WebDriverWait(driver, 50).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, '//button[@id="recaptcha-audio-button"]'))
        # )

        # self.log("Wait")
        # driver.implicitly_wait(10)

        # self.log("Click")
        # audio_btn.click()

        # self.log("Wait")
        # self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        # self.log("Find solver button")
        # capt_btn = WebDriverWait(driver, 50).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, '//button[@id="solver-button"]'))
        # )

        # self.log("Wait")
        # self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        # self.log("Click")
        # capt_btn.click()

        # self.log("Wait")
        # self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        # try:
        #     self.log("Alert exists")
        #     alert_handler = WebDriverWait(driver, 20).until(
        #         EC.alert_is_present()
        #     )
        #     alert = driver.switch_to.alert
        #     self.log("Wait before accept alert")
        #     self.wait_between(MIN_RAND, MAX_RAND)

        #     alert.accept()

        #     self.wait_between(MIN_RAND, MAX_RAND)
        #     self.log("Alert accepted, retry captcha solver")

        #     self.do_captcha(driver)
        # except:
        #     self.log("No alert")

        # self.log("Wait")
        # driver.implicitly_wait(5)
        # self.log("Switch")
        # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        driver.switch_to.default_content()

    # Main function

    def test_run(self):
        # driver = self.driver
        # number = self.number

        # self.log("Start get")
        # driver.get('https://sync.me')
        # self.log("End get")

        # self.log("Send phone")

        # # sync.me seems to have moved away from IDs
        # # phone_input = driver.find_element_by_xpath('//*[@id="mobile-number"]')
        # phone_input = driver.find_element_by_xpath(
        #     '//input[@placeholder="Search any phone number"]')
        # phone_input.send_keys(number)

        # self.log("Wait")
        # self.wait_between(MIN_RAND, MAX_RAND)

        # search_btn = WebDriverWait(driver, 20).until(
        #     # EC.presence_of_element_located((By.ID ,"submit"))
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//button[contains(@class, "SearchNumber_searchNumber__find")]'))
        # )

        # self.log("Wait")
        # self.wait_between(MIN_RAND, MAX_RAND)
        # search_btn.click()

        # self.log("Wait")
        # self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        # self.do_captcha(driver)

        # self.log("Done")

        driver = self.driver
        wait = WebDriverWait(driver, 10)

        login_url = "https://yeyak.seoul.go.kr/web/loginForm.do?ru=aHR0cHM6Ly95ZXlhay5zZW91bC5nby5rci93ZWIvcmVzZXJ2YXRpb24vc2VsZWN0UmVzZXJ2Vmlldy5kbz9yc3Zfc3ZjX2lkPVMyMTEyMzAxNzU0MjcxNDQ5ODAmY29kZT1UMTAwJmRDb2RlPVQxMDkmc2NoX29yZGVyPTEmc2NoX2Nob29zZV9saXN0PSZzY2hfdHlwZT0mc2NoX3RleHQ9JUVDJTlCJTk0JUVCJTkzJTlDJUVDJUJCJUI1JnNjaF9yZWNwdF9iZWdpbl9kdD0mc2NoX3JlY3B0X2VuZF9kdD0mc2NoX3VzZV9iZWdpbl9kdD0mc2NoX3VzZV9lbmRfZHQ9JnNjaF9yZXFzdF92YWx1ZT0="

        # 로그인 페이지 접속
        driver.get(login_url)

        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

        # ID, PASSWD 입력
        id_elem = wait.until(EC.element_to_be_clickable((By.ID, "userid")))
        pass_elem = driver.find_element_by_id("userpwd")
        id_elem.clear()
        pass_elem.clear()
        id_elem.send_keys(mc.my_id)
        pass_elem.send_keys(mc.my_pw)

        # 로그인 실행
        login_elem = driver.find_element_by_class_name("btn_login")
        login_elem.click()

        self.wait_between(2, 2)
        notice_elem = driver.find_element_by_xpath(
            "/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button"
        )
        notice_elem.click()

        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div[3]/div[2]/div/div[1]/div/div[2]/button")
            )
        )

        able_day_ok = False
        iam_lose = False
        loop = True
        while loop:
            self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)
            month_elem = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cal_top"))
            )
            year_month_txt = month_elem.find_element_by_class_name("txt1")
            month = year_month_txt.text
            yyyymm = ((month.replace("년", "")).replace("월", "")).replace(" ", "")

            self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

            print(yyyymm, mc.reserve_day[:6])

            if yyyymm == mc.reserve_day[:6]:
                print(yyyymm, "검색 시작!")

                # 달력의 날짜 선택(macro_config.py 에서 reserve_day 값에 설정한 날짜)
                calendar_elem = driver.find_element_by_id("calendar")
                able_list = calendar_elem.find_elements_by_class_name("able")

                reserve_count_text = calendar_elem.find_element_by_id(
                    "div_cal_" + mc.reserve_day
                ).text
                reserve_count = reserve_count_text.split("/")[0]
                total_count = reserve_count_text.split("/")[1]

                print(reserve_count)

                if reserve_count == total_count:
                    print("이미 예약이 완료되었습니다. 우리가 졌습니다.")
                    iam_lose = True
                    break

                for div_able_day in able_list:
                    able_day = div_able_day.get_attribute("id").replace("calendar_", "")
                    print("가능일자:", able_day)

                    if able_day == mc.reserve_day:
                        print(able_day, "가능!!")
                        able_day_ok = True
                        break

                if able_day_ok:
                    day_elem = wait.until(
                        EC.element_to_be_clickable((By.ID, "cal_" + mc.reserve_day))
                    )
                    day_elem.click()

                    self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                    try:
                        # 예약 페이지로 이동
                        reserve_elem = driver.find_element(
                            By.XPATH,
                            "/html/body/div/div[3]/div[2]/div/form[2]/div[1]/div[2]/div/div/a[1]",
                        )
                        reserve_elem.click()

                        self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                        loop = False
                    except:
                        pass
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
            unit_group_elem = driver.find_element_by_id("useUnit")
            unit_list_elem = unit_group_elem.find_elements(By.TAG_NAME, "li")

            # 회차 선택(macro_config.py 에서 unit_time 값에 설정한 회차)
            for unit in unit_list_elem:
                if "(1/1)" in unit.text:
                    continue

                print(unit.text)
                if mc.unit_time in unit.text:
                    # 설정한 회차 선택
                    unit.click()

                    # 0.5초 딜레이
                    self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                    # 전체동의 클릭
                    all_agree_elem = driver.find_element_by_xpath(
                        "/html/body/div/div[3]/div[2]/div/div[2]/form/div[3]/div[2]/div[5]/div[4]/span/label/span"
                    )
                    driver.execute_script("arguments[0].click();", all_agree_elem)

                    self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                    # 신청자 정보와 동일 클릭
                    same_person_elem = driver.find_element_by_xpath(
                        "/html/body/div/div[3]/div[2]/div/div[2]/form/div[3]/div[2]/div[4]/h5/span/label/span"
                    )
                    driver.execute_script("arguments[0].click();", same_person_elem)

                    self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                    # 이용인원 추가
                    useteam_elem = driver.find_element_by_class_name("user_plus")
                    useteam_elem.click()

                    self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                    # 이용자 정보(이름, 휴대폰) 입력
                    name_elem = driver.find_element_by_id("form_name2")
                    phone_elem = driver.find_element_by_id("moblphone2")
                    name_elem.clear()
                    phone_elem.clear()
                    name_elem.send_keys(mc.my_name)
                    phone_elem.send_keys(mc.my_phone)

                    self.wait_between(LONG_MIN_RAND, LONG_MAX_RAND)

                    quick_btn_elem = driver.find_element_by_class_name("btn_quick")
                    quick_btn_elem.click()

                    # 캡차 인증 확인
                    # capcha_answer_btn = driver.find_element_by_xpath(
                    #     "/html/body/div[1]/div[3]/div[2]/div/div[2]/form/div[3]/div[2]/div[4]/table/tbody/tr[8]/td/div/div/div/iframe")
                    # driver.execute_script(
                    #     "arguments[0].click();", capcha_answer_btn)
                    self.do_captcha(driver)

                    # try:
                    #     result = driver.switch_to.alert()
                    #     result.accept()
                    # except:
                    #     pass

                    # 예약하기 버튼 목록 검색 (8개 버튼중에 랜덤하게 나와서 검색 필요)
                    reserve_btn_group_elem = driver.find_element_by_class_name(
                        "book_btn_box"
                    )
                    reserve_btn_list_elem = reserve_btn_group_elem.find_elements(
                        By.TAG_NAME, "li"
                    )

                    # 예약하기 실행
                    for reserve_btn in reserve_btn_list_elem:
                        if reserve_btn.text == "예약하기":
                            reserve_btn.click()

                            self.wait_between(MIN_RAND, MAX_RAND)

                            # try:
                            #     result = driver.switch_to.alert()
                            #     result.accept()
                            # except:
                            #     pass

                            try:
                                WebDriverWait(driver, 3).until(EC.alert_is_present())
                                alert = driver.switch_to.alert

                                # 취소하기(닫기)
                                # alert.dismiss()

                                # 확인하기
                                alert.accept()
                            except:
                                pass

    def tearDown(self):
        self.wait_between(21.13, 31.05)


if __name__ == "__main__":
    unittest.main()
