from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'WELCOME TO JENKINS DEVOPS GITHOPS TEST ENVIRONMENT'
