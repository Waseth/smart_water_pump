def log_status(message):
    with open("pump_log.txt", "a") as log_file:
        log_file.write(f"{message}\n")
