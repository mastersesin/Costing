from flask import request, jsonify, Blueprint
from AppFolder.Views.Landing import landing
from AppFolder.Views.ProductSetting import product
from AppFolder.SqlClasses.models import *
from AppFolder import session
from AppFolder.AppMessages.appmessage import ReturnMSG
from AppFolder.Views.Caculator.Stone import stone
from AppFolder.Views.Caculator.Finding import finding
from AppFolder.Views.Caculator.Metal import metal
from AppFolder.Views.Caculator.IndirectLaborCost import cnc, lacquering, plating

# from mainAppFolder.crmapi import testProject3
costing = Blueprint('costing', __name__)


@costing.route('/', methods=['GET'])
def index():
    return jsonify(landing.view())


@costing.route('/productsetting', methods=['GET'])
def get_product():
    return jsonify(product.view())


@costing.route('/calculator/<calculate_what>', methods=['GET', 'POST'])
def calculator_detail(calculate_what=None):
    if request.method == 'GET' and calculate_what == 'stone':
        msg = ReturnMSG().doc
        require_params = finding.view.__code__.co_varnames[:stone.view.__code__.co_argcount]
        msg['msg'] = [x for x in require_params]
        return jsonify(msg)
    elif request.method == 'GET' and calculate_what == 'finding':
        msg = ReturnMSG().doc
        require_params = finding.view.__code__.co_varnames[:finding.view.__code__.co_argcount]
        msg['msg'] = [x for x in require_params]
        return jsonify(msg)
    elif request.method == 'POST' and calculate_what == 'stone' and request.is_json:
        stone_name = request.json.get('stone_name', None)
        stone_amount_of_unit_of_measure = request.json.get('stone_amount_of_unit_of_measure', None)
        setting_type_string = request.json.get('setting_type_string', None)
        stone_quantity = request.json.get('stone_quantity', None)
        material = request.json.get('material_string', None)
        if stone_name and stone_amount_of_unit_of_measure and setting_type_string and stone_quantity and material:
            msg = ReturnMSG().stonecost
            msg['msg'] = stone.view(
                stone_name,
                float(stone_amount_of_unit_of_measure),
                int(stone_quantity),
                setting_type_string,
                material
            )
            return jsonify(msg)
        else:
            return 'Something wrong'
    elif request.method == 'POST' and calculate_what == 'finding' and request.is_json:
        finding_name = request.json.get('finding_name', None)
        finding_amount_of_unit_of_measure = request.json.get('finding_amount_of_unit_of_measure', None)
        finding_quantity = request.json.get('finding_quantity', None)
        if finding_name and finding_amount_of_unit_of_measure and finding_quantity:
            msg = ReturnMSG().stonecost
            msg['msg'] = finding.view(finding_name, float(finding_amount_of_unit_of_measure), int(finding_quantity))
            return jsonify(msg)
        else:
            return 'Something wrong'
    elif request.method == 'POST' and calculate_what == 'metal' and request.is_json:
        alloy_name = request.json.get('alloy_name', None)
        alloy_amount_of_unit_of_measure = request.json.get('alloy_amount_of_unit_of_measure', None)
        alloy_quantity = request.json.get('alloy_quantity', None)
        product_type = request.json.get('product_type', None)
        difficulty_type = request.json.get('difficulty_type', None)
        finish_color = request.json.get('finish_color', None)
        if alloy_name and alloy_amount_of_unit_of_measure and alloy_quantity and product_type \
                and difficulty_type and finish_color:
            msg = ReturnMSG().stonecost
            msg['msg'] = metal.view(
                alloy_name=alloy_name,
                alloy_amount_of_unit_of_measure=float(alloy_amount_of_unit_of_measure),
                alloy_quantity=int(alloy_quantity),
                product_type=product_type,
                difficulty_type=difficulty_type,
                finish_color=finish_color
            )
            return jsonify(msg)
    elif request.method == 'POST' and calculate_what == 'cnc' and request.is_json:
        cnc_size = request.json.get('cnc_size', None)
        cnc_type = request.json.get('cnc_type', None)
        if cnc_size and cnc_type:
            msg = ReturnMSG().stonecost
            msg['msg'] = cnc.view(cnc_size=cnc_size, cnc_type=cnc_type)
            return jsonify(msg)
        else:
            return 'Something wrong'
    elif request.method == 'POST' and calculate_what == 'lacquering' and request.is_json:
        lacquering_type = request.json.get('lacquering_type', None)
        if lacquering_type:
            msg = ReturnMSG().stonecost
            msg['msg'] = lacquering.view(lacquering_type=lacquering_type)
            return jsonify(msg)
        else:
            return 'Something wrong'
    elif request.method == 'POST' and calculate_what == 'plating' and request.is_json:
        plating_type = request.json.get('plating_type', None)
        product_type = request.json.get('product_type', None)
        difficulty_type = request.json.get('difficulty_type', None)
        if plating_type:
            msg = ReturnMSG().stonecost
            msg['msg'] = plating.view(plating_type_string=plating_type,
                                      product_type_string=product_type,
                                      difficulty_type_string=difficulty_type)
            return jsonify(msg)
        else:
            return 'Something wrong'
    else:
        return 'METHOD ERR'

# @costing.route('/calculator', methods=['POST'])
# def calculator():
#     if request.method == 'POST' and request.is_json:
#         # Finding Cost
