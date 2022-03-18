# The purpose of this file is to hold sensitive information that you don't want to 
# post publicly to GitHub.  This file is excluded from being sent to github by .gitignore

def getSecrets():
    secrets = {
        'MAIL_PASSWORD':'<password_to_gmail_account>',
        'MAIL_USERNAME':'<gmail_address>',
        'MONGO_HOST':'mongodb+srv://sasukek:00343268@cluster0.oizni.mongodb.net/capstone?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'sasukek'
        }
    return secrets