from AppFolder import session
from AppFolder.SqlClasses.models import *


def view():
    return_data = {}
    query_record = session.query(ComponentPrice) \
        .filter(ComponentPrice.type_id == (79 or 93)).limit(10).all()
    return_data['stones'] = [record.component_product_name for record in query_record]
    return return_data

