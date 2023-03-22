import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import light, i2c
from esphome.const import CONF_OUTPUT_ID

qwiic_twist_ns = cg.esphome_ns.namespace("qwiic_twist")
QwiicTwist = qwiic_twist_ns.class_("QwiicTwist", light.LightOutput)

DEPENDENCIES = ["light", "i2c"]
AUTO_LOAD = ["light"]

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(CONF_OUTPUT_ID): cv.declare_id(QwiicTwist),
        }
    )
    .extend(light.RGB_LIGHT_SCHEMA)
    .extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_OUTPUT_ID])
    await light.register_light(var, config)

