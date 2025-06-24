#!/usr/bin/env python3
"""Testing the MCP protocol - seeing if I can talk to my server"""

import subprocess
import json
import time


def test_mcp_server():
    """Fire up the server and see if it responds properly"""
    
    # Start server
    process = subprocess.Popen(
        ["python", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    try:
        # Initialize
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0.0"}
            }
        }
        
        process.stdin.write(json.dumps(init_request) + "\n")
        process.stdin.flush()
        
        # Read response
        response = process.stdout.readline()
        print(f"Init response: {response.strip()}")
        
        # List tools first
        list_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        }
        
        process.stdin.write(json.dumps(list_request) + "\n")
        process.stdin.flush()
        
        response = process.stdout.readline()
        print(f"Tools list: {response.strip()}")
        
        # Test hello tool
        hello_request = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "hello",
                "arguments": {"name": "MCP Tester"}
            }
        }
        
        process.stdin.write(json.dumps(hello_request) + "\n")
        process.stdin.flush()
        
        response = process.stdout.readline()
        print(f"Hello response: {response.strip()}")
        
        # Test calculate tool
        calc_request = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "calculate",
                "arguments": {
                    "operation": "add",
                    "a": 10,
                    "b": 5
                }
            }
        }
        
        process.stdin.write(json.dumps(calc_request) + "\n")
        process.stdin.flush()
        
        response = process.stdout.readline()
        print(f"Calculate response: {response.strip()}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        process.terminate()
        process.wait()


if __name__ == "__main__":
    test_mcp_server()