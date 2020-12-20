# About

A Python 3 application that sends an email and desktop notification(Currently Mac OS only) when the Ontario, Canada Covid-19 numbers are updated.

If you would like to use a lighter version(which does not require the Web Driver, but uses the requests library instead) of the app, use the lightweight branch.



# Setup
To run this application make sure to have Google Chrome and the Chromium Web Driver(which can be found [here](https://chromedriver.chromium.org/downloads) for MacOS  and Windows, and if you are using GNU/Linux you will likely be able to obtain both Google Chrome and the Web Driver from your package manager. Make sure it is installed in the default location, or if you would like to install it in a different location please specify it , and install the dependencies of the project using the requirements.txt:

```
pip3 install -r requirements.txt
```
You will also need to setup the Sendgrid API, and follow the instructions on Sengrid to create a single sender. The quickstart method provided by Sendgrid is a great way to quickly setup the api with your email provider. A credentials.json will also likely be required in the same folder as the project.

You will also need to set the environment variables ```TEST_EMAIL_SEND``` to the email that is setup with Sendgrid, ```TEST_EMAIL_REC``` to the email address you are sending to and most importantly ```SENDGRID_API_KEY``` to the value of your API key as a string. Typically the file that contains these are the ```~/.bashrc``` or ```~/.zshrc``` if using a Unix-like operating system(eg. Mac or Linux). If you are not using bash or zsh, the file may be named differently or in a different file in the file system. Please consult the shell's resources(i.e wiki) for information on how to access these files. 

This can be done in Bash by running:
``` 
echo "export TEST_EMAIL_SEND='INSERT_SEND_EMAIL_HERE'" >> ~/.bashrc
echo "export TEST_EMAIL_REC='INSERT_RECEIVING_EMAIL_HERE'" >> ~/.bashrc
echo "export SENDGRID_API_KEY='INSERT_API_KEY_HERE'" >> ~/.bashrc
```
Replace ```~/.bashrc``` with ```~/.zshrc``` to use with ```zsh```

# Support
If there are any inquiries regarding the project(eg. setting up/running), please create an issue and I would be happy to help.
