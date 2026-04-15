import requests

MOVE_URL = 'http://192.168.50.241:5000/move'

print("Control your robot with WASD keys. Press ESC to stop and exit.")

while True:
    key = input("Enter command (w/a/s/d/stop): ").lower()

    if key in ['w', 'a', 's', 'd', 'stop']:
        try:
            requests.post(MOVE_URL, data={'cmd': key})
            print(f"Sent command: {key}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending command: {e}")
    elif key == 'esc':
        requests.post(MOVE_URL, data={'cmd': 'stop'})
        print("Stopping robot. Exiting.")
        break
    else:
        print("Invalid command. Use w/a/s/d/stop.")