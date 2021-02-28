from flask import Flask, request

from apps.api.controllers.course_get_controller import CourseGetController
from apps.api.controllers.course_post_controller import CoursePostController

app = Flask(__name__)

course_get_controller = CourseGetController()
course_post_controller = CoursePostController()


@app.route('/courses/<string:course_id>', methods=['GET'])
def get_course(course_id):
    return course_get_controller(course_id=course_id)


@app.route('/courses', methods=['POST'])
def create_course():
    return course_post_controller(request.body)


@app.errorhandler(ValueError)
def handle_value_error(error: ValueError):
    return str(error), 400
