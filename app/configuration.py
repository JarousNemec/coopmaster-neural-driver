import os

host = "127.0.0.1"
port = 9002
hello_message = "Hello from neural driver"

log_file_name = "neural_driver.log"

def get_log_directory():
    return "./logs/"

def get_log_filename():
    return log_file_name