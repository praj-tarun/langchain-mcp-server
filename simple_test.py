#!/usr/bin/env python3
"""Direct test of MCP server functions"""

import asyncio
from mcp_server import call_tool, list_tools


async def simple_test():
    """Test server functions directly"""
    
    print("=== Testing MCP Server Functions ===")
    
    # Test list_tools
    print("\n1. Testing list_tools...")
    tools = await list_tools()
    print(f"Available tools: {[tool.name for tool in tools]}")
    
    # Test hello tool
    print("\n2. Testing hello tool...")
    result = await call_tool("hello", {"name": "Direct Tester"})\n    print(f"Result: {result[0].text}")
    
    # Test calculate tool
    print("\n3. Testing calculate tool...")
    result = await call_tool("calculate", {
        "operation": "multiply",
        "a": 7,
        "b": 8
    })
    print(f"Result: {result[0].text}")
    
    # Test error case
    print("\n4. Testing error case...")
    result = await call_tool("calculate", {
        "operation": "divide",
        "a": 10,
        "b": 0
    })
    print(f"Result: {result[0].text}")
    
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    asyncio.run(simple_test())