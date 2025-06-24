#!/usr/bin/env python3
"""My first MCP server - learning how this protocol works"""

import asyncio
import json
from typing import Any, Dict
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


# Create the server instance
server = Server("simple-mcp-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """Tell clients what tools we have"""
    return [
        Tool(
            name="hello",
            description="Print a greeting message",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name to greet (optional)",
                        "default": "World"
                    }
                }
            }
        ),
        Tool(
            name="calculate",
            description="Perform basic math calculations",
            inputSchema={
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "Math operation to perform"
                    },
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    }
                },
                "required": ["operation", "a", "b"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> list[TextContent]:
    """Handle tool calls"""
    
    if name == "hello":
        name_arg = arguments.get("name", "World")
        message = f"Hello, {name_arg}! 👋"
        return [TextContent(type="text", text=message)]
    
    elif name == "calculate":
        operation = arguments["operation"]
        a = float(arguments["a"])
        b = float(arguments["b"])
        
        try:
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return [TextContent(type="text", text="Error: Division by zero")]
                result = a / b
            else:
                return [TextContent(type="text", text=f"Error: Unknown operation {operation}")]
            
            return [TextContent(type="text", text=f"Result: {a} {operation} {b} = {result}")]
            
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {str(e)}")]
    
    else:
        return [TextContent(type="text", text=f"Error: Unknown tool {name}")]


async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())