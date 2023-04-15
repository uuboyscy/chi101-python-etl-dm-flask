from flask import Flask, request

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

"""
[GET] /get_names/department_id:string/team_id:int
Response:
    [
        {
            "emp_name": "Allen",
            "emp_id": 13
        },
        {
            "emp_name": "Ted",
            "emp_id": 44
        }, ...
    ]
"""
@app.route("/get_names/<string:department_id>/<int:team_id>")
def get_names(department_id: str, team_id: int) -> str:
    sql = """
        SELECT emp_name, emp_id FROM emp
        WHERE department_id = '{}'
        AND team_id = {};
    """.format(department_id, team_id)
    return sql


# /hello_get?name=Allen&age=22
@app.route("/hello_get")
def hello_get():
    name = request.args.get("name")
    age = request.args.get("age")

    if name is None:
        output_html = "<h1>What's your name?</h1>"
    elif age is None:
        output_html = "<h1>Hello {}.</h1>".format(name)
    else:
        output_html = "<h1>Hello {}, you are {} years old.</h1>".format(name, age)

    return output_html


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
