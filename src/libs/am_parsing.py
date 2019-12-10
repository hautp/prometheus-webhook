#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader
from configs.webhook_configs import title, colors, severity


class AMParsing():
    def __init__(self):
        self.instances = []

    def parsing_data(self, data):
        ''' Collect variables from input '''
        for element in data['alerts']:
            ''' Key status '''
            status = element['status']

            ''' Key labels '''
            instance_name = element['labels']['instance'] 
            alert_name = element['labels']['alertname']
            ''' Check key exists in dictionary '''
            if 'channel' in element['labels']:
                channel = element['labels']['channel']
            else:
                channel = 'default'

            ''' Key annotations '''
            desc = element['annotations']['description']
            summary = element['annotations']['summary']

            ''' Generate body '''
            body = {'color': colors[severity[status]], \
                    'title': title, \
                    'status': severity[status].upper(), \
                    'instance_name': instance_name, \
                    'alert_name': alert_name, \
                    'channel': channel, \
                    'desc': desc, \
                    'summary': summary}
            self.instances.append(body)
        return (self.instances)


if __name__ == "__main__":
    pass