import asyncio
from random import random

from parlant.sdk import (
    PluginServer,
    ToolContext,
    ToolResult,
    tool,
)

PORT = 8089


@tool
async def get_random_number(context: ToolContext) -> ToolResult:
    return ToolResult(data=int(random() * 1000))


TOOLS = [
    get_random_number,
]


async def main() -> None:
    async with PluginServer(tools=TOOLS, port=PORT):
        pass


if __name__ == "__main__":
    asyncio.run(main())
