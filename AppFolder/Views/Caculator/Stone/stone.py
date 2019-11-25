# Calculator for Stone Cost
from AppFolder import session
from AppFolder.SqlClasses.models import *
from AppFolder.UsefulTools import getprice, getstandardweight, getlaborcost
from AppFolder.UsefulTools import getattributeid


def view(stone_name: str, stone_quantity: int, setting_type_string: str, material_string: str):
    def convert_setting_type_string_to_setting_id():
        query_record = session.query(CostAttributes) \
            .filter(CostAttributes.attribute_name == 'setting_type') \
            .filter(CostAttributes.attribute_text == setting_type_string) \
            .first()
        if query_record:
            return int(query_record.attribute_id)
        else:
            return False

    def get_material_id_of_stone():
        query_record = session.query(ComponentPrice) \
            .filter(ComponentPrice.type_id == 77) \
            .filter(ComponentPrice.component_product_name == stone_name) \
            .first()
        if query_record:
            return int(query_record.material_id)
        else:
            return False

    if isinstance(getstandardweight.get_standard_weight(stone_name), float) \
            and isinstance(getprice.get_price(stone_name), float):
        stone_amount_of_unit_of_measure = 1
        # Stone Cost
        single_component_cost = stone_amount_of_unit_of_measure * getprice.get_price(stone_name)
        total_stone_cost = single_component_cost * stone_quantity
        # Stone Labor Cost
        total_stone_labor_cost = getlaborcost.get_labor_cost(
            convert_setting_type_string_to_setting_id(),
            getattributeid.convert_attribute_name_to_attribute_id(
                attribute_name='material',
                attribute_text=material_string
            )
        )
        final_stone_cost = total_stone_cost + total_stone_labor_cost
        return {
            "final_stone_cost": final_stone_cost,
            "total_stone_cost": total_stone_cost,
            "total_stone_labor_cost": total_stone_labor_cost
        }


print(view("AMG_CSRC_8X8_B2", 1, "Pave", "Gold"))
