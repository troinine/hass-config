# My Home Assistant config

DISCLAIMER: Just that you are aware, this is probably a forever-work-in-progress project 😊

![Screenshot](/assets/images/screenshot-tablet.png)

## Introduction

My home assistant journey started roughly 2018 but was not very active for the first two years. I was happy with the default lovelace UI for a while until I started to notice projects that took a completely different way to design their dashboards.

Big insparation came from the [UI-Lovelace-Minimalist](https://github.com/UI-Lovelace-Minimalist/UI) project and from [@matt8707](https://github.com/matt8707/hass-config)'s nice design!

After learning how to use the excellent [button-card](https://github.com/custom-cards/button-card) I came up with my current design for tablet and mobile. Yes, this design is heavily based on the button-card. Maybe I went a bit too deep with it...

Hope you enjoy and find things useful in this repo! ⭐

## Setup

Home Assistant runs on [Docker](https://hub.docker.com/r/homeassistant/home-assistant) on a [Synology NAS](https://www.synology.com). Users access Home Assistant through the [Companion App](https://companion.home-assistant.io) on their mobile. In addition, the house has table mounted [10.5" Samsung Galaxy Tab A8](https://www.samsung.com/uk/tablets/galaxy-tab-a/galaxy-tab-a8-wifi-dark-gray-32gb-sm-x200nzaaeua/).

Configuration is performed using the YAML mode.

The following custom cards are extensively used throughout the dashboards:

- [button-card](https://github.com/custom-cards/button-card)
- [mini-graph-card](https://github.com/kalkih/mini-graph-card)
- [card-mod](https://github.com/thomasloven/lovelace-card-mod)
- [layout-card](https://github.com/thomasloven/lovelace-layout-card)
- [light-entity-card](https://github.com/ljmerza/light-entity-card)

Plus few others.

## Features

### Sidebar, notifications and clock

### Popups

## Hardware and software

The following table contains some of the hardward and software I use with Home Assistant

| Product                     | Description                                                                                                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Philips Hue                 | Philips Hue Bridge with light strips, bulbs, motion sensors, dimmer switches                                                                                                                        |
| Synology Diskstation DS220+ | NAS which runs Home Assistant and bunch of other services for my needs                                                                                                                              |
| Ruuvi                       | A bunch of RuuviTags. I have a custom-built software that reads data from these tags                                                                                                                |
| Raspberry Pi Zero           | Provides near real-time data from the ground source heat pump. Reads data from RuuviTags. Is equipped with [Readbear's IOT pHAT](https://github.com/redbear/IoT_pHAT) for Wifi and BT connectivity. |
| Nibe 1226 NEW 8kW           | Ground source heat pump providing heating and cooling to the house                                                                                                                                  |

In addition to HW I use a collection of OSS

| Software                                                                                                     | Description                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ruuvi-mqtt-data-publisher](https://github.com/troinine/ruuvi-mqtt-data-publisher)                           | A forked version of [Scrin/RuuviCollector](https://github.com/Scrin/RuuviCollector) that reads data from RuuviTags and publishes it to an MQTT Broker |
| [airthings-waveplus-mqtt-data-publisher](https://github.com/troinine/airthings-waveplus-mqtt-data-publisher) | Reads data from Airthings Wave Plus sensors and publishes it to an MQTT broker                                                                        |
| [Eclipse Mosquitto](https://mosquitto.org)                                                                   | Receives data from various MQTT clients and is observed by Home Assistant                                                                             |
| Nibe heat pump MQTT data publisher                                                                           | Custom-built app that reads Nibe heat pump logs through an USB OTG mass-storage emulation and publishes the data to an MQTT broker                    |

## Special thanks!

TBD

## License

MIT
