#################################
#THis lib is for Virtual Console#
#Version: Python Virtual Console#
#     Language: Chinese         #
#       版本：中文1.0P          #
#################################

import time
import sys
from os import system


Start = 'N'
user = "User"
Ver = "LOS.10"
ver = "LM.10"
version = "中文1.0P"

def wait(seconds):

    time.sleep(seconds)
    return

def clear():

    if started():
        if (sys.platform == 'win32'):
            system("cls")
        else:
            system("clear")
    else:
        printstopped()

def clear_():
    
    if (sys.platform == 'win32'):
        system("cls")
    else:
        system("clear")
    
def pause():
    
    system("pause")

def started():
    
    global Start
    if Start == 'N':
        return 0
    else:
        return 1

def printstopped():
    
    print("服务已停止！")

def printstarted():
    
    print("服务仍在运行！")

def start(LibName):
    
    global Start
    global user
    global Ver
    global ver
    global version
    
    if started():
        print("手机已经启动了哦！")
    else:
        clear_()
        print("[控制台]开始启动手机")
        print("(Powerd By ",ver,")")
        wait(5)
        print("[控制台]加载文件（通讯录、邮件、应用、文件）")
        print("[控制台]加载云文件（ICload、ITunes、Music）")
        wait(1)
        print("[信息]开始加载通讯录...")
        wait(3)
        print("[信息]中国电信（10000）、中国联通（10010）、中国移动（10086）")
        print("[信息]开始加载邮件...")
        wait(3)
        print("[信息]欢迎！",user,"用户！")
        print("[警告]没有关联的邮件账号！")
        print("[信息]开始加载应用...")
        wait(3)
        print("[信息]FaceTime等18个应用")
        print("[信息]开始加载照片")
        wait(3)
        print("[信息]无照片可加载！")
        print("[信息]开始加载云文件...")
        wait(3)
        print("[信息]欢迎！",user,"用户！")
        wait(5)
        print("...... 2 More]")
        wait(5)
        print("[信息]硬件版本：",Ver)
        print("[信息]软件版本：",ver)
        print("[信息]核心：",sys.argv[0])
        print("[信息]库：",LibName)
        print("[信息]控制台版本：",version)
        print("[信息]语言：简体中文")
        print("[控制台]手机启动完成！")
        print("[控制台]启动完成！")
        Start = 'Y'
        pause()
        clear()

def stop():
    
    global Start
    
    print("[控制台]正在停止服务...")
    wait(3)
    print("[控制台]停止成功！")
    Start = 'N'

def copyright():
    
    if started():
        print("Copyright (c) GLgele 2019-2020.All Rights Reserved.")
    else:
        printstopped()
        
def exit_():
    
    if started():
        printstarted()
    else:
        exit()

def help_(str):
    global Ver
    global ver
    global version
    if started():
        if str == "":
            print("该功能还在开发！")
        else:
            print("该功能还在开发！")
    else:
        printstopped()
    
def vcver(LibName):
    global Ver
    global ver
    global version
    if started():
        print("[信息]硬件版本：",Ver)
        print("[信息]软件版本：",ver)
        print("[信息]核心：VClib")#,sys.argv[0])
        print("[信息]库：VCP")#,LibName)
        print("[信息]控制台版本：",version)
        print("[信息]语言：简体中文")
    else:
        printstopped()
