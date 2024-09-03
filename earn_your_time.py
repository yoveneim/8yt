import time
import psutil
from datetime import datetime, timedelta
import logging 
from plyer import notification
import pyautogui
import json

# Set up logging
logging.basicConfig(level=logging.INFO,filename='earn_your_time.log', format='%(asctime)s - %(message)s')

def is_user_active():
    return pyautogui.position() != (0, 0)

# Send notification 
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="8yt",
        timeout=10
    )

# List of game processes to block
def load_game_list():
    try:
        with open('game_list.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Game list file not found. Using default list.")
        return ["JagexLauncher.exe", "Wow.exe", "ev.exe"]

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
    end_time = start_time + timedelta(minutes=work_duration)
    logging.info(f"Work tracking started. End time: {end_time}")
    while datetime.now() < end_time:
        if not is_user_active():
            logging.warning("User is not active.")
            send_notification("User is not active", "A one minute delay will be added to your work time.")
            end_time += timedelta(minutes=1)
        block_games()
        time.sleep(5)  # Check every 5 minutes
    logging.info("Work time completed!")


# send notification multiple times using : send_notification("title", "message")
if __name__ == "__main__":
    game_processes = load_game_list()
    work_duration = float(input("Enter work duration in minutes: "))
    send_notification("Work started", f"Cession begin, working for {work_duration} minutess")
    logging.info(f"Work for {work_duration} minutes to unlock games.")
    track_work_time(work_duration)
    logging.info("You can now play games!")
    send_notification("Focus cession completed", "You earned your time")
