import json
from flask import Flask, render_template

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

# Load data from JSON file
try:
    with open('data/aggregated_data.json') as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "conversations": [],
        "call_logs": []
    }
    print("Warning: 'data/aggregated_data.json' not found. Using empty data.")

@app.route('/')
def index():
    """Render the home launcher page"""
    apps = [
        {"name": "Messenger", "icon": "Messenger.png", "route": "messenger"},
        {"name": "Call", "icon": "Phone.png", "route": "call"},
        {"name": "SMS", "icon": "Messages.png", "route": "sms"},
        {"name": "Keylogs", "icon": "Samsung Keyboard.png", "route": "keylogs"},
    ]
    return render_template('index.html', apps=apps)

@app.route('/app/<name>')
def app_details(name):
    """Render details for a specific app"""
    if name == "messenger":
        messages = data.get('conversations', [])
        return render_template('app_details.html', app_name="Messenger", data=messages)
    elif name == "call":
        calls = data.get('call_logs', [])
        return render_template('app_details.html', app_name="Call", data=calls)
    elif name == "sms":
        sms = data.get('sms', [])
        return render_template('app_details.html', app_name="SMS", data=sms)
    elif name == "keylogs":
        keylogs = data.get('keylogs', [])
        return render_template('app_details.html', app_name="Keylogs", data=keylogs)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')