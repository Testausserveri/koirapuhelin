"""Koirapuhelin main program file.

Copyright (c) 2024 Testausserveri ry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import discord
import dotenv

import config

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Prints a message when the bot is initialised"""

    print(f"Logged in as {client.user}")


def start():
    """Starts the bot using a token found in the environment variables"""
    dotenv.load_dotenv(".env")

    if not config.TOKEN_NAME in os.environ:
        print("Token not found in environment variables")
        return

    client.run(os.environ[config.TOKEN_NAME])


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        sys.exit(0)
