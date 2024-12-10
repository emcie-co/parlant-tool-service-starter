import asyncio
from random import random

from parlant.sdk import (
    PluginServer,
    ToolContext,
    ToolResult,
    tool,
)


@tool
async def get_random_number(context: ToolContext) -> ToolResult:
    return ToolResult(data=int(random() * 1000))


TOOLS = [
    get_random_number,
]


async def main() -> None:
    async with PluginServer(tools=TOOLS, port=8089):
        pass


if __name__ == "__main__":
    asyncio.run(main())
