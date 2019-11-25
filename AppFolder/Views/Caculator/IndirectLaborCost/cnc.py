from AppFolder.UsefulTools import getattributeid, getlaborcost


def view(cnc_size: str, cnc_type: str):
    cnc_size_id = getattributeid.convert_attribute_name_to_attribute_id(
        attribute_name='cnc_size',
        attribute_text=cnc_size
    )
    cnc_type_id = getattributeid.convert_attribute_name_to_attribute_id(
        attribute_name='cnc_type',
        attribute_text=cnc_type
    )
    x_coordinate = cnc_size_id
    y_coordinate = cnc_type_id
    cnc_labor_cost = getlaborcost.get_labor_cost(
        x=x_coordinate,
        y=y_coordinate
    )
    return {
        "cnc_labor_cost": cnc_labor_cost,
    }


# EXAMPLE
# print(view(cnc_size='Small', cnc_type='Gold simple'))
