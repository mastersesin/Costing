# Calculator for Stone Cost
from AppFolder import session
from AppFolder.SqlClasses.models import *


def view(stone_name: str, stone_amount_of_unit_of_measure: float, stone_quantity: int, setting_type_string: str):
    def get_standard_weight():
        query_record = session.query(ComponentPrice) \
            .filter(ComponentPrice.component_product_name == stone_name).first()
        if query_record:
            return float(query_record.standard_weight)
        else:
            return False

    def get_component_price():
        query_record = session.query(ComponentPrice) \
            .filter(ComponentPrice.component_product_name == stone_name).first()
        if query_record:
            return float(query_record.component_price_per_uom)
        else:
            return False

    def convert_setting_type_string_to_setting_id():
        query_record = session.query(CostAttributes) \
            .filter(CostAttributes.attribute_text == 'setting_type') \
            .filter(CostAttributes.attribute_shrot_text == setting_type_string) \
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

    def get_stone_labor_cost(x, y):
        query_record = session.query(CostAttributeValues) \
            .filter(CostAttributeValues.x_attribute_id == x) \
            .filter(CostAttributeValues.y_attribute_id == y) \
            .first()
        if query_record:
            return float(query_record.attribute_value)
        else:
            return False

    if isinstance(get_standard_weight(), float) and isinstance(get_component_price(), float):
        # Stone Cost
        component_weight_in_gram = get_standard_weight() * stone_amount_of_unit_of_measure
        single_component_cost = component_weight_in_gram * get_component_price()
        total_stone_cost = single_component_cost * stone_quantity
        # Stone Labor Cost
        total_stone_labor_cost = get_stone_labor_cost(
            convert_setting_type_string_to_setting_id(),
            get_material_id_of_stone()
        )
        final_stone_cost = total_stone_cost + total_stone_labor_cost
        return {
            "final_stone_cost": final_stone_cost,
            "total_stone_cost": total_stone_cost,
            "total_stone_labor_cost": total_stone_labor_cost
        }


# view("AGB_FL-082B-856089_9.0H3.0_C2", 1, 1, "Prong / Bezel /Nick / Pressure Hand Set")
