
# LCD Control Using PyQt6 & GPIO on Raspberry Pi 5

This project provides a GUI-based control system for switching high-frequency flexible LCD screens using Low Signal Relay DPDT NON-LATCHING 1A, 5VDC (TQ2-5V - ATQ209). The application is built with PyQt6 and utilizes GPIO Zero to control relays, enabling seamless switching between two LCDs on a Raspberry Pi 5.


## Features
✅ GUI Interface: PyQt6-based user-friendly interface for controlling LCD screens.

✅ Independent Control: Turn ON/OFF two separate LCD screens individually.

✅ Relay-Based Switching: Uses DPDT relays to switch between high-frequency LCDs.

✅ GPIO Control: Implements GPIO Zero for relay activation.

✅ Optimized for Raspberry Pi 5: Leverages enhanced GPIO performance on Pi 5.


## Hardware Requirements
1. Raspberry Pi 5
2. Low Signal Relay DPDT NON-LATCHING 1A, 5VDC (TQ2-5V - ATQ209)
3. High-Frequency Flexible LCD Screens (Wisecoco New Ultra Thin 6 Inch 2880*1440 Resolution Landscape By Default MIPI-DSI 4 Lanes Flexible Amoled Display Module)
4. Jumper wires 

## GPIO Pin Configuration (Raspberry Pi 5)

GPIO-Pin	      Function	            LCD Screen
5	        Relay Control 1	Left        LCD ON/OFF
6	        Relay Control 2	Left        LCD ON/OFF
24	        Relay Control 3	Right       LCD ON/OFF
23	        Relay Control 4	Right       LCD ON/OFF

## Installation

1. Install Dependencies

pip install PyQt6 gpiozero
pip install PyQt6
pip install lgpio 
 
2. Run the GUI

python lcd_control.py


## How It Works

Right LCD ON/OFF → Controls the right LCD
Left LCD ON/OFF → Controls the left LCD

## Author

🚀 Developed by Muhammad Yahya
🔧 Embedded Systems Engineer
