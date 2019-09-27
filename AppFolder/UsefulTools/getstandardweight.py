from AppFolder import session
from AppFolder.SqlClasses.models import *


def get_standard_weight(component_name):
    # Get standard weight of component ( 4.442 g/m for example )
    query_record = session.query(ComponentPrice) \
        .filter(ComponentPrice.component_product_name == component_name).first()
    if query_record:
        return float(query_record.standard_weight)
    else:
        return False
