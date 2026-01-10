from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    return 'If You Are Reading This you are going to hell with me :('

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)