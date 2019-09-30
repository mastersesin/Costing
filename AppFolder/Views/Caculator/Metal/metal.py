from AppFolder.UsefulTools import getattributeid, getlaborcost, getstandardweight, getprice


def view(product_type: str, difficulty_type: str, finish_color: str,
         alloy_name: str, alloy_amount_of_unit_of_measure: float, alloy_quantity: int):
    def get_x_coordinate(product_type_id_f, difficulty_type_id_f):
        x_coordinate_without_difficulty_type_id = product_type_id_f * 1000
        x_coordinate_f = x_coordinate_without_difficulty_type_id + difficulty_type_id_f
        return x_coordinate_f

    # Metal Cost
    lost_rate = 1.05  # 5%
    component_weight_in_gram = alloy_amount_of_unit_of_measure
    single_component_cost = component_weight_in_gram * lost_rate * getprice.get_price(alloy_name)
    total_casting_cost = single_component_cost * alloy_quantity
    # Metal labor cost
    product_type_id = getattributeid.convert_attribute_name_to_attribute_id('product_type', product_type)
    difficulty_type_id = getattributeid.convert_attribute_name_to_attribute_id('difficulty_type', difficulty_type)
    finish_color_id = getattributeid.convert_attribute_name_to_attribute_id('finish_color', finish_color)
    x_coordinate = get_x_coordinate(product_type_id_f=product_type_id, difficulty_type_id_f=difficulty_type_id)
    y_coordinate = finish_color_id
    casting_labor_cost = getlaborcost.get_labor_cost(x=x_coordinate, y=y_coordinate)
    print(casting_labor_cost)
    return {
        "casting_labor_cost": casting_labor_cost,
        "casting_cost": total_casting_cost
    }


# EXAMPLE
print(view(product_type='Ring', difficulty_type='Simple', finish_color='Yellow',
           alloy_name='CASTING585Y', alloy_amount_of_unit_of_measure=0.9, alloy_quantity=1))
