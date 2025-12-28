import logging 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger
logger.addHandler(ch)
def log_messages():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
log_messages()

# Real-life example: Logging in a file processing application
def process_user_data(filename):
    """
    Example function showing practical logging usage.
    Logging is useful for:
    - Debugging issues in production
    - Tracking application flow
    - Recording errors without crashing
    - Monitoring performance
    """
    try:
        logger.info(f"Starting to process file: {filename}")
        
        # Simulate file operations
        if not filename:
            logger.warning("Empty filename provided, using default")
            filename = "default.txt"
        
        logger.debug(f"Opening file: {filename}")
        # with open(filename) as f:
        #     data = f.read()
        
        logger.info(f"Successfully processed {filename}")
        return True
        
    except FileNotFoundError:
        logger.error(f"File not found: {filename}", exc_info=True)
        return False
    except Exception as e:
        logger.critical(f"Unexpected error processing {filename}: {e}", exc_info=True)
        return False

# Call the example
process_user_data("users.txt")
process_user_data("")




if __name__ == "__main__":
    log_messages()
