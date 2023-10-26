import time
import cv2
import numpy as np
import pytesseract
import pyautogui
import keyboard
import re

# Constants
GAME_WINDOW_TITLE = "NoxPlayer"
OPEN_CASE_COORDS = (978, 765)
SAVE_BUTTON_COORDS = (1530, 875)
SELL_BUTTON_COORDS = (420, 865)
GUN_NAME_COORDS = (594, 127, 1394 - 594, 180 - 127)

# Define the screen coordinates for the region where rarity is displayed
RARITY_COORDS = (670, 210, 1287 - 670, 213 - 210)

# Define the screen coordinates for the region where the item value is displayed
VALUE_COORDS = (850, 814, 1106 - 850, 871 - 814)

def check_already_open():
    skin_open = check_initial_state()
    if skin_open:
        print("A skin is already open. Handling the initial state...")
        rarity_screenshot = capture_screen_at_coordinates(RARITY_COORDS)
        print("Captured rarity screenshot")
        rarity = item_rarity(rarity_screenshot)
        print(f"Item rarity: {rarity}\n")

        if rarity in ['Pink', 'Red', 'Yellow'] or item_value() > 20:
            gun_name_screenshot = capture_screen_at_coordinates(GUN_NAME_COORDS)
            gun_name = extract_text(gun_name_screenshot)
            print(f"Gun Name: {gun_name}")
            tap_location(*SAVE_BUTTON_COORDS)
        else:
            print("Selling the item...")
            tap_location(*SELL_BUTTON_COORDS)

    else:
        print("No skin is open. Starting the script...")
        tap_location(*OPEN_CASE_COORDS)
        print("Opening case...")
        time.sleep(6)
        print("Case opened!")

        rarity_screenshot = capture_screen_at_coordinates(RARITY_COORDS)
        print("Captured rarity screenshot")
        rarity = item_rarity(rarity_screenshot)
        print(f"Item rarity: {rarity}\n")

        if rarity in ['Pink', 'Red', 'Yellow'] or item_value() > 20:
            gun_name_screenshot = capture_screen_at_coordinates(GUN_NAME_COORDS)
            gun_name = extract_text(gun_name_screenshot)
            print(f"Gun Name: {gun_name}")
            tap_location(*SAVE_BUTTON_COORDS)
        else:
            print("Selling the item...")
            tap_location(*SELL_BUTTON_COORDS)

def activate_game_window(window_title):
    """Activate the game window by its title."""
    try:
        window = pyautogui.getWindowsWithTitle(window_title)
        if window:
            window[0].activate()
            print(f"Activated window: {window_title}\n")
        else:
            print(f"Window not found: {window_title}\n")
    except Exception as e:
        print(f"Error activating the window: {str(e)}\n")

def tap_location(x, y):
    """Simulate a mouse click at the specified screen coordinates."""
    pyautogui.click(x, y)

def extract_text(screenshot):
    """Extract text from a screenshot using Pytesseract."""
    extracted_text = pytesseract.image_to_string(screenshot)
    return extracted_text

def capture_screen_at_coordinates(coords):
    """Capture a screenshot at specific screen coordinates using PyAutoGUI."""
    x, y, width, height = coords
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def open_case():
    print("No skin is open. Starting the script...")
    tap_location(*OPEN_CASE_COORDS)
    print("Opening case...")
    time.sleep(6)
    print("Case opened!")

    rarity_screenshot = capture_screen_at_coordinates(RARITY_COORDS)
    print("Captured rarity screenshot")
    rarity = item_rarity(rarity_screenshot)
    print(f"Item rarity: {rarity}\n")

    if rarity in ['Pink', 'Red', 'Yellow'] or item_value() > 20:
        gun_name_screenshot = capture_screen_at_coordinates(GUN_NAME_COORDS)
        gun_name = extract_text(gun_name_screenshot)
        print(f"Gun Name: {gun_name}")

        is_stattrak = "StatTrak" in gun_name
        if is_stattrak:
            print("Saving the StatTrak FN item...")
            tap_location(*SAVE_BUTTON_COORDS)
        else:
            print("Selling the item...")
            tap_location(*SELL_BUTTON_COORDS)
    else:
        print("Selling the item...")
        tap_location(*SELL_BUTTON_COORDS)

def item_rarity(screenshot):
    best_match_score = 0
    best_rarity = None

    # Load the template images and resize them to match the screenshot size
    templates = {
        'Pink': cv2.imread('images/Pink.png'),
        'Red': cv2.imread('images/Red.png'),
        'Blue': cv2.imread('images/Blue.png'),
        'Yellow': cv2.imread('images/Yellow.png'),
        'Purple': cv2.imread('images/Purple.png'),
        'Save': cv2.imread('images/Save.png'),
        'Sell': cv2.imread('images/Sell.png'),
        # Add more templates for other rarity levels
    }

    for rarity, template in templates.items():
        # Resize the template image to match the size of the screenshot
        template = cv2.resize(template, (screenshot.shape[1], screenshot.shape[0]))

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > best_match_score:
            best_match_score = max_val
            best_rarity = rarity

    return best_rarity

def item_value():
    """Extract the item's value from the screen using Pytesseract."""
    value_screenshot = capture_screen_at_coordinates(VALUE_COORDS)
    item_value_text = pytesseract.image_to_string(value_screenshot)
    print(f"Extracted item value text: {item_value_text}")

    item_values = re.findall(r'\d+\.\d+', item_value_text)

    if item_values:
        item_value = float(item_values[0])
        print(f"Item value: {item_value}")
    else:
        item_value = 0.0  # Default value
        print("\nNo item value found; using default value.")

    return item_value

def check_initial_state():
    """Check the initial state and return True if a save button is already present."""
    save_button_check_coords = (1335, 805, 1735 - 1335, 949 - 805)
    save_button_screenshot = capture_screen_at_coordinates(save_button_check_coords)
    save_button_template = cv2.imread('images/Save.png')
    result = cv2.matchTemplate(save_button_screenshot, save_button_template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    threshold = 0.8  # Adjust this threshold as needed
    if max_val >= threshold:
        print("\nSave button is already present.")
        rarity_screenshot = capture_screen_at_coordinates(RARITY_COORDS)
        print("Captured rarity screenshot.")
        rarity = item_rarity(rarity_screenshot)
        print(f"Item rarity: {rarity}\n")

        if rarity in ['Pink', 'Red', 'Yellow'] or item_value() > 20:
            print("\nSaving the item...")
            tap_location(*SAVE_BUTTON_COORDS)
        else:
            print("\nSelling the item...")
            tap_location(*SELL_BUTTON_COORDS)
        return True
    else:
        print("\nNo save button is present.")
        return False

def main():
    print('Checking if the app window is already open...')
    activate_game_window(GAME_WINDOW_TITLE)
    time.sleep(2)
    check_already_open()
    running = True

    def stop_script(e):
        nonlocal running
        running = False

    # Add a hotkey to stop the script when, for example, the 'q' key is pressed
    keyboard.on_press_key('q', stop_script)

    while running:
        time.sleep(2)
        open_case()

if __name__ == "__main__":
    main()
