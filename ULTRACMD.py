import os
import subprocess
import random
from datetime import datetime

def print_ascii_art():
    print(r"""
   _____ __  __ _____    _    _ _   _______ _____            
  / ____|  \/  |  __ \  | |  | | | |__   __|  __ \     /\    
 | |    | \  / | |  | | | |  | | |    | |  | |__) |   /  \   
 | |    | |\/| | |  | | | |  | | |    | |  |  _  /   / /\ \  
 | |____| |  | | |__| | | |__| | |____| |  | | \ \  / ____ \ 
  \_____|_|  |_|_____/   \____/|______|_|  |_|  \_\/_/    \_\
                                                             
                                                             """)

def devmode():
    os.system('color 02')  # Change the terminal text color to green
    print("Developer mode activated (currently does nothing else).")

def normalcmd():
    subprocess.run("cmd", shell=True)  # Open the actual Windows CMD prompt

def hello():
    print("Hello! How can I assist you today?")

def calc():
    try:
        expression = input("Enter a mathematical expression (e.g., 2 + 2): ")
        result = eval(expression)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Error: {e}")

def display_datetime():
    now = datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

def quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "The only way to do great work is to love what you do.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Don't watch the clock; do what it does. Keep going.",
        "Keep your face always toward the sunshine—and shadows will fall behind you."
    ]
    print(random.choice(quotes))

def help_command():
    print("""
Available commands:
- devmode: Changes the terminal color to green.
- normalcmd: Opens the Windows CMD prompt.
- hello: Prints a friendly greeting.
- calc: Opens a simple calculator for basic arithmetic operations.
- datetime: Displays the current date and time.
- quote: Shows a random motivational quote.
- install_packages: Installs commonly used Python packages one by one.
- custompip <package>: Installs a specified Python package.
- clear: Clears the terminal.
- joe: Changes the terminal text color to yellow.
- help: Lists all available commands.
- exit: Exits the script.
""")

def install_packages():
    packages = ['numpy', 'pandas', 'requests', 'matplotlib', 'scipy']
    for package in packages:
        print(f"Installing {package}...")
        subprocess.run([os.sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed successfully.")

def custompip(package):
    try:
        print(f"Installing {package}...")
        subprocess.run([os.sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def joe():
    os.system('color 06')  # Change the terminal text color to yellow on Windows

def main():
    print_ascii_art()
    while True:
        command = input("Enter a command (type 'help' for list of commands, 'exit' to quit): ").strip().lower()
        if command == 'devmode':
            devmode()
        elif command == 'normalcmd':
            normalcmd()
        elif command == 'hello':
            hello()
        elif command == 'calc':
            calc()
        elif command == 'datetime':
            display_datetime()
        elif command == 'quote':
            quote()
        elif command == 'install_packages':
            install_packages()
        elif command.startswith('custompip '):
            package = command.split(' ')[1]
            custompip(package)
        elif command == 'clear':
            clear()
        elif command == 'joe':
            joe()
        elif command == 'help':
            help_command()
        elif command == 'exit':
            break
        else:
            print("Unknown command. Please try again. Type 'help' to see the list of commands.")

if __name__ == "__main__":
    main()
