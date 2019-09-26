from AppFolder import session
from AppFolder.SqlClasses.models import *

query_string_product = ['difficulty_type', 'product_type', 'design_type',
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
    return return_data
