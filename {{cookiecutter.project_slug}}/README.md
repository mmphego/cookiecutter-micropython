{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if cookiecutter.add_codacy_badge == 'y' %}
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43713e0b78f547e8912ff05c9350cffb)](https://app.codacy.com/app/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}?utm_source=github.com&utm_medium=referral&utm_content={{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}&utm_campaign=Badge_Grade_Dashboard)
{% endif %}
{% if cookiecutter.add_python_version_badge == 'y' %}
[![Python](https://img.shields.io/badge/Python-3.6%2B-red.svg)](https://www.python.org/downloads/)
{% endif %}
{% if cookiecutter.add_saythanks_badge == 'y' %}
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/{{ cookiecutter.github_username }})
{% endif %}

{{ cookiecutter.project_short_description }}

# Installation


## Circuit Diagram

![image](assets/)

## Setup NodeMCU & Tools

Read the [docs](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html)

TL;DR
*   Clone the repo and,
*   Plug in the device to your computer

    **NOTE:** The installation assumes that the port name of device is `/dev/ttyUSB0` else, modify `Makefile` with port name [Hint:`$ ls /dev/tty.*`].
*   Run `make bootstrap`

    **NOTE:** This will install `esptool` and `mpfshell` for communicating with ESP chips and for serial connection with MicroPython boards, Eraze and flash the chip with firmware `esp8266-20190125-v1.10.bin` as well as upload the required files to the ESP.


## Feedback

Feel free to fork it or send me PR to improve it.

# Oh, Thanks!

By the way...
Click if you'd like to [saythanks](https://saythanks.io/to/>{{cookiecutter.github_username}})... :) else *Star* it.

✨🍰✨
