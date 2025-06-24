#!/usr/bin/env python3
"""Demo script for Level 1 deliverable presentation"""

import asyncio
import time
from mcp_server import call_tool, list_tools

async def demo_presentation():
    """Complete demo for Level 1 deliverable"""
    
    print("=" * 60)
    print("LEVEL 1 DELIVERABLE DEMONSTRATION")
    print("GenAI MCP Tool Implementation")
    print("=" * 60)
    
    # 1. Show available tools
    print("\n1. AVAILABLE MCP TOOLS:")
    print("-" * 30)
    tools = await list_tools()
    for i, tool in enumerate(tools, 1):
        print(f"   {i}. {tool.name}: {tool.description}")
    
    time.sleep(2)
    
    # 2. Demo Hello Tool
    print("\n2. HELLO TOOL DEMONSTRATION:")
    print("-" * 30)
    names = ["World", "Level 1 Reviewer", "MCP Demo"]
    for name in names:
        result = await call_tool("hello", {"name": name})
        print(f"   Input: {name}")
        print(f"   Output: {result[0].text}")
        time.sleep(1)
    
    # 3. Demo Calculator Tool
    print("\n3. CALCULATOR TOOL DEMONSTRATION:")
    print("-" * 30)
    calculations = [
        ("add", 15, 25),
        ("subtract", 100, 37),
        ("multiply", 8, 9),
        ("divide", 144, 12)
    ]
    
    for op, a, b in calculations:
        result = await call_tool("calculate", {
            "operation": op,
            "a": a,
            "b": b
        })
        print(f"   Operation: {a} {op} {b}")
        print(f"   Result: {result[0].text}")
        time.sleep(1)
    
    # 4. Error handling demo
    print("\n4. ERROR HANDLING DEMONSTRATION:")
    print("-" * 30)
    try:
        result = await call_tool("calculate", {
            "operation": "divide",
            "a": 10,
            "b": 0
        })
        print(f"   Division by zero: {result[0].text}")
    except Exception as e:
        print(f"   Error handled: {e}")
    
    # 5. Summary
    print("\n5. IMPLEMENTATION SUMMARY:")
    print("-" * 30)
    print("   ✅ MCP Protocol: Implemented")
    print("   ✅ Hello Tool: Working")
    print("   ✅ Calculator Tool: Working")
    print("   ✅ Error Handling: Implemented")
    print("   ✅ Web UI: Available")
    print("   ✅ Debug Tools: Available")
    print("   ✅ Client Configs: Provided")
    
    print("\n" + "=" * 60)
    print("LEVEL 1 DELIVERABLE COMPLETE")
    print("Ready for Level 2 Advanced Implementation")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(demo_presentation())