import logging
import os
import sys
from colorama import Fore,Style
import psutil
import time

home = os.environ['HOME']
project_dir = os.path.join(home, '.scaner')
if not os.path.exists(project_dir):
    os.makedirs(project_dir)
db_path = os.path.join(project_dir, 'db')

log_path = os.path.join(project_dir, 'scaner.log')
logging.basicConfig(filename=log_path, filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.INFO)

def log_info(msg, *args, **kwargs):
    logging.info(msg, *args, **kwargs)

def log_error(msg, *args, **kwargs):
    logging.error(msg, *args, **kwargs)

def progress_msg(content):
    print(Fore.CYAN + '[ Scaner ]: ' + content + '...' + Fore.RESET)

def status_msg(category, detail):
    if sys.stdout.isatty() and psutil.POSIX:
        fmt = '%-13s %s' % (Fore.BLUE + Style.BRIGHT + str(category),
                            Fore.RESET + Style.RESET_ALL + str(detail))
    else:
        fmt = '%-11s %s' % (category, detail)
    print(fmt)

def status_msg_div():
    print(Fore.BLUE + Style.BRIGHT + '------------------------------------------' + Fore.RESET + Style.RESET_ALL)


def timestamp_to_strftime(timestamp_ms):
    timeArray = time.localtime(timestamp_ms/1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

