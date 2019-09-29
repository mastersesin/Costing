from AppFolder import session
from AppFolder.Views.ProductSetting.Stone import name as stonename
from AppFolder.Views.ProductSetting.Finding import name as findingname
from AppFolder.Views.ProductSetting.Metal import name as alloyname
from AppFolder.SqlClasses.models import *

query_string_product = ['difficulty_type', 'product_type', 'design_type', 'plating_type',
                        'brand', 'finish_color', 'lacquering_type', 'setting_type',
                        {'cnc': ['cnc_size', 'cnc_type']},
                        {'material': ['material', 'material_rate']}]


def view():
    return_data = {}
    for data in query_string_product:
        if isinstance(data, dict):
            for key, value in data.items():
                for query_string in value:
                    query_record = session.query(CostAttributes) \
                        .filter(CostAttributes.attribute_text == query_string).all()
                    # Create return scaffold
                    try:
                        return_data[key].update({query_string: []})
                    except KeyError:  # Not yet have so we have to create it
                        return_data[key] = ({query_string: []})
                    for attribute in query_record:
                        return_data[key][query_string].append(attribute.attribute_shrot_text)
        else:
            query_record = session.query(CostAttributes) \
                .filter(CostAttributes.attribute_text == data).all()
            for attribute in query_record:
                try:
                    return_data[data].append(attribute.attribute_shrot_text)
                except KeyError:
                    return_data[data] = []
                    return_data[data].append(attribute.attribute_shrot_text)
    stone_name = stonename.view()
    finding_name = findingname.view()
    alloy_name = alloyname.view()
    return_data['stone_name'] = stone_name['stone_name']
    return_data['finding_name'] = finding_name['finding_name']
    return_data['alloy_name'] = alloy_name['alloy_name']
    return return_data
