# 8yt (Earn Your Time)

8yt is a small Windows-focused focus timer that blocks games for a set work session. You enter a number of minutes, and the script kills any process on your game list until that time has passed. It also watches for mouse inactivity and extends the session when you step away.

## Features

- **Timed focus sessions:** Enter a work duration in minutes and the session starts immediately.
- **Game blocking:** Terminates processes whose names appear in a game list, every few seconds, for the length of the session.
- **Inactivity penalty:** If the mouse hasn't moved, you get a notification and one minute is added to the session.
- **Desktop notifications:** Alerts when the session starts, when you're inactive, and when it ends.
- **Logging:** Writes activity to `earn_your_time.log`.

## Requirements

- Python 3.8 or newer
- A desktop session with a display (pyautogui needs one)
- Python packages:
  - `psutil`
  - `plyer`
  - `pyautogui`

Install them with:

```bash
pip install psutil plyer pyautogui
```

## Setup

1. Place `game_list.json` in the same folder as the script. It should contain a JSON array of process names, for example:

```json
   ["JagexLauncher.exe", "Wow.exe", "ev.exe"]
```

2. If the file is missing, the script logs an error and falls back to the same three process names shown above.

## Usage

Run the script from a terminal:

```bash
python earn_your_time.py
```

When prompted, enter the work duration in minutes (decimals are allowed, e.g. `25` or `0.5`). The script then:

1. Sends a "Work started" notification.
2. Checks every 5 seconds whether the mouse has moved and kills any listed game processes.
3. Sends a "Focus session completed" notification when time is up, at which point you can play games again.

Stop the script early with `Ctrl+C`.

## How it works

| Function | Purpose |
|---|---|
| `is_user_active()` | Returns `True` if the mouse is not at position `(0, 0)`. |
| `send_notification()` | Shows a desktop notification via plyer. |
| `load_game_list()` | Reads `game_list.json`, or returns the default list if it's missing. |
| `block_games()` | Iterates over running processes and kills any whose name matches the game list. |
| `track_work_time()` | Runs the session loop: checks activity, blocks games, and extends the end time when inactive. |

## Logging

Events are written to `earn_your_time.log` in the format:
