# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyodbc
import pymysql
import requests
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import re
import os

# import pymssql

# 连接sqlserver
user_password = []


def input_info():
    try:
        t1 = int(input("输入信息： "))
        t3 = input("输入需要查询的客户ID：")
        match t1:
            case 1:
                t2 = int(input("是否确认： "))
                match t2:
                    case 1:
                        connect_sqlser(t3)
                    case 2:
                        print("退出了")
                        return ("走")
            case 2:
                t3 = int(input("是否确认： "))
                match t3:
                    case 1:
                        connect_mysql_57()
                    case 2:
                        print("退出了")
                        return ("走")
            case _:
                print("退出了")
                return ("走")
    except(AttributeError, ValueError, UnboundLocalError):
        print("请正确输入数字")


def connect_mysql_57():
    connection = pymysql.connect(
        host="172.16.60.221",
        user="app",
        password="pazJh.Yq.lFZk",
        database="",
        port=3306,
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute("select  * from app.f_dm_bf_mkt_salekpi_day limit 10")
    version = cursor.fetchall()
    if version:
        print('Runnning data: ', version)
    else:
        print('Not connected.')
    cursor.close()


def connect_sqlser(uid):
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server}; Server=172.16.60.211,1433\\sql;DATABASE=BI_DM;UID=SA;PWD=SHrl2021.sq1;TrustServerCertificate=yes;')
    cursor = cnxn.cursor()
    cursor.execute("select top 1 dynamic_password from  edw.dbo.fr_access_user where user_id = \'" + uid + '\'')
    for row in cursor:
        print(f'{row}')
    user_password.append(row[0])


def open_google():
    # s =Service(r"C:\Users\MLTY\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
    # driver = webdriver.Chrome(server=s)
    # driver.get("https://bi-charts.beautyfarm.com.cn/")

    driver = webdriver.Chrome(r"C:\Users\MLTY\AppData\Local\Programs\Python\Python310\Scripts\chromedriver.exe")
    driver.get(r"https://bi-charts.beautyfarm.com.cn/decision/login.html")
    time.sleep(50)


# driver.find_element_by_css_selector(r'//*[@id="wrapper"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/input').sleep(100).sent_key(user_password[0])
#  .find_element_by_xpath(r"/html/body/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/input").sleep(100).sent_key(user_password[0])


if __name__ == "__main__":
    input_info()
    # try:
    #     open_google()
    #     print(user_password[0])
    # except(AttributeError,IndexError,UnboundLocalError):
    #     print('"AttributeError error" or "请正确输入数字和工号"')
    open_google()
    print(user_password[0])
