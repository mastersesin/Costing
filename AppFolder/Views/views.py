from flask import request, jsonify, Blueprint
from AppFolder.Views.Landing import landing
from AppFolder.Views.Product import product
from AppFolder.SqlClasses.models import *
from AppFolder import session

# from mainAppFolder.crmapi import testProject3
costing = Blueprint('costing', __name__)


@costing.route('/', methods=['GET'])
def index():
    return jsonify(landing.view())


@costing.route('/productsetting', methods=['GET'])
def get_product():
    return jsonify(product.view())
