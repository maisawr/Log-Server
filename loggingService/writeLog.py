# Filename: writeLog.py
# Project: loggingService
# By: Maísa Wolff Resplande, student ID 8778967
# Date: Feb 24, 2023
# Description: This file define the functions to write the log to .txt in different formats (Syslog or JSON)



from datetime import datetime
import json
import sys
import os
import platform



# Constants definitions
json_format = "JSON"



# Write log to a .txt file
# Open file with a+ access
# If the file doesn't exist, it will create a new file and append to it
# Otherwise, it will append to the existing file
def logger(file_name, request_data, log_format):
        
        formatted_log = ""

        try:
            with open(file_name, 'a+') as file:

                if (log_format == json_format):
                    formatted_log = format_as_json(request_data)
                else:
                    formatted_log = format_as_syslog(request_data)

                try:
                    # Write log message to file
                    file.write(formatted_log)
                except Exception as e:
                    sys.exit(f"Error writing to file: {e}.\nExiting logging server.\n")

        except Exception as e:
            sys.exit("Error creating/appending to file: {e}.\nExiting logging server.\n")



# Syslog format
# timestamp hostname application:<level>[pid]: message
# timestamp format: month day hour -> Feb 19 13:20:49
def format_as_syslog(request_data):
        
        # Format timestamp
        date_time_str = get_timestamp().strftime("%b %d %H:%M:%S")
    
        # Split the request
        request_data = request_data.split(":")

        # Parse request message
        if len(request_data) == 5:                          # check number of arguments from log message
            
            client_name = request_data[0].strip()
            process_name = request_data[1].strip()
            log_level = request_data[2].strip()
            process_id = request_data[3].strip() 
            log_message = request_data[4].strip()

            # Log formatted as syslog
            formatted_log = f"{date_time_str} {client_name} {process_name}:<{log_level}>[{process_id}] {log_message} \n"

        else:                                               # wrong format
            
            server_name = platform.node()
            process_name = sys.argv[0]
            process_id = os.getpid()
            log_level =  "ERROR"
            log_message = "Client sent the wrong format to the log. Not recording the client log."
            
            formatted_log = f"{date_time_str} {server_name} {process_name}:<{log_level}>[{process_id}] {log_message} \n"

        return formatted_log
        


# JSON format
# Format the log as a JSON string
def format_as_json(request_data):
        
        # Format timestamp
        date_time_str = get_timestamp().strftime("%d %m %Y %H:%M:%S")

        if len(request_data) == 5:                          # check number of arguments from log message
            # Parse request message
            request_data = request_data.split(":")
            client_name = request_data[0].strip()
            process_name = request_data[1].strip()
            log_level = request_data[2].strip()
            process_id = request_data[3].strip() 
            log_message = request_data[4].strip()
        

        else:                                               # wrong format
            server_name = platform.node()
            process_name = sys.argv[0]
            process_id = os.getpid()
            log_level =  "ERROR"
            log_message = "Client sent the wrong format to the log. Not recording the client log."

        #Log formatted as JSON
        # Create a dictionary
        formatted_log = {
            "timestamp": date_time_str,
            "message": log_message,
            "log": {
                "level": log_level,
                "file": process_name,
            },
            "user": {
                "name": client_name,
            }
        }
        
        # Convert dictionary to JSON format
        JSON_log = json.dumps(formatted_log)

        # Log formatted as a JSON string
        formatted_log = f"{JSON_log}\n"

        return formatted_log



# Get timestamp for current date and time
def get_timestamp():
        current_time = datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.fromtimestamp(time_stamp)
        return date_time
