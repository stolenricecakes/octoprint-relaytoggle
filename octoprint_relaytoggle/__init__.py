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

    def gimme_the_port:
        return GPIO("/dev/gpiochip0", port, "out"

    def on_event(self,event,payload):
        if event == 'PrintStarted':
            self._logger.info("print started, trying to turn lights on")
            gpio_out = gimme_the_port()
            gpio_out.write(True)
            gpio_out.close()
            self._logger.info("print started, lights on now")
        elif event == 'PrintFailed':
            self._logger.info("print failed, trying to turn lights off")
            gpio_out = gimme_the_port()
            gpio_out.write(False)
            gpio_out.close()
            self._logger.info("print failed, lights off now")
        elif event == 'PrintDone':
            self._logger.info("print done, trying to turn lights off")
            gpio_out = gimme_the_port()
            gpio_out.write(False)
            gpio_out.close()
            self._logger.info("print done, lights off now")
        elif event == 'PrintCancelled':
            self._logger.info("print cancelled. trying to turn lights off")
            gpio_out = gimme_the_port()
            gpio_out.write(False)
            gpio_out.close()
            self._logger.info("print cancelled. lights off now")


__plugin_name__ = "Relaytoggle"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = RelaytogglePlugin()

