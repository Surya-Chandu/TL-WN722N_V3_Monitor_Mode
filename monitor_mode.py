#!/use/bin/env python3

from tkinter import *
import subprocess
import os

root = Tk(className=" Auto to Monitor mode")
root. geometry("500x200")

def monmod():
    subprocess.call(["ifconfig"])
    subprocess.call(["ifconfig", "wlan0", "up"])
    os.chdir('/root/rtl8188eus/')
    r_mov = ('rmmod ' + 'r8188eu.ko')
    subprocess.call(r_mov, shell=True)
    mod_pro = ('modprobe ' + '8188eu')
    subprocess.call(mod_pro, shell=True)
    subprocess.call(["ifconfig", "wlan0", "up"])
    subprocess.call(["ifconfig", "wlan0", "down"])
    subprocess.call(["airmon-ng", "check", "kill"])
    subprocess.call(["iwconfig", "wlan0", "mode", "monitor"])
    subprocess.call(["ifconfig", "wlan0", "up"])
    subprocess.call(["iwconfig"])
    label = Label(root, text="Check your wireless adapter is Monitor mode now !!!!! Hey !!!!!")
    label.pack()

label = Label(root, text="Make sure your wireless adapter is pluged in and connected to kali")
label.pack()
button = Button(root, text="Monitor mode", command=monmod)
button.pack()
exi_but = Button(root, text="Exit", command=root.destroy)
exi_but.pack()

root.mainloop()