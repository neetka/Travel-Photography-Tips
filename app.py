# app.py
from flask import Flask, render_template, request
from tip_generator import generate_tips

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        preferences = {
            'tripod': 'tripod' in request.form,
            'filters': 'filters' in request.form
        }
        
        tips = generate_tips(location, preferences)
        return render_template('results.html', tips=tips, location=location)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)