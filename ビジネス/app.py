from flask import Flask, render_template, request, logging, Response, redirect, flash
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')




@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run()
 
