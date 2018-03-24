# OSL_KeyLogger_Windows
A Keylogger written in Python that takes in user input, stores the data log, and then sends it to an email address. The data log is destroyed after the email is sent to remain anonymous.

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
 	<li>now we want to install the pyHook module from this library with pip, (my path is the following, change the path to wherever you have stored the .whl module):
py -3.6 -m pip install C:\Users\YourPath\pywin32-223-cp36-cp36m-win32.whl</li>
 	<li>now we want to install the pyWin32 module from this library with pip, (my path is the following, change the path to wherever you have stored the .whl module):
py -3.6 -m pip install C:\Users\YourPath\pywin32-223-cp36-cp36m-win32.whl</li>
</ul>
&nbsp;

<img src="https://offseclab.com/wp-content/uploads/2018/03/installinglibraries.png" />
