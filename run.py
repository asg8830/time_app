from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_current_time():
    # Get the current time in the USA Eastern Daylight Time (EDT) timezone
    edt_timezone = pytz.timezone('US/Eastern')
    current_time = datetime.now(edt_timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    # Debug statement to print the current time to the console
    print(f"Current time (USA EDT): {current_time}")
    
    return f"Current time (USA EDT): {current_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
