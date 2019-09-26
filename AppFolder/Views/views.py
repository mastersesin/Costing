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
    elif request.method == 'POST' and calculate_what == 'stone' and request.is_json:
        stone_name = request.json.get('stone_name', None)
        stone_amount_of_unit_of_measure = request.json.get('stone_amount_of_unit_of_measure', None)
        setting_type_string = request.json.get('setting_type_string', None)
        stone_quantity = request.json.get('stone_quantity', None)
        if stone_name and stone_amount_of_unit_of_measure and setting_type_string and stone_quantity:
            msg = ReturnMSG().stonecost
            msg['msg'] = stone.view(stone_name, float(stone_amount_of_unit_of_measure), float(stone_quantity), setting_type_string)
            return jsonify(msg)
        else:
            return 'Something wrong'
    else:
        return 'METHOD ERR'
