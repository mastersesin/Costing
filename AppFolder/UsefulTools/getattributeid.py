from AppFolder import session
from AppFolder.SqlClasses.models import *


def convert_attribute_name_to_attribute_id(attribute_name: str, attribute_description_text: str):
    query_record = session.query(CostAttributes) \
        .filter(CostAttributes.attribute_text == attribute_name) \
        .filter(CostAttributes.attribute_shrot_text == attribute_description_text) \
        .first()
    if query_record:
        return int(query_record.attribute_id)
    else:
        return False

# print(convert_attribute_name_to_attribute_id('difficulty_type', 'Very simple'))
