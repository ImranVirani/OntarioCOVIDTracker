# Ontario Covid Update
Sends an email and desktop notification(Mac OS only) when the Ontario,Canada Covid Numbers are updated.

# Usage
To run this application make sure to have the Chromium Web Driver installed in the default location, and install the dependencies of the project using the requirements.txt:

```
pip install -r requirements.txt
```
You will also need to setup the Sendgrid API, you will need the quickstart.py and credentials.json in the same folder as the project.

You will also need to set the environment variables ```TEST_EMAIL_SEND``` to the email that is setup with Sendgrid and ```TEST_EMAIL_REC``` to the email address you are sending to.
