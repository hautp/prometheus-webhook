#!/usr/bin/env python
from flask import render_template, request, jsonify
from app import app
from funcs.alert_manager import AlertManager
from funcs.setup_logging import logger

@app.route('/')
def index():
    return jsonify({"message": "Prometheus Webhook HomePage"}), 200

@app.route('/api/teams/', methods=['POST'])
def teams():
    if request.data:
    	data = request.json
    	am = AlertManager()
    	return (am.push_msg(data))
    else:
    	logger.warning("Do not get body from POST request.")
    	return jsonify({"message": "Empty body from POST request."}), 400

if __name__ == '__main__':
    pass
