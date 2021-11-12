from flask import Flask
import requests
import requests
import json


app = Flask(__name__)


file = open('config.json')
config_data = json.load(file)
address = config_data['bind']['address']
port = config_data['bind']['port']
api_url = config_data['api']['url']


@app.route('/')
def hello_world():
    api = api_url if api_url != '' else 'http://worldtimeapi.org/api/timezone/Asia/Tehran'
    res = requests.get(api)
    return {
        'hostname': 'amiroo@Raei',
        "time": res.json()
    }

if __name__ == '__main__':
    app.run(host=address, port=port, debug=True)