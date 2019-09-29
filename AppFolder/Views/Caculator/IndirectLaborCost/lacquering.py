from AppFolder.UsefulTools import getattributeid, getlaborcost


def view(lacquering_type: str):
    lacquering_id = getattributeid.convert_attribute_name_to_attribute_id('lacquering_type', lacquering_type)
    x = lacquering_id
    y = lacquering_id
    lacquering_labor_cost = getlaborcost.get_labor_cost(x, y)
    return {
        "lacquering_labor_cost": lacquering_labor_cost,
    }

# EXAMPLE
# print(view('Lacquering  - complicated & repoli'))
