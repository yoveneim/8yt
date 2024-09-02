import time
import psutil
from datetime import datetime, timedelta

# List of game processes to block
game_processes = ["JagexLauncher.exe", "Wow.exe", "ev.exe"]  # Replace with actual game process names

# Function to check and kill game processes
def block_games():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in game_processes:
            proc.kill()

# Function to track work time
def track_work_time(work_duration):
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=work_duration)
    while datetime.now() < end_time:
        block_games()
        time.sleep(300)  # Check every 5 minute

# Main function
if __name__ == "__main__":
    
    block_games()
#    work_duration = 2  # Work for 2 hours;
#    print(f"Work for {work_duration} hours to unlock games.")
#    track_work_time(work_duration)
#    print("You can now play games!")
