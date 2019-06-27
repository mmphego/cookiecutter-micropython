# -*- coding: utf-8 -*-

"""Main module."""
import machine
import utime

from utils import MQTTWriter, Slack, Ubidots, current_time, force_garbage_collect

# Code goes here