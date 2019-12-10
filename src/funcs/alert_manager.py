#!/usr/bin/env python
import os
import requests
import json
from jinja2 import Environment, FileSystemLoader
from libs.am_parsing import AMParsing
from funcs.setup_logging import logger
from configs.webhook_configs import teams_connectors, proxies, template_name


class AlertManager():
    def __init__(self):
        ''' Load AMParsing function'''
        self.am = AMParsing()


        ''' Get templates directory '''
        self.template_dir = 'templates'
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

        ''' Set jinja2 environment '''
        self.j2_env = Environment(loader=FileSystemLoader(os.path.join(self.current_dir, self.template_dir)))

    def push_msg(self, data):
        ''' Load templates '''
        self.template = self.j2_env.get_template(template_name)
        alerts = self.am.parsing_data(data)
        try:
            for alert in alerts:
                msg = self.template.render(alert)

                #logger.info("Push a message to teams connector through proxy.")
                req = requests.post(url=teams_connectors[alert['channel']], \
                            proxies=proxies, \
                            json=json.loads(msg))

            #logger.info("The message has been successfully sent.")
            return (json.dumps({"message": "SUCCESS"}), 200)
        except Exception as err:
            logger.error("Could not send message to teams connector. Output: %s" % err)
            return (json.dumps({"message": "FALSE"}), 500)


if __name__ == "__main__":
    pass