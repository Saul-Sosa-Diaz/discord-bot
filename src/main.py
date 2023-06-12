"""
File: main.py
Author: Saúl Sosa
Date: 26/04/2023
Description: Main program file
"""

from dotenv import load_dotenv
from bot import run_bot
import asyncio
import os


def main():
    load_dotenv()
    API_KEY = os.getenv('TOKEN')
    run_bot(API_KEY)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(str(err))
