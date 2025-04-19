from flask import Flask, render_template, request
from tip_generator import generate_tips

app = Flask(__name__)
app.debug = True  # Enable debug mode

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Route / accessed")  # Debug print
    if request.method == 'POST':
        print("POST request received")  # Debug print
        location = request.form['location']
        preferences = {
            'tripod': 'tripod' in request.form,
            'filters': 'filters' in request.form
        }
        tips = generate_tips(location, preferences)
        return render_template('results.html', tips=tips, location=location)
    return render_template('index.html')

@app.route('/test')
def test():
    return "Flask is working!"

if __name__ == '__main__':
    print("Starting Flask server...")  # Debug print
    app.run(host='0.0.0.0', port=5001)  # Explicit host/port