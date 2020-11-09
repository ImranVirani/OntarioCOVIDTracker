# Ontario Covid Update
Sends an email and desktop notification(Mac OS only) when the Ontario, Canada Covid Numbers are updated.

# Setup
To run this application make sure to have the Chromium Web Driver installed in the default location, and install the dependencies of the project using the requirements.txt:

```
pip3 install -r requirements.txt
```
You will also need to setup the Sendgrid API, and follow the instructions on Sengrid to create a single sender, the quickstart method is a great way to quickly setup the api with your email provider, a credentials.json will likely be required in the same folder as the project.

You will also need to set the environment variables ```TEST_EMAIL_SEND``` to the email that is setup with Sendgrid and ```TEST_EMAIL_REC``` to the email address you are sending to. Typically this file is the ```~/.bashrc``` or ```~/.zshrc``` if using a Unix-like operating system(eg. Mac or Linux). If you are not using bash or zsh, the file may be named differently or in a different file in the file system. Please consult the shell's resources(i.e wiki) for information on how to access these files.

If there are any inquiries regarding the project, please create an issue and I would be happy to help.
