from flask import render_template


username = "Allen"
repo_name = "TEST"

print(
    render_template("templates/notifacation.txt", username=username, repo_name=repo_name)
)
