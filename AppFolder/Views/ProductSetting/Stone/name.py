from AppFolder import session
from AppFolder.SqlClasses.models import *


def view():
    return_data = {}
    query_record = session.query(ComponentPrice) \
        .filter(ComponentPrice.type_id == 77).limit(100).all()
    return_data['stone_name'] = [record.component_product_name for record in query_record]
    return return_data


# print(view())