import logging

log_filename = 'logg/example.log'

#Standard configuration
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#Function to add two numbers
def add(x, y):
    logging.debug(f"Adding {x} and {y}")
    result = x + y
    logging.info(f"Result: {result}")
    return result

if __name__ == "__main__":
    logging.info("Program started")
    
    result = add(3, 4)
    logging.info(f"Calculation complete. Result: {result}")
    
    logging.debug("Debugging information")
    
    logging.info("Program finished")

