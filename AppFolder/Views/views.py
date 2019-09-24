from flask import request, jsonify, Blueprint

# from mainAppFolder.crmapi import testProject3
costing = Blueprint('costing', __name__)


@costing.route('/', methods=['GET'])
def index():
    return "<h1>D.I Limited Costing project</h1>"
