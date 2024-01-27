from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/hello')
def Hello():
    return 'Hello Manuchexra'


@app.route('/Manuchehra')
def get_all_brands():
    return "My full name is Manuchexra Nurmexrojova.\nI am 17 years old.I am a student.\nMy future dream is to become a programmer. "



if __name__ == '__main__':
    app.run(debug=True)