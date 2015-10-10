__author__ = 'Antonio Locandro'

from flask import Flask
app = Flask (__name__)

@app.route("/")

def main():
    return "Antonio Locandro! Test Page"

if __name__ == "__main__":
    app.run()


