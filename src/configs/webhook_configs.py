# Teams connectors
teams_connectors = {'<channel-name>': '<microsoft-teams-webhook>', \
                'default': '<default-teams-webhook>' }

# Proxies
proxies = { 'http': '<internal-proxy>', \
            'https': '<internal-proxy>' }

# Jinja2 templates
template_name = 'default_template.j2'

# Title
title = "Prometheus Monitoring System"

# Mapping colors
colors = { 'ok': '32FF41', \
                'warning': 'FFF632', \
                'critical': 'EA4300' }

# Mapping severity
severity = { 'firing': 'critical', \
                'resolved': 'ok' }

# Logging and debug mode
logging_dir = "logs/outputs.log"
logging_level = "WARNING"
