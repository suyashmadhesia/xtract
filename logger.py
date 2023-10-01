import logging

# Create a custom logger for INFO-level messages
info_logger = logging.getLogger("info")
info_logger.setLevel(logging.INFO)

# Create a custom logger for ERROR-level messages
error_logger = logging.getLogger("error")
error_logger.setLevel(logging.ERROR)

# Create handlers for both loggers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('./logs/app.log')

# Set log levels for handlers
console_handler.setLevel(logging.INFO)  # Set the desired log level for console output
file_handler.setLevel(logging.INFO)     # Set the desired log level for the log file

# Create formatters and add them to handlers
console_format = logging.Formatter('%(levelname)s - %(message)s')
file_format = logging.Formatter('%(levelname)s - %(asctime)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to both loggers
info_logger.addHandler(console_handler)
info_logger.addHandler(file_handler)

error_logger.addHandler(console_handler)
error_logger.addHandler(file_handler)
