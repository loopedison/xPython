#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ==============================================================================
import os
import sys
import random

# ==============================================================================
def JigsawMain():
    os.system("mode con cols=20 lines=8")
    boxs = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
    random.shuffle(boxs)
    while True:
        os.system('cls')
        print("\033[1;31m"+"Welcome Jigsaw"+"\033[0m")
        print("\b\033[1;33m")
        print("*************")
        print("**  %s %s %s  **" %tuple(boxs)[0:3])
        print("**  %s %s %s  **" %tuple(boxs)[3:6])
        print("**  %s %s %s  **" %tuple(boxs)[6:9])
        print("*************")
        print("\b\033[0m")
        try :
            cmd = input("Move No. =>")
            if int(cmd) == 0:
                exit()
            if int(cmd) in range(1, 9):
                kong_index = boxs.index(' ')
                num_index = boxs.index(cmd)
                if (kong_index - num_index) in (-1, 1, 3, -3):
                    boxs[num_index], boxs[kong_index] = boxs[kong_index], boxs[num_index]
            if  boxs == ['1', '2', '3', '4', '5', '6', '7', '8', ' ']:
                print("\033[1;32m"+"Succeed!"+"\033[0m")
                os.system("pause")
        except ValueError:
            pass
#===============================================================================
if __name__ == "__main__":
    JigsawMain()