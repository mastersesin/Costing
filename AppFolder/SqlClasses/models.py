from AppFolder import Base
from AppFolder.UsefulTools import timestamp
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, REAL, Numeric, DateTime
from datetime import datetime

class ProductCost(Base):
    __tablename__ = 'ProductCost'
    cost_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    cost_product_code = Column(Integer, nullable=False)
    cost_version = Column(Integer, nullable=False, default=1)
    cost_status = Column(Integer, nullable=False, default=10)
    expiration_date = Column(Integer, nullable=False, default=timestamp.current_time_stamp() + 31536000)
    material_id = Column(Integer, nullable=False)
    material_rate = Column(Integer, nullable=False)
    product_type_id = Column(Integer, nullable=False)
    difficulty_type_id = Column(Integer, nullable=False)
    design_type_id = Column(Integer, nullable=False)
    finishing_color_id = Column(Integer, default=None)
    lacquering_type_id = Column(Integer, default=None)
    product_id = Column(Integer, default=None)
    product_name = Column(String, default=None)
    drawing_number = Column(String, default=None)
    brand_id = Column(Integer, default=None)
    customer_id = Column(Integer, default=None)
    description = Column(String, default=None)
    currency = Column(String, nullable=False, default='USD')
    usd_exchange_rate = Column(Numeric(8, 2), nullable=False, default=1)
    user_material_base_price_per_uom = Column(Numeric(8, 2), nullable=False, default=0)
    material_base_unit_of_measure = Column(String, nullable=False, default='USD/kg')
    loss_rate = Column(Numeric(8, 3), nullable=False, default=1)
    weight_conversion_rate = Column(Numeric(8, 3), nullable=False, default=1)
    fp_total_cost = Column(Numeric(8, 3), nullable=False, default=0)
    fp_metal_cost = Column(Numeric(8, 3), nullable=False, default=0)
    metal_casting_cost = Column(Numeric(8, 3), nullable=False, default=0)
    metal_finding_cost = Column(Numeric(8, 3), nullable=False, default=0)
    fp_finding_cost = Column(Numeric(8, 3), nullable=False, default=0)
    fp_stones_cost = Column(Numeric(8, 3), nullable=False, default=0)
    fp_labor_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_casting_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_casting_extra_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_casting_extra_quantity = Column(Numeric(8, 3), nullable=False, default=0)
    labor_plating_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_lacquer_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_setting_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_purchased_findings_cost = Column(Numeric(8, 3), nullable=False, default=0)
    labor_cnc_cost = Column(Numeric(8, 3), nullable=False, default=0)
    cnc_type = Column(Integer, default=None)
    cnc_size = Column(Integer, default=None)

    def __repr__(self):
        return '<Cost ID: %d>' % self.cost_id

    class ProductCostComponent(Base):
        __tablename__ = 'ProductCostComponent'
        cost_line_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
        cost_id = Column(Integer, nullable=False)
        component_id = Column(Integer, nullable=False)
        component_size = Column(String, default=None)
        type_id = Column(Integer, nullable=False)
        subtype_id = Column(String, default=None)
        sourcing_type_id = Column(Integer, nullable=False, default=0)
        material_id = Column(Integer, nullable=False, default=0)
        material_rate = Column(Integer, nullable=False, default=1)
        material_price_per_uom = Column(Numeric(8, 3), nullable=False, default=0)
        operation_type_id = Column(Integer, nullable=False, default=0)
        quantity_component_quantity = Column(Numeric(8, 3), nullable=False, default=0)
        quantity_unit_of_measure = Column(String, nullable=False, default='pc')
        component_price_per_uom = Column(Numeric(8, 3), nullable=False, default=0)
        component_price = Column(Numeric(8, 3), nullable=False, default=0)
        currency = Column(String, nullable=False, default='USD')
        usd_exchange_rate = Column(Numeric(8, 3), nullable=False, default=1)
        standard_weight = Column(Numeric(8, 3), nullable=False, default=0)
        standard_metal_weight = Column(Numeric(8, 3), nullable=False, default=0)
        weight_unit_of_measure = Column(String, nullable=False, default='g')
        create_by = Column(String, nullable=False)
        create_on = Column(Integer, nullable=False, default=timestamp.current_time_stamp())
        update_by = Column(String, default=None)
        update_on = Column(Integer, default=0)

    def __repr__(self):
        return '<Cost line id: %d>' % self.cost_line_id

    class ComponentPrice(Base):
        __tablename__ = 'ComponentPrice'
        component_id = Column(Integer, primary_key=True, nullable=False)
        component_status = Column(Integer, nullable=False, default=10)
        component_product_id = Column(String, default=None)
        component_product_name = Column(String, default=None)
        component_product_description = Column(String, default=None)
        component_size = Column(String, default=None)
        type_id = Column(Integer, nullable=False)
        subtype_id = Column(String, default=None)
        sourcing_type_id = Column(Integer, nullable=False, default=0)
        quantity_unit_of_measure = Column(String, nullable=False, default='pc')
        material_id = Column(Integer, nullable=False, default=0)
        material_rate = Column(Integer, nullable=False, default=1)
        material_price_per_uom = Column(Numeric(8, 3), nullable=False, default=0)
        component_price_per_uom = Column(Numeric(8, 3), nullable=False, default=0)
        currency = Column(String, nullable=False, default='USD')
        standard_weight = Column(Numeric(8, 3), nullable=False, default=0)
        standard_metal_weight = Column(Numeric(8, 3), nullable=False, default=0)
        weight_unit_of_measure = Column(String, nullable=False, default='g')
        component_sort_id = Column(Integer, nullable=False, default=0)
        create_by = Column(String, nullable=False)
        create_on = Column(DateTime, default=datetime.utcnow)#Column(Integer, nullable=False, default=timestamp.current_time_stamp())
        update_by = Column(String, default=None)
        update_on = Column(DateTime, default=datetime.utcnow)

        def __repr__(self):
            return '<Component id: %d>' % self.component_id

    class CostAttributes(Base):
        __tablename__ = 'CostAttributes'
        attribute_id = Column(Integer, primary_key=True, nullable=False)
        attribute_language = Column(String, primary_key=True, nullable=False)
        attribute_status = Column(Integer)
        attribute_shrot_text = Column(String)
        attribute_text = Column(String)
        attribute_name = Column(String)
        attribute_sort_by = Column(String)
        attribute_page_frame = Column(String)
        attribute_table_name = Column(String)
        attribute_field_name = Column(String)
        attribute_notes = Column(String)

        def __repr__(self):
            return '<Attribute id: %d>' % self.attribute_id

    class CostAttributeValues(Base):
        __tablename__ = 'CostAttributeValues'
        attribute_value_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
        attribute_value_status = Column(Integer)
        x_attribute_id = Column(Integer)
        y_attribute_id = Column(Integer)
        attribute_value = Column(Numeric(8, 3))
        attribute_value_type = Column(String)
        attribute_value_name = Column(String)

        def __repr__(self):
            return '<Attribute value id: %d>' % self.attribute_value_id
