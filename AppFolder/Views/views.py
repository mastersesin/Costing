from flask import request, jsonify, Blueprint
from AppFolder.Views.Landing import landing
from AppFolder.Views.Product import product
from AppFolder.SqlClasses.models import *
from AppFolder import session
from AppFolder.AppMessages.appmessage import ReturnMSG
from AppFolder.Views.Caculator.Stone import stone

# from mainAppFolder.crmapi import testProject3
costing = Blueprint('costing', __name__)


@costing.route('/', methods=['GET'])
def index():
    return jsonify(landing.view())


@costing.route('/productsetting', methods=['GET'])
def get_product():
    return jsonify(product.view())


@costing.route('/calculator/<calculate_what>', methods=['GET', 'POST'])
def calculator(calculate_what=None):
    if request.method == 'GET' and calculate_what == 'stone':
        msg = ReturnMSG().doc
        require_params = stone.view.__code__.co_varnames[:stone.view.__code__.co_argcount]
        msg['msg'] = [x for x in require_params]
        return jsonify(msg)
