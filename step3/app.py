from flask import Flask
import requests
import linecache


app = Flask(__name__)

get_api_from_configmap = linecache.getline('deployment.yaml', 46)


@app.route('/')
def hello_world():
    api = get_api_from_configmap.split('"')[1] if get_api_from_configmap.split('"')[1] != "" else 'http://worldtimeapi.org/api/timezone/Asia/Tehran'
    res = requests.get(api)
    return {
        'hostname': 'amiroo@Raei',
        "time": res.json()
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

# ubuntu-5895b8b77-dzh94