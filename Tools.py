import os
from subprocess import Popen
import time
import qrcode
from colorama import Fore as f 
from pyzbar.pyzbar import decode
from PIL import Image
import pyfiglet
import webbrowser as wb
import sys


def baner():
    if os.name == "nt":
        os.system("cls")
        print("")
        time.sleep(1)
        Popen('neofetch -c red -ac green')
        time.sleep(1)
    elif os.name =="posix":
        os.system("clear")
        print("")
        time.sleep(2)
        Popen("neofetch")
        
def Qrcode(): # Build QR code
    name_qr = input(f.YELLOW+'Please enter QRcode name :> ') # Choose a QR name
    name_pic = input(f.GREEN+'Please choose a name for the photo :> ') # Choose a name for the QR photo
    print(f.RED+'Please wait ! !')
    time.sleep(1)
    qr = qrcode.make(name_qr) # Build QR code
    qr.save(name_pic +'.png') # Creating a QR file
    print(f.BLUE+'Was made')

def decode_QR(): # QR code decoding
    picture_n = input(f.GREEN+'Please enter the QR code name :> ') # Enter the QR name
    picture = Image.open(picture_n + '.png')
    qr = decode(picture)
    text = qr[0].data.decode()
    print('Please wait')
    time.sleep(1.5)
    print(f.LIGHTRED_EX + 'Result :>> ' + text.format(text))


def text_edit():
    
    Name = str(input(f.LIGHTCYAN_EX+'Please enter a'+f.LIGHTRED_EX +' name'+f.RESET + ' or' + f.LIGHTYELLOW_EX + ' number: >>>>')).lower()
    print('red', 'green', 'yellow', 'blue', 'cyan',
          'magenta', 'black', 'white', '....')
    Color = input(f.LIGHTMAGENTA_EX+'What color do you want ? ? ?').lower()          
    figlet = pyfiglet.figlet_format(Name)
    print('Please wait')
    time.sleep(0.5)
    if Color == 'red':
            print(f.RED+figlet)
    elif Color == 'green':
            print(f.GREEN+figlet)
    elif Color == 'yellow':
            print(f.YELLOW+figlet)
    elif Color == 'blue':
            print(f.BLUE+figlet)
    elif Color == 'cyan':
            print(f.CYAN+figlet)
    elif Color == 'magenta':
            print(f.MAGENTA+figlet)
    elif Color == 'black':
            print(f.BLACK+figlet)
    elif Color == 'whait':
            print(f.WHITE+figlet)
    else: raise NameError(f.LIGHTWHITE_EX+'The color you selected is not in the specified colors')
    

def select():
        os.system('cls')
        baner()
        print('')
        print('')
        print('')
        print(f.BLUE+'Which do you want?')
        print(
        f.RED+'[1] Text editing\n',
        f.YELLOW+'[2] Build QR code\n ',
        f.RED+'[3] QR code decoding\n  ',
        f.YELLOW+'[4] About the programmer\n   ',
        f.RED+'[5] Exit'
        )
        sel = int(input(f.GREEN+' Please select an option <:<>:> '))
        if sel == 1:
                os.system('cls')
                baner()
                print('')
                print('')
                print('')
                text_edit()
        elif sel == 2:
                os.system('cls')
                baner()
                print('')
                print('')
                print('')
                Qrcode()
        elif sel == 3:
                os.system('cls')
                baner()
                print('')
                print('')
                print('')
                decode_QR()

        elif sel == 4:
                os.system('cls')
                baner()
                print('')
                print('')
                print('')
                print(f.LIGHTMAGENTA_EX + ' Please follow me for support \n Instagram :> kamy.py \n Github :> virtualtramp ' )
        # elif sel == 5:
        #         sys()
        


select()