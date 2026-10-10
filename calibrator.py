import time

import mouse

print("Launch cs and move cursor in place where button 'ACCEPT' should be displayed.")
print("Coords updating every second. Press Ctrl+C in console to stop script.")

try:
    while True:
        x, y = mouse.get_position()
        print(f"Coords -> X: {x} | Y: {y}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDone!")
