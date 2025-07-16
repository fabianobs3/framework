from app import app
from flask import jsonify
from modules.osintgram import osintgram_tool

@app.route('/osintgram')
def run_osintgram():
    result = osintgram_tool.run()
    return jsonify({'status': result})
