from typing import Any
from homeassistant import data_entry_flow
from homeassistant.components.repairs import RepairsFlow
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
import voluptuous as vol

from .const import DOMAIN

class MissingDeviceRepairFlow(RepairsFlow):
    """Handler for missing device repair flow."""

    def __init__(self, hass: HomeAssistant, device_id: str) -> None:
        self.hass = hass
        self.device_id = device_id

    async def async_step_init(
        self, user_input: dict[str, str] | None = None
    ) -> data_entry_flow.FlowResult:
        """Handle the initial step."""
        return await self.async_step_confirm_removal()

    async def async_step_confirm_removal(
        self, user_input: dict[str, str] | None = None
    ) -> data_entry_flow.FlowResult:
        """Handle device removal confirmation step."""
        if user_input is not None:
            await remove_missing_device(self.hass, self.device_id)
            return self.async_create_entry(title="", data={})

        return self.async_show_form(
            step_id="confirm_removal",
            data_schema=vol.Schema({}),
            description_placeholders={"device_id": self.device_id},
        )


async def remove_missing_device(hass: HomeAssistant, device_id: str):
    """Remove the missing device from Home Assistant."""
    device_registry = dr.async_get(hass)
    device_registry.async_remove_device(device_id)


async def async_create_fix_flow(
    hass: HomeAssistant,
    issue_id: str,
    *args: Any,
    **kwargs: Any,
) -> RepairsFlow | None:
    """Create a fix flow based on the issue ID."""
    if issue_id.startswith("missing_device"):
        device_id = issue_id.split("_")[-1]
        return MissingDeviceRepairFlow(hass, device_id)
    return None
