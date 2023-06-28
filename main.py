from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Firwall'
     
  },
 {
    'id':2,
    'title':'stop'
     
  },
   {
    'id':3,
    'title':'share'
     
  },
  

]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS) #passing home.html here 

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  #second url addese
  


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
