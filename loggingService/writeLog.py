from datetime import datetime
import json

# Constants definitions
json_format = "JSON"

def logger(file_name, request_data, log_format):
        # Open file with a+ access
        # If the file doesn't exist, it will create a new file and append to it
        # Otherwise, it will append to the existing file
        formatted_log = ""
        fhand = open(file_name, 'a+')

        if (log_format == json_format):
            formatted_log = format_as_json(request_data)
        else:
            formatted_log = format_as_syslog(request_data)

        # Write log message to file
        fhand.write(formatted_log)

        # Close file
        fhand.close()


# Syslog format
# timestamp hostname application:<level>[pid]: message
# timestamp format: month day hour -> Feb 19 13:20:49
def format_as_syslog(request_data):
        
        # Format timestamp
        date_time_str = get_timestamp().strftime("%b %d %H:%M:%S")

        # Parse request message
        request_data = request_data.split(":")
        client_name = request_data[0].strip()
        process_name = request_data[1].strip()
        log_level = request_data[2].strip()
        process_id = request_data[3].strip() 
        log_message = request_data[4].strip()
        
        # Log formatted as syslog
        formatted_log = f"{date_time_str} {client_name} {process_name}:<{log_level}>[{process_id}] {log_message} \n"

        return formatted_log



# JSON format
# Format the log as a JSON string
def format_as_json(request_data):
        
        # Format timestamp
        date_time_str = get_timestamp().strftime("%d %m %Y %H:%M:%S")

        # Parse request message
        request_data = request_data.split(":")
        client_name = request_data[0].strip()
        process_name = request_data[1].strip()
        log_level = request_data[2].strip()
        process_id = request_data[3].strip() 
        log_message = request_data[4].strip()
        
        # Log formatted as JSON
        # Create a dictionary
        formatted_log = {
            "timestamp": date_time_str,
            "message": log_message,
            "log": {
                "level": log_level,
                "file": process_name,
                "line": "",
            },
            "user": {
                "name": client_name,
                "id": "",
            },
            "event": {
                "success": True
            }
        }

        # Convert dictionary to JSON format
        JSON_log = json.dumps(formatted_log)

        formatted_log = f"{JSON_log} \n"

        return formatted_log



# Get timestamp for current date and time
def get_timestamp():
        current_time = datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.fromtimestamp(time_stamp)
        return date_time
