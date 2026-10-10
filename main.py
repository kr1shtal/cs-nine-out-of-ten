import os
import time

import cv2
import mss
import numpy as np
import pydirectinput

LOWER_GREEN = np.array([40, 50, 50])
UPPER_GREEN = np.array([85, 255, 255])
SCAN_WIDTH = 400
SCAN_HEIGHT = 200


def auto_accept():
    print("Waiting for a match...")

    with mss.MSS() as sct:
        monitor = sct.monitors[1]
        screen_w = monitor["width"]
        screen_h = monitor["height"]

        region = {
            "top": (screen_h // 2) - (SCAN_HEIGHT // 2),
            "left": (screen_w // 2) - (SCAN_WIDTH // 2),
            "width": SCAN_WIDTH,
            "height": SCAN_HEIGHT,
        }

        while True:
            screenshot = sct.grab(region)
            img = np.array(screenshot)
            bgr_img = img[:, :, :3]

            hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_img, LOWER_GREEN, UPPER_GREEN)
            green_pixels_count = cv2.countNonZero(mask)

            if green_pixels_count > 1000:
                print("Match Found!")

                pydirectinput.moveTo(screen_w // 2, screen_h // 2)

                pydirectinput.click()
                print("First try to accept")

                time.sleep(3)

                pydirectinput.click()
                print("Second try to accept")

                print("Shutting down...")
                os._exit(0)

            time.sleep(1)


if __name__ == "__main__":
    auto_accept()
