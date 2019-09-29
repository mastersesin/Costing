from AppFolder import session
from AppFolder.SqlClasses.models import *


def view():
    return_data = {}
    query_record = session.query(CostAttributes) \
        .filter(CostAttributes.attribute_text == 'setting_type').limit(10).all()
    return_data['stonesettingtype'] = [record.attribute_shrot_text for record in query_record]
    return return_data


print(view())
