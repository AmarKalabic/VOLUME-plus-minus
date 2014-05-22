import sys, Tkinter
sys.modules['tkinter'] = Tkinter 
import subprocess
import pythoncom, pyHook 
import os
import win32api, win32con
from win32api import GetSystemMetrics
import os.path
import ConfigParser
import time
from tkinter import *
import tkMessageBox
import PIL
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import time

config = ConfigParser.RawConfigParser()

if hasattr(sys, 'frozen'):
  # retrieve path from sys.executable
  rootdir = os.path.abspath(os.path.dirname(sys.executable))
else:
  # assign a value from __file__
  rootdir = os.path.abspath(os.path.dirname(__file__))


def beenClicked():
    global app
    a = tkMessageBox.showinfo("VOLUME+-", "Thanks for using VOLUME+-")
    time.sleep(3)
    app.destroy()
    return

def changeLabel():
    name = "Thanks for the click " + yourName.get()
    labelText.set(name)
    yourName.delete(0, END)
    yourName.insert(0, "Test")
    return


app = Tk()
app.configure(background='#000000')
app.wm_iconbitmap('%s/img/volume_-_16x16.ico'%rootdir)
#imgPath = '%s/img/volume+-_16x16.gif'%rootdir
#photo = PhotoImage(file = imgPath)
#label = Label(image = photo)
#label.image = photo
#label.grid(row = 3, column = 1, padx = 5, pady = 5)
#2 img = PhotoImage(file='%s/img/volume+-_16x16.png'%rootdir)
#2 app.tk.call('wm', 'iconphoto', app._w, img)
#app.iconbitmap(default='%s/img/volume+-_16x16.ico'%rootdir)
app.title("VOLUME+-")
app.geometry('450x350+200+200')

var1 = StringVar()
e1 = Entry(app, textvariable=var1)
e1.pack()

var1.set("Volume up key")

var2 = StringVar()
e2 = Entry(app, textvariable=var2)
e2.pack()

var2.set("Volume down key")

def changeConfig():
    if os.path.isfile("%s/config.cfg"%rootdir):
       config.read(r'%s/config.cfg'%rootdir)
       if len(var1.get()) == 1:
          if var1.get().isdigit() or var1.get().isalpha():
             if len(var2.get()) == 1:
                if var2.get().isdigit() or var2.get().isalpha():
                   config.set("main", "volume-up-key", var1.get())
                   config.set("main", "volume-down-key", var2.get())
                   beenClicked()
                   with open('%s/config.cfg'%rootdir, 'wb') as configfile:
                        config.write(configfile)
                else:
                    a = tkMessageBox.showerror("VOLUME+-", "Volume down must be alphanumeric!")
             else:
                 a = tkMessageBox.showerror("VOLUME+-", "Volume down must be made of only one letter or number!")
          else:
             a = tkMessageBox.showerror("VOLUME+-", "Volume up must be alphanumeric!")
       else:
           a = tkMessageBox.showerror("VOLUME+-", "Volume up must be made of only one letter or number!")
    else:
       var1.delete(0, END)
       var1.set("There is no config file!")
       var2.delete(0, END)
       var2.set("Let us create it for you after clicking START! (Default keys will be assigned")

def chgcfg():
    if os.path.isfile("%s/config.cfg"%rootdir):
       w = tkMessageBox.showerror("VOLUME+-", CheckVar1.get())
       if CheckVar1.get() == "1":
          config.read(r'%s/config.cfg'%rootdir)
          config.set("main", "enable-key-logging", "on")
          with open('%s/config.cfg'%rootdir, 'wb') as configfile:
               config.write(configfile)
       else:
          config.read(r'%s/config.cfg'%rootdir)
          config.set("main", "enable-key-logging", "off")
          with open('%s/config.cfg'%rootdir, 'wb') as configfile:
               config.write(configfile)
    else:
       var1.delete(0, END)
       var1.set("There is no config file!")
       var2.delete(0, END)
       var2.set("Let us create it for you after clicking START! (Default keys will be assigned")

CheckVar1 = IntVar()
C1 = Checkbutton(app, text = "Enable key logging", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20, command=chgcfg)

C1.pack()

img_path = "%s/img/logo.png"%rootdir
img = ImageTk.PhotoImage(Image.open(img_path))
panel = Label(app, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#labelText = StringVar()
#labelText.set("Are you ready?")
#label1 = Label(app, textvariable=labelText, height=4)
#label1.pack()

#checkBoxVal = IntVar()
#checkBox1 = Checkbutton(app, variable=checkBoxVal, text="Happy?")
#checkBox1.pack()

#custName = StringVar(None)
#yourName = Entry(app, textvariable=custName)
#yourName.pack()

button1 = Button(app, text="START", width=20, command=changeConfig)
button1.pack(side='bottom',padx=10,pady=10)

app.mainloop()

#c:/Python27/python.exe c:/Users/Amar/Documents/volume+/VOLUME+-.py

# C:\Program Files (x86)\Webteh\BSPlayer\bsplayer.exe


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
        print "Volume UP key:", config.get("main", "volume-up-key").upper()
        print "Volume DOWN key:", config.get("main", "volume-down-key").upper()
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
    if event.Key == config.get("main", "volume-up-key").upper():
       #if event.WindowName.startswith(input1):
       #   if input1 in open("%s/config.cfg"%os.path.abspath(os.path.dirname(__file__))).read():
       #      set_master_volume(get_master_volume() + 1)
       #      print "New volume:", get_master_volume()
       win32api.keybd_event(0xAF,0,1,0) #0xAF is volume UP
       print("VOLUME +++++")
    elif event.Key == config.get("main", "volume-down-key").upper():
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
   