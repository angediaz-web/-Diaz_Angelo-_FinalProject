"""
Premium display utilities for the Python Core Lessons Study CLI.
"""

import os

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pauses the screen until the user presses Enter."""
    input(f"\n{DIM}{YELLOW}Press Enter to continue...{RESET}")


def print_section():
    """Prints a premium divider."""
    print(f"\n{BLUE}{'━' * 64}{RESET}")


def print_header():
    """Displays the premium application header."""
    print(f"{MAGENTA}╔{'═' * 62}╗{RESET}")
    print(
        f"{MAGENTA}║{RESET}"
        f"{BOLD}{WHITE}{'PYTHON CORE LESSONS STUDY CLI'.center(62)}{RESET}"
        f"{MAGENTA}║{RESET}"
    )
    print(f"{MAGENTA}╚{'═' * 62}╝{RESET}")
    print()


def print_menu():
    """Displays the premium main menu."""
    print(f"{BOLD}{WHITE}MAIN MENU{RESET}")
    print(f"{DIM}{'─' * 25}{RESET}")

    print(f"{CYAN}[01]{RESET}  {WHITE}View lesson list{RESET}")
    print(f"{CYAN}[02]{RESET}  {WHITE}Study a lesson{RESET}")
    print(f"{CYAN}[03]{RESET}  {WHITE}Take a quiz{RESET}")
    print(f"{CYAN}[04]{RESET}  {WHITE}Search lessons{RESET}")
    print(f"{CYAN}[05]{RESET}  {WHITE}Sort lessons A-Z{RESET}")
    print(f"{CYAN}[06]{RESET}  {WHITE}View progress{RESET}")
    print(f"{YELLOW}[07]{RESET}  Exit")
    print()