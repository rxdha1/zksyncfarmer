import os
import random
import sys
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

import questionary
from loguru import logger
from questionary import Choice
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from config import PROXIES
from modules_settings import *
from utils.helpers import remove_wallet
from utils.sleeping import sleep

# Replace the direct import of sensitive information with environment variables
USE_PROXY = os.getenv('USE_PROXY', 'False').lower() in ('true', '1', 't')
RANDOM_WALLET = os.getenv('RANDOM_WALLET', 'False').lower() in ('true', '1', 't')
SLEEP_FROM = int(os.getenv('SLEEP_FROM', '1'))
SLEEP_TO = int(os.getenv('SLEEP_TO', '5'))
QUANTITY_THREADS = int(os.getenv('QUANTITY_THREADS', '10'))
THREAD_SLEEP_FROM = int(os.getenv('THREAD_SLEEP_FROM', '1'))
THREAD_SLEEP_TO = int(os.getenv('THREAD_SLEEP_TO', '5'))
REMOVE_WALLET = os.getenv('REMOVE_WALLET', 'False').lower() in ('true', '1', 't')
ACCOUNTS = os.getenv('ACCOUNTS', '').split(',')

def get_module():
    # ... (No changes in this function)

def get_wallets():
    # ... (No changes in this function)

async def run_module(module, account_id, key, proxy):
    # ... (No changes in this function)

def _async_run_module(module, account_id, key, recipient):
    asyncio.run(run_module(module, account_id, key, recipient))

def main(module):
    wallets = get_wallets()

    if RANDOM_WALLET:
        random.shuffle(wallets)

    with ThreadPoolExecutor(max_workers=QUANTITY_THREADS) as executor:
        for _, account in enumerate(wallets, start=1):
            executor.submit(
                _async_run_module,
                module,
                account.get("id"),
                account.get("key"),
                account.get("proxy")
            )
            time.sleep(random.randint(THREAD_SLEEP_FROM, THREAD_SLEEP_TO))

if __name__ == '__main__':
    print("❤️ Subscribe to me – https://t.me/CyberRyda\n")

    logger.add("logging.log")

    module = get_module()
    if module == "tx_checker":
        get_tx_count()
    else:
        main(module)

    print("\n❤️ Subscribe to me – https://t.me/CyberRyda\n")
    print("🤑 Donate me: 0x24744DF6A4cc3a80E094B60109Af9d536b9968Fe")
