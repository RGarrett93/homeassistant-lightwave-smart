---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

Please describe your issues here.

Ideally provide output from homeassistant.log, preferably with additional logging enabled.

To enable additional logging, add the following to configuration.yaml

logger:
  default: warning
  logs:
    lightwave_smart.lightwave_smart: debug
    custom_components.lightwave_smart: debug
