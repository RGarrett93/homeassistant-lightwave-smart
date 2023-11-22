from .const import DOMAIN
from homeassistant.helpers.device_registry import DeviceInfo

def make_device_info(entity, name = None):
    feature_set = entity._lwlink.featuresets[entity._featureset_id]

    return DeviceInfo({
        'identifiers': { (DOMAIN, entity._featureset_id) },
        'name': name or entity.name,
        'manufacturer': feature_set.manufacturer_code,
        'model': feature_set.product_code,
        'serial_number': feature_set.serial,
        'sw_version': feature_set.firmware_version,
        'via_device': (DOMAIN, entity._linkid),
    })
