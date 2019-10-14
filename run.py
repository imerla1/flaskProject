from flaskapp import app
import logging
import os


if __name__ == '__main__':
    
    app.run(debug=True, host='192.168.3.22')