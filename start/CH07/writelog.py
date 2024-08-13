import datetime

def create_log_entry(ip_address, identd, username, resource_message, http_return_code, return_size):
    timestamp = datetime.datetime.now().strftime("[%d/%b/%Y:%H:%M:%S %z]")

    log_entry = f'{ip_address} {identd} {username} {timestamp} "{resource_message}" {http_return_code} {return_size}\n'

    with open('access.log', 'a') as log_file:
        log_file.write(log_entry)

    print("Log entry added successfully.")

create_log_entry('192.168.1.1', '-', 'johnnah', 'GET /index.html HTTP/1.1', '200', '1234')
