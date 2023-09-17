from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/ping',methods=['GET','POST'])
def ping():
    return jsonify(success=True)

@app.route('/',methods=['GET','POST'])
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=5001)