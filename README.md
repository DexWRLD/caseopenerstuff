# Running the Python Script for Automating In-Game Actions

This guide provides step-by-step instructions on how to run a Python script for automating in-game actions on a NoxPlayer emulator. The script is designed to open in-game cases, check item rarity, and decide whether to save or sell the item.

## Prerequisites

Before you begin, make sure you have the following prerequisites:

1. **Python**: Ensure you have Python installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Required Python Packages**: You need to have several Python packages installed to run the script. You can install these packages using `pip`. Open your command prompt or terminal and run:

   `pip install opencv-python pyautogui pytesseract keyboard`

3. **Game Setup**: Ensure you have the NoxPlayer emulator running with the game open where you intend to use the script. Adjust the coordinates in the script to match the game's interface.

## Running the Script

Follow these steps to run the provided Python script:

### 1. Script and Images

- Place the Python script (`your_script_name.py`) in a directory on your computer. Additionally, you should have template images for different in-game elements such as rarity levels (`Pink.png`, `Red.png`, etc.). Make sure to place these images in the same directory as your script.

### 2. Modify Coordinates

- Review the script and adjust the screen coordinates and other constants in the script to match the layout of the game on your NoxPlayer emulator. Modify the following constants if necessary:

   - `OPEN_CASE_COORDS`: Coordinates for the "Open Case" button.
   - `SAVE_BUTTON_COORDS`: Coordinates for the "Save" button.
   - `SELL_BUTTON_COORDS`: Coordinates for the "Sell" button.
   - `GUN_NAME_COORDS`: Coordinates for the region where the gun name is displayed.
   - `RARITY_COORDS`: Coordinates for the region where the item rarity is displayed.
   - `VALUE_COORDS`: Coordinates for the region where the item's value is displayed.

### 3. Start the Script

- Open your command prompt or terminal, navigate to the directory where the script is located, and run the script using the following command:

   `python your_script_name.py`

### 4. Activate Game Window

- The script will attempt to activate the NoxPlayer game window with the title specified in `GAME_WINDOW_TITLE`. Ensure that NoxPlayer is running and the game is open when you run the script.

### 5. Execute Script

- Once the game window is activated, the script will begin its execution. The script will check if a skin is already open and decide whether to save or sell the item. If no skin is open, it will open a case and perform the same actions.

### 6. Stopping the Script

- To stop the script, press the 'q' key. This will trigger the hotkey to stop the script, and it will exit gracefully.

Please ensure that you have tested the script with the correct game coordinates and templates to ensure it works effectively with your specific game setup. You may need to adjust thresholds and coordinates based on your game's interface.
