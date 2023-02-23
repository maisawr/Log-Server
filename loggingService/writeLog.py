from datetime import datetime
import calendar

def writeLog(file_name, request_data, client_ip):
        # Open file with a+ access
        # If the file doesn't exist, it will create a new file and append to it
        # Otherwise, it will append to the existing file
        fhand = open(file_name, 'a+')

        # Get timestamp for current date and time
        current_time = datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.fromtimestamp(time_stamp)

        # Format timestamp
        date_time_str = date_time.strftime("%b %d %H:%M:%S")
        month = date_time.month

        # Parse request message
        request_data = request_data.split(":")
        client_name = request_data[0].strip()
        log_level = request_data[1].strip()
        process_id = request_data[2].strip()
        log_message = request_data[3].strip()

        # Log formatted as syslog
        formatted_log = f"{date_time_str} {client_name} application:<{log_level}>[{process_id}] {log_message} \n"

        # Write log message to file
        fhand.write(formatted_log)

        # Close file
        fhand.close()


# Syslog format
# timestamp hostname application:<level>[pid]: message
# timestamp format: month day hour -> Feb 19 13:20:49

# JSON format
#{
#    "timestamp": "",
#    "message": "",
#    "log": {
#        "level": "",
#        "file": "",
#        "line": 1,
#    },
#    "user": {
#        "name": "",
#        "id": "",
#    },
#    "event": {
#        "success": True
#    }
#}
