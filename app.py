from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

@app.route('/')
def hello():
  return "bakayaroo"
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
