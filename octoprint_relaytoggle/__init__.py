# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

from periphery import GPIO




class RelaytogglePlugin(octoprint.plugin.StartupPlugin,
                        octoprint.plugin.TemplatePlugin,
                        octoprint.plugin.SettingsPlugin,
                        octoprint.plugin.EventHandlerPlugin):
    port = 17

    def on_after_startup(self):
        port = int(self._settings.get(["port"]))
        self._logger.info("HOLY TINKLES Im starting******* on port: %d" % port)
        gpio_out = GPIO("/dev/gpiochip0", port, "out")
        self._logger.info("setting up GPIO to be legit output")

    def get_settings_defaults(self):
        return dict(port=17)

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    def on_event(self,event,payload):
        if event == 'PrintStarted':
            gpio_out.write(True)
            self._logger.info("print started, lights on")
        elif event == 'PrintFailed':
            gpio_out.write(False)
            self._logger.info("print failed, lights off")
        elif event == 'PrintDone':
            gpio_out.write(False)
            self._logger.info("print done, lights off")
        elif event == 'PrintCancelled':
            gpio_out.write(False)
            self._logger.info("print cancelled. lights off")


__plugin_name__ = "Relaytoggle"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = RelaytogglePlugin()

