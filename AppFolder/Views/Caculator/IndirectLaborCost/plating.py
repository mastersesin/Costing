from AppFolder.UsefulTools import getattributeid, getlaborcost


def view(product_type_string: str, difficulty_type_string: str, plating_type_string: str):
    def get_x_coordinate(product_type_id_f, difficulty_type_id_f):
        x_coordinate_without_difficulty_type_id = product_type_id_f * 1000
        x_coordinate_f = x_coordinate_without_difficulty_type_id + difficulty_type_id_f
        return x_coordinate_f

    product_type_id = getattributeid.convert_attribute_name_to_attribute_id(
        attribute_name='product_type',
        attribute_description_text=product_type_string
    )
    difficulty_type_id = getattributeid.convert_attribute_name_to_attribute_id(
        attribute_name='difficulty_type',
        attribute_description_text=difficulty_type_string
    )
    plating_type_id = getattributeid.convert_attribute_name_to_attribute_id(
        attribute_name='plating_type',
        attribute_description_text=plating_type_string
    )
    x_coordinate = get_x_coordinate(product_type_id_f=product_type_id, difficulty_type_id_f=difficulty_type_id)
    y_coordinate = plating_type_id
    plating_labor_cost = getlaborcost.get_labor_cost(
        x=x_coordinate,
        y=y_coordinate
    )
    return {
        "plating_labor_cost": plating_labor_cost,
    }


# EXAMPLE
print(view(product_type_string='Necklace', difficulty_type_string='Simple', plating_type_string='AG10'))
