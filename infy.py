from flask import Flask,render_template,request,redirect,session

app=Flask(__name__)

@app.route('/')
def homePage():
    return 'WELCOME TO INFY API SERVER'

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001)
