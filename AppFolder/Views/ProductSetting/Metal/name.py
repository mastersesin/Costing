from AppFolder import session
from AppFolder.SqlClasses.models import *
from sqlalchemy import and_


def view():
    return_data = {}
    query_record = session.query(ComponentPrice) \
        .filter(ComponentPrice.type_id >= 75, ComponentPrice.type_id < 77) \
        .limit(100)\
        .all()
    return_data['alloy_name'] = [record.component_product_name for record in query_record]
    return return_data
