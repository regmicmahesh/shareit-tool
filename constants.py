from enum import Enum
BANNER = """
*****************************************************
*    ____  _   _    _    ____  _____   ___ _____    *
*   / ___|| | | |  / \  |  _ \| ____| |_ _|_   _|   *
*   \___ \| |_| | / _ \ | |_) |  _|    | |  | |     *
*    ___) |  _  |/ ___ \|  _ <| |___   | |  | |     *
*   |____/|_| |_/_/   \_\_| \_\_____| |___| |_|.py  *
*                                                   *
*   Programmed By Sachit Yadav                      *
*   https://github.com/ASACHIT/shareit-tool.git     *
*****************************************************
"""
class COMMAND_HANDLER_KEYS(Enum):
    PRINT_ALLOCATED_PORTS = 1
    SHARE_FILE = 2


HELP_MESSAGE = """
What do you want to do?
1. Share a file.
2. Print all allocated ports.
3. Exit.
"""
