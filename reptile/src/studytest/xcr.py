#coding=utf-8
from appium import webdriver
import time

def xcr():
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['app'] = 'D:\XCTZ_3.1.1test.apk'
    desired_caps['appName']='asuper.yt.cn.supermarket'
    desired_caps['appActivity'] = '.activity.SplashActivity'

    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    time.sleep(2)#休息2s，进行加载

    try:
        driver.find_element_by_id('asuper.yt.cn.supermarket:id/update_operation')
        driver.find_element_by_class_name('android.widget.Button').click()
        time.sleep(2)
        driver.find_element_by_id('asuper.yt.cn.supermarket:id/email').send_keys('chenqiuju')#定位并输入账号
        driver.find_element_by_id('asuper.yt.cn.supermarket:id/password').send_keys('123456')#定位并输入密码
        driver.find_element_by_id('asuper.yt.cn.supermarket:id/email_sign_in_button').click()#点击登录
        print 'successfully'
    except:
        print 'fail'


if __name__ == '__main__':
    xcr()