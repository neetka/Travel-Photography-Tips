# Travel Photography Tips Chatbot

This project is a Flask-based web application that offers photography ideas and tips through a chatbot interface.

## Features

- Interactive chatbot providing photography suggestions
- User authentication and session management
- Integration with external APIs for dynamic content

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/neetka/Travel-Photography-Tips.git
   
2.  **Navigate to the project directory:**
    
    bash
    
    CopyEdit
    
    `cd Travel-Photography-Tips` 
    
3.  **Create a virtual environment:**
    
    bash
    
    CopyEdit
    
    `python3 -m venv venv` 
    
4.  **Activate the virtual environment:**
    
    -   On macOS/Linux:
        
        bash
        
        CopyEdit
        
        `source venv/bin/activate` 
        
    -   On Windows:
        
        bash
        
        CopyEdit
        
        `venv\Scripts\activate` 
        
5.  **Install the required dependencies:**
    
    bash
    
    CopyEdit
    
    `pip install -r requirements.txt` 
    

## Usage

### Set environment variables

bash

CopyEdit

`export FLASK_APP=app.py export FLASK_ENV=development` 

> For Windows (Command Prompt):

cmd

CopyEdit

`set FLASK_APP=app.py
set FLASK_ENV=development` 

### Initialize the database

bash

CopyEdit

`flask db init
flask db migrate -m "Initial migration." flask db upgrade` 

### Run the application

bash

CopyEdit

`flask run` 

Then open your browser and navigate to:  
[http://127.0.0.1:5001](http://127.0.0.1:5001)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.