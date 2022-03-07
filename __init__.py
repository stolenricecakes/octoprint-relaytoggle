# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import RPi.GPIO as GPIO

class Relaytoggle(octoprint.plugin.StartupPlugin,
                 octoprint.plugin.TemplatePlugin):
    def log
    def on_after_startup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        self._logger.info("setting up GPIO to be legit output")
        log = self._logger

    def on_event(event,payload):
        if event == 'PrintStarted':
            GPIO.output(17, GPIO.HIGH)
            log.info("print started, lights on")
        elif event == 'PrintFailed':
            GPIO.output(17, GPIO.LOW)
            log.info("print failed, lights off")
        elif event == 'PrintDone':
            GPIO.output(17, GPIO.LOW)
            log.info("print done, lights off")
        elif event == 'PrintCancelled':
            GPIO.output(17, GPIO.LOW)
            log.into("print cancelled. lights off)



__plugin_name__ = "Relaytoggle"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = Relaytoggle()

