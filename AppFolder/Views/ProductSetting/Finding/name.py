from AppFolder import session
from AppFolder.SqlClasses.models import *


def view():
    return_data = {}
    query_record = session.query(ComponentPrice) \
        .filter(ComponentPrice.type_id == 79).limit(100).all()
    return_data['finding_name'] = [record.component_product_name for record in query_record]
    return return_data
