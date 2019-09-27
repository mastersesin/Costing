from AppFolder import session
from AppFolder.SqlClasses.models import *


def get_price(component_name):
    # Get component price aka component price per UOM
    query_record = session.query(ComponentPrice) \
        .filter(ComponentPrice.component_product_name == component_name).first()
    if query_record:
        return float(query_record.component_price_per_uom)
    else:
        return False
