# My MCP Learning Journey

Started this project to understand how MCP works with AI tools. Built a simple server with basic tools to test the protocol.

## What I Built

- Simple greeting tool (because hello world is always first!)
- Basic calculator for math operations
- Debug logging to see what's happening under the hood

## Getting Started

Just need Python and a few packages:

```bash
pip install -r requirements.txt
pip install mcp flask
python mcp_server.py
```

That's it! No API keys needed for this basic setup.

## How to Test

**Web interface** (easiest way):
```bash
python web_ui.py
```
Open http://localhost:5000 and click around

**Quick function test**:
```bash
python simple_test.py
```

**Full protocol test** (if you're curious about JSON-RPC):
```bash
python test_client.py
```

## AI Tool Integration

### For Claude:
1. Copy `mcp_config.json` to your AI tool's MCP configuration directory
2. Restart your AI tool
3. The tools will be available as `simple-mcp-server___hello` and `simple-mcp-server___calculate`

### Available Tools:

**hello**
- Description: Print a greeting message
- Parameters: `name` (optional string)
- Example: `{"name": "Alice"}`

**calculate**
- Description: Perform basic math calculations
- Parameters: 
  - `operation` (required): "add", "subtract", "multiply", "divide"
  - `a` (required): First number
  - `b` (required): Second number
- Example: `{"operation": "add", "a": 10, "b": 5}`
