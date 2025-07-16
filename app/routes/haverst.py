from app import app
from flask import jsonify
from modules.haverst import haverst_tool

@app.route('/haverst')
def run_haverst():
    result = haverst_tool.run()
    return jsonify({'status': result})
