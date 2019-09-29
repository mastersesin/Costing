from AppFolder.UsefulTools import getlaborcost, getprice, getstandardweight


def view(finding_name: str, finding_amount_of_unit_of_measure: float, finding_quantity: int):
    if isinstance(getstandardweight.get_standard_weight(finding_name), float) \
            and isinstance(getprice.get_price(finding_name), float):
        # Finding Cost
        component_weight_in_gram = getstandardweight.get_standard_weight(
            finding_name
        ) * finding_amount_of_unit_of_measure
        single_component_cost = component_weight_in_gram * getprice.get_price(finding_name)
        total_finding_cost = single_component_cost * finding_quantity
        # Finding Labor Cost
        total_finding_labor_cost = getlaborcost.get_labor_cost(
            '144',  # fixed x
            '144'  # fixed y
        )
        final_finding_cost = total_finding_cost + total_finding_labor_cost
        return {
            "final_finding_cost": final_finding_cost,
            "total_finding_cost": total_finding_cost,
            "total_finding_labor_cost": total_finding_labor_cost
        }


# print(view('AFCHgSERPD0.65_18K', 0.005, 1))
