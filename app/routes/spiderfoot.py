from app import app
from flask import jsonify
from modules.spiderfoot import spiderfoot_tool

@app.route('/spiderfoot')
def run_spiderfoot():
    result = spiderfoot_tool.run()
    return jsonify({'status': result})
