########################
#Thanks for your using!#
#  Created by GLgele   #
########################

##########################
#  这只是个Python体验版  #
#迁移正在进行，敬请期待！#
#       GUI MOBILE       #
#   还在开发，敬请期待！ #
##########################

from os import system
import VClib as vclib
import sys


cmd = ''



def init():
    
    global cmd
    system("@echo off")
    while 1:
        print('>>', end = '')
        cmd = input()
        if (cmd.lower() == 'start'):
            break
        else:
            print('控制台还未启动！')
    vclib.start(sys.argv[0])
    vclib.clear()

def commands(stri):
    
    if stri == "start":
        vclib.start(sys.argv[0])
    elif stri == "stop":
        vclib.stop()
    elif stri == "clear":
        vclib.clear()
    elif stri == "copyright":
        vclib.copyright()
    elif stri == "exit":
        vclib.exit_()
    elif stri == "ver":
        vclib.vcver(sys.argv[0])
    elif stri == "help":
        vclib.help_()
    elif stri == "help copyright":
        vclib.help_("copyright")
    elif stri == "help ver":
        vclib.help_("vcver")
    else:
        print("未知的命令！")

def demo():

    global cmd
    
    init()
    while 1:
        print('>>', end = '')
        cmd = input()
        commands(cmd.lower())

