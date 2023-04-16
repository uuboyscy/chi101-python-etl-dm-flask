from flask import Blueprint

test_controller = Blueprint(
    "test_controller",
    __name__,
)


@test_controller.route("/test_ctrl")
def test_ctrl():
    return "12312321321"
