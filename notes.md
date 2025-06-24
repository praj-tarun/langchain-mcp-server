# My MCP Learning Notes

## What I Figured Out

Started this to understand how AI tools can use external functions. MCP seems like the standard way to do this.

### Key Insights:
- MCP is basically JSON-RPC with specific message formats
- Tools are just functions with schema definitions
- The protocol handles discovery and execution
- Debugging is mostly about watching the JSON messages

### Things That Tripped Me Up:
- File paths in configs need to be absolute
- Different AI clients expect configs in different places
- Error messages aren't always helpful
- Some clients don't support MCP yet (looking at you, Copilot)

### What Actually Works:
- Claude Desktop: Best MCP support so far
- Web UI: Always reliable for testing
- Direct Python calls: Good for debugging
- VS Code extensions: Hit or miss

## Next Steps

Want to try:
- File operations (read/write)
- API calls to external services
- Multi-step workflows
- RAG with vector databases

## Debugging Tips I Learned

1. Always start with simple print statements
2. Log the JSON messages - that's where the real info is
3. Test tools directly before adding MCP protocol
4. Use absolute paths in configs
5. Restart clients after config changes

## Resources That Helped

- MCP specification docs
- Claude Desktop examples
- LangChain debugging guides

## Random Thoughts

MCP feels like it could be the standard for AI tool integration. Similar to how REST became the standard for web APIs. The protocol is simple enough to implement but flexible enough for complex use cases.

Still figuring out the best practices for error handling and tool composition. The ecosystem is young but growing fast.