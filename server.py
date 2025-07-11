# server.py
from mcp.server.fastmcp import FastMCP

# Create an MMCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers.
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    """
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """
    Divide two numbers.
    """
    return a / b


@mcp.tool()
def myName() -> str:
    """
    Return the name .
    """
    return "JUNJIE LI"

if __name__ == "__main__":
    mcp.run()