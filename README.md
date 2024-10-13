# Alert System Project

This project features an alert system that signals different operational statuses using an Arduino Uno. The system communicates through LEDs, an LCD, a buzzer, and a Python-based GUI developed with Tkinter. It dynamically displays the current status and updates in real-time based on inputs from the Arduino.

## Project Overview

The alert system includes three operational statuses:
- **Normal**: Indicated by a green LED and shown on the LCD and GUI.
- **Attention Needed**: Triggered by a button, signaled with a blue LED, and displayed as an alert on the LCD and GUI.
- **Critical Error**: Triggered by another button, signaled with a red LED, and displayed as a critical message on both the LCD and GUI.

The Python GUI interacts with the Arduino via serial communication, displaying the system status and updating dynamically as inputs change.

### Features:
- **Real-Time Status Updates**: System statuses are reflected on both the LCD and the GUI interface.
- **Multi-Mode Alerts**: Visual (LED), auditory (buzzer), and on-screen (LCD and GUI) signals for different status modes.
  
## Project Structure

The project is organized into the following components:
- `Alert_system_project.ino` - Arduino sketch controlling the LED, buzzer, and LCD.
- `Alert_system_GUI.py` - Python script for the Tkinter-based GUI that communicates with the Arduino.
- `Circuit_diagram.png` - Circuit diagram showing the wiring for the Arduino, LCD, LEDs, and buttons.
- `Setup_picture.png` - Picture of the hardware setup for guidance.

## Hardware Requirements

- Arduino Uno (or compatible board)
- 16x2 LCD
- Potentiometer
- 3x 220Ω Resistors
- LEDs (Green, Blue, Red)
- Buzzer
- Push Buttons
- Jumper Wires
- Breadboard
- USB Cable

## Software Requirements

- [Arduino IDE](https://www.arduino.cc/en/software) (for uploading the Arduino code)
- [Python](https://www.python.org/downloads/) (for running the GUI)
- `pyserial` and `tkinter` Python libraries

## Setup Instructions

1. **Hardware Setup:**
   - Connect the LEDs, buzzer, potentiometer, resistors, and LCD to the Arduino following the schematic in `Circuit_diagram.png`.
   
2. **Arduino Code:**
   - Open `Alert_system.ino` in the Arduino IDE, select the correct board and port, and upload the code to your Arduino.

3. **Python GUI Setup:**
   - Install the required Python libraries by running:
     ```bash
     pip install pyserial tkinter
     ```
   - Run the `Alert_system_GUI.py` script to start the GUI interface.

4. **Run the System:**
   - With both the Arduino and Python GUI running, you will see the system status dynamically displayed on the LCD and GUI.

## Future Improvements

- Add more status modes for additional alert levels.
- Implement a wireless communication option to eliminate the need for a direct connection between the Arduino and computer.
- Enhance the GUI with more advanced features like logging status changes.

## Author

Created by **Helina Semu**.
