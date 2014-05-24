from flask import Flask, render_template, request, url_for
import commands

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/', methods=['POST'])
def cheeseFries():
  command=request.form['cheeseFries']
  output=commands.getoutput(command)
  return render_template('home.html', allCarbDiet=output)
if __name__ == '__main__':
  app.run(debug=True)
