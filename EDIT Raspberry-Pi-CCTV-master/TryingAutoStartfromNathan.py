####-------------autostart------------------

import os

output=os.system('mkdir -p .config/lxsession/LXDE-pi')
output=os.system('cp /etc/xdg/lxsession/LXDE-pi/autostart .config/lxsession/LXDE-pi')
output=os.system('sudo nano /etc/xdg/lxsession/LXDE-pi/autostart')

cwd = os.getcwd()
#f= open("/etc/rc.local","w+")
#f= open("/home/pi/.config/lxsession/LXDE-pi/autostart","w")
text='''@lxpanel --profile LXDE-pi\n@pcmanfm --desktop --profile LXDE-pi\n@xscreensaver -no-splash'''
text=text+'''\n@sleep 10 \n@sudo python3 '''+str(cwd)+'''/DesktopCover.py & \n@sudo python3 '''+str(cwd)+'''/Start_Here.py &\n'''
text=text+'''@sudo rm /home/pi/lock.txt'''

print(text)
user_input5=input(text +'Is this correct (y/n)?')[0]
if (user_input5=='y'):
    f.write(text)
    f.flush()
    f.close()
    #adding absolute 
    f= open(str(cwd)+"/Start_Here.py","r")
    text=f.read()
    text=text.replace('''working_dirctory=''''','working_dirctory='+"'"+str(cwd)+'/'+"'")
    f.close()
    f= open(str(cwd)+"/Start_Here.py","w")
    f.write(text)
    f.flush()
    f.close()
    #adding absolute
    f= open(str(cwd)+"/CorrectVeiw.py","r")
    text=f.read()
    f.close()
    text=text.replace('''working_dirctory=''''','working_dirctory='+"'"+str(cwd)+'/'+"'")
    f= open(str(cwd)+"/CorrectVeiw.py","w")
    f.write(text)
    f.flush()
    f.close()
        
