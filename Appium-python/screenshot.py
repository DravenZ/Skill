# -*- coding: utf-8 -*-
import os
import unittest
import platform
import tempfile
import shutil
from PIL import Image, ImageDraw, ImageFont

from appium import webdriver
from time import sleep
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['app'] = 'F:\\ytsjb_v2.3.0_230_prd.apk'
        desired_caps['appPackage'] = 'com.yatang.xc.xcr'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        #卸载app
        #print("remove app")
        #self.driver.remove_app('com.yatang.xc.xcr')
        self.driver.quit()

    def test_main(self):
        #测试开始
        print("start testing...")
        sleep(5)

        setFont = ImageFont.truetype('simsun.ttc', 50)
        fillColor = "#ff0000"

        try:
            element = self.driver.find_element_by_id('com.yatang.xc.xcr:id/butLogin')
            print element
            element1 = self.driver.find_element_by_id('111')
            print element1
            element.click()
            self.driver.get_screenshot_as_file("F:/error_png.png")

            # 获取元素bounds
            location = element.location
            size = element.size
            box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
            image = Image.open("F:/error_png.png")
            newImage = image.crop(box)
            newImage.save("F:/error_png1.png")

            # 图片上写字
            image = Image.open("F:/error_png.png")
            draw = ImageDraw.Draw(image)
            width, height = image.size
            draw.text((40, height - 100), u'广告', font=setFont, fill=fillColor)
            image.save('F:/error_png3.png')
        except:
            self.driver.get_screenshot_as_file("F:/error_png11.png")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)