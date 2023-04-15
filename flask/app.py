from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<h1>Hello Flask!123123123123</h1>"


@app.route("/greet/<name>")
def greet(name):
    return "Hello {}".format(name)


@app.route("/two_sum/<x>/<y>")
def two_sum(x, y):
    return str(int(x) + int(y))

# [GET] /get_names/department_id:string/team_id:string
@app.route("/get_names/<department_id>/<team_id>")
def get_names(department_id, team_id):
    sql = """
        SELECT emp_name, emp_id FROM emp
        WHERE department_id = '{}'
        AND team_id = {};
    """.format(department_id, team_id)
    return sql


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
