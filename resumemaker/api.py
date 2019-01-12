from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route('make-resume', methods=['POST'])
def make_resume():
    ...
