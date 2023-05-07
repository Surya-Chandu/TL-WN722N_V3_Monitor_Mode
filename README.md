# TL-WN722N_V3_Monitor_Mode
Enabling the Monitor mode and capturing the WIFI signals

https://www.youtube.com/watch?v=yTnYqrmb_wM&pp=ygUXdHAtbGluayB0bC13bjcyMm4gc2V0dXA%3D

First follow this youtube video and the video description has commands.
By following that command you can enable monitor mode.

commands
sudo apt update
sudo apt install bc
sudo rmmod r8188eu.ko
git clone https://github.com/aircrack-ng/rtl8188eus
cd rtl8188eus
sudo -i
echo "blacklist r8188eu.ko" > "/etc/modprobe.d/realtek.conf"
exit
make
sudo make install
sudo modprobe 8188eu

To enable Monitor mode
ifconfig wlan0 down
airmon-ng check kill
iwconfig wlan0 mode monitor
ifconfig wlan0 up
iwconfig 

This python GUI program will enable monitor mode every start of kali.
Every start of kali first we need to run this command:
sudo rmmod r8188eu.ko
sudo modprobe 8188eu
After that to eneble monitor mode commands will execute.

![Monitor_mode_file_image](https://user-images.githubusercontent.com/82871619/236670420-365f369a-cfd8-451c-9237-a5aa2df87e49.PNG)

This python GUI program can automate this process.
Just connect the wireless adapter to the kali machine, download this python file in kali download directory and open the terminal in download directory.
Run this command: python3 monitor_mode.py and enter.

![GUI_Interface](https://user-images.githubusercontent.com/82871619/236670455-c0de8d1d-c751-48bf-b622-88f2db3e86b0.PNG)

GUI program will popup It has two buttons, one is Monitor mode this button will execute all the commands
sudo rmmod r8188eu.ko
sudo modprobe 8188eu
ifconfig wlan0 down
airmon-ng check kill
iwconfig wlan0 mode monitor
ifconfig wlan0 up
iwconfig : –this command will show you that adaptor is in monitor mode.

![Showing_mod](https://user-images.githubusercontent.com/82871619/236670498-6712d601-0586-441f-891c-4470a034adc4.PNG)

We can notice that your wireless adaptor(TL-WN722N-V3) is in monitor mode.
If you are facing any problem to in changing to monitor mode close GUI.
Remove your adaptor and connect it again and run python3 monitor_mode.py and click on Monitor mode button.
After done with changing to monitor mode clisk on second button to close exit the program.

