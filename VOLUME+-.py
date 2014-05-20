import subprocess
import pythoncom, pyHook 
import os
import win32api, win32con
from win32api import GetSystemMetrics
import os.path
import ConfigParser
import time
import sys

config = ConfigParser.RawConfigParser()

#c:/Python27/python.exe c:/Users/Amar/Documents/volume+/main.py

# C:\Program Files (x86)\Webteh\BSPlayer\bsplayer.exe

if hasattr(sys, 'frozen'):
  # retrieve path from sys.executable
  rootdir = os.path.abspath(os.path.dirname(sys.executable))
else:
  # assign a value from __file__
  rootdir = os.path.abspath(os.path.dirname(__file__))


if os.path.isfile("%s/config.cfg"%rootdir):
   #I must add config self creating to reduce program's size
   print 15 * "/"
   print "Config loaded..."
   print "VOLUME+- working properly..."
   print "MADE BY AMAR 'BRIX' KALABIC"
   print 15 * "/"
   print 15 * "*"
   print "CONTROLS:"
   #config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
   config.read('%s/config.cfg'%rootdir)
   print "Volume UP key:", config.get("main", "volume-up-key")
   print "Volume DOWN key:", config.get("main", "volume-down-key")
   print 15 * "*"
else:
   config.add_section('main')
   #config.set('main', 'exampleprogram', '/full/path/to/program')
   config.set('main', 'enable-key-logging', 'on')
   config.set('main', 'volume-up-key', 'U')
   config.set('main', 'volume-down-key', 'D')
   with open('config.cfg', 'wb') as configfile:
        config.write(configfile)
        print "Configuration file is created. Check 'config.cfg' in VOLUME+ folder."
        print 15 * "/"
        print "Config loaded..."
        print "VOLUME+- working properly..."
        print "MADE BY AMAR 'BRIX' KALABIC"
        print 15 * "/"
        print 15 * "*"
        print "CONTROLS:"
        #config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
        config.read('%s/config.cfg'%rootdir)
        print "Volume UP key:", config.get("main", "volume-up-key")
        print "Volume DOWN key:", config.get("main", "volume-down-key")
        print 15 * "*"

#print "WARNING: if you are entering new program name, name it same as window name of that program."
#input1 = raw_input("Please enter new or existing program name (same as in config):")

#if input1 in open("%s/config.cfg"%os.path.abspath(os.path.dirname(__file__))).read():
#   pass
#else:
#   input2 = raw_input("Please enter FULL path to program (like C:/Users/Amar/program.exe):")
#   config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
#   config.set('main', input1, input2)

def get_master_volume(): #not being used at the moment, this will probably be used in future versions for "per app sound" feature...
    #config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
    config.read('%s/config.cfg'%rootdir)
    p = "%s sget Master"%config.get('main', input1)
    print("PROG:", p)
    proc = subprocess.Popen(p, stdout=subprocess.PIPE)

    proc.wait()

    amixer_stdout = proc.communicate()[0].split('\n')
    print("OUTPUT", amixer_stdout)
    amixer_stdout = amixer_stdout[4]

    find_start = amixer_stdout.find('[') + 1
    find_end = amixer_stdout.find('%]', find_start)

    return float(amixer_stdout[find_start:find_end])
    
def set_master_volume(volume): #not being used at the moment, this will probably be used in future versions for "per app sound" feature...
    #config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
    config.read('%s/config.cfg'%rootdir)
    val = float(int(volume))

    proc = subprocess.Popen('%s sset Master '%config.get('main', input1) + str(val) + '%', shell=True, stdout=subprocess.PIPE)
    proc.wait()

def OnKeyboardEvent(event):
    state = False
    #config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
    config.read('%s/config.cfg'%rootdir)
    if config.getboolean("main", "enable-key-logging") == True:
       print 10 * '---'
       print 'MessageName:',event.MessageName
       print 'Message:',event.Message
       print 'Time:',event.Time
       print 'Window:',event.Window
       print 'WindowName:',event.WindowName
       print 'Ascii:', event.Ascii, chr(event.Ascii)
       print 'Pressed key:', event.Key
       print 'Ascii:', event.Ascii, chr(event.Ascii)
       print 'KeyID:', event.KeyID
       print 'ScanCode:', event.ScanCode
       print 'Extended:', event.Extended
       print 'Injected:', event.Injected
       print 'Alt', event.Alt
       print 'Transition', event.Transition
       print 10 * '---'
    #config.read('%s/config.cfg'%os.path.abspath(os.path.dirname(__file__)))
    config.read('%s/config.cfg'%rootdir)
    #print "Working directory:", os.getcwd()
    if event.Key == config.get("main", "volume-up-key"):
       #if event.WindowName.startswith(input1):
       #   if input1 in open("%s/config.cfg"%os.path.abspath(os.path.dirname(__file__))).read():
       #      set_master_volume(get_master_volume() + 1)
       #      print "New volume:", get_master_volume()
       win32api.keybd_event(0xAF,0,1,0) #0xAF is volume UP
       print("VOLUME +++++")
    elif event.Key == config.get("main", "volume-down-key"):
         #if event.WindowName.startswith(input1):
         #   if config.has_option('main', input1):
         #      set_master_volume(get_master_volume() - 1)
         #      print "New volume:", get_master_volume()
         win32api.keybd_event(0xAE,0,1,0) #0xAF is volume DOWN
         print("VOLUME -----")
 
# return True to pass the event to other handlers
    return True
 
# create a hook manager
hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
   