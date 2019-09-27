from AppFolder import session
from AppFolder.SqlClasses.models import *


def get_labor_cost(x, y):
    query_record = session.query(CostAttributeValues) \
        .filter(CostAttributeValues.x_attribute_id == x) \
        .filter(CostAttributeValues.y_attribute_id == y) \
        .first()
    if query_record:
        return float(query_record.attribute_value)
    else:
        return False
