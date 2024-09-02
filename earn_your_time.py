import time
import psutil
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# List of game processes to block
game_processes = ["JagexLauncher.exe", "Wow.exe", "ev.exe"]  # Replace with actual game process names

def block_games():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in game_processes:
            try:
                proc.kill()
                logging.info(f"Blocked game process: {proc.info['name']}")
            except psutil.NoSuchProcess:
                pass
            except psutil.AccessDenied:
                logging.warning(f"Access denied when trying to kill {proc.info['name']}")

def track_work_time(work_duration):
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=work_duration)
    logging.info(f"Work tracking started. End time: {end_time}")
    while datetime.now() < end_time:
        block_games()
        time.sleep(300)  # Check every 5 minutes
    logging.info("Work time completed!")

if __name__ == "__main__":
#    work_duration = 2  # Work for 2 hours
    logging.info(f"Work for {work_duration} hours to unlock games.")
    track_work_time(work_duration)
    logging.info("You can now play games!")
