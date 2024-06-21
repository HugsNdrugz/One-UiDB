from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  """Render the launcher application homepage"""
  # Replace with your actual data for apps
  apps = [
      {"name": "SMS", "icon": "message"},
      {"name": "Contacts", "icon": "account_box"},
      {"name": "Calendar", "icon": "date_range"},
      # Add more apps here
  ]
  return render_template('index.html', apps=apps)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
