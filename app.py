from flask import Flask, render_template

app = Flask(__name__)

JOBS= [
{
  'id' : 1,
  'title' : 'full stack devloper',
  'location' : 'New York',
  'salary' : '100000'
},
  {
    'id' : 2,
    'title' : 'web devloper',
    'location' : 'casablanca',
    'salary' : '200000'
  }
  ]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
