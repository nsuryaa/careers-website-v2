from flask import Flask,render_template,jsonify
from database import load_jobs_from_db

#Creating object of class
app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru,India',
#         'salary': 'Rs. 1,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Scientist',
#         'location': 'Delhi,India',
#         'salary': 'Rs. 15,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Frontend Engineer',
#         'location': 'Remote',
#     },
#     {
#         'id': 4,
#         'title': 'Backend Engineer',
#         'location': 'San Francisco, USA',
#         'salary': '$150,000'
#     }
# ]


#Creating a route
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html',jobs=jobs,company_name = 'myStartup')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)