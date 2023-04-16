from flask import Flask, request, jsonify, render_template

import poker as p
import model
from test_controller import test_controller

app = Flask(__name__, static_url_path="/resource", static_folder="./my_resource")
app.register_blueprint(test_controller, url_prefix="/controller_A")


@app.route("/")
def hello_flask():
    return "<h1>Hello Flask!123123123123</h1>"


# @app.route("/greet/<name>")
# def greet(name):
#     return "Hello {}".format(name)


@app.route("/greet/<name>")
def greet(name):
    return render_template("hello.html", name=name)

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
# @app.route("/hello_get")
# def hello_get():
#     name = request.args.get("name")
#     age = request.args.get("age")
#
#     if name is None:
#         output_html = "<h1>What's your name?</h1>"
#     elif age is None:
#         output_html = "<h1>Hello {}.</h1>".format(name)
#     else:
#         output_html = "<h1>Hello {}, you are {} years old.</h1>".format(name, age)
#
#     return output_html

# /hello_get?name=Allen&age=22
@app.route("/hello_get")
def hello_get():
    name = request.args.get("name")
    age = request.args.get("age")

    return render_template(
        "hello_get.html",
        name=name,
        age=age,
    )


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    output_html = """
        <form action="/hello_post" method="POST">
            <label>What's your name?</label>
            <input name="username">
            <button type="submit">SUBMIT</button>
        </form>
    """

    request_method = request.method
    if request_method == "POST":
        username = request.form.get("username")
        output_html += "<h1>Hello {}.</h1>".format(username)

    return output_html


@app.route("/poker/<num>")
def poker(num):
    json_data = p.poker(int(num))

    return jsonify(json_data)


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
