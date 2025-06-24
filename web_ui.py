#!/usr/bin/env python3
"""Web UI for MCP tools"""

from flask import Flask, render_template, request, jsonify
import asyncio
from mcp_server import call_tool, list_tools

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tools', methods=['GET'])
def get_tools():
    """Get available tools"""
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        tools = loop.run_until_complete(list_tools())
        return jsonify([{
            'name': tool.name,
            'description': tool.description,
            'schema': tool.inputSchema
        } for tool in tools])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/call', methods=['POST'])
def call_mcp_tool():
    """Call MCP tool"""
    try:
        data = request.json
        tool_name = data['name']
        arguments = data.get('arguments', {})
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(call_tool(tool_name, arguments))
        
        return jsonify({
            'success': True,
            'result': result[0].text if result else 'No result'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)