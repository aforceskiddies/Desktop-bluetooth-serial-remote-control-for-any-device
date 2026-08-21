 Scorpion Arm Bluetooth Remote Control

A web-based Bluetooth remote control interface for controlling a Scorpion Arm robot arm via serial/Bluetooth connection.

## Overview

This project provides a web-based remote control interface for operating a Scorpion Arm robotic arm. The interface communicates with the robot via Bluetooth Serial API (or Web Serial API for compatible browsers) at 9600 baud rate, sending single-character commands for movement and operations.

## Features

- **Directional Control**: D-pad for Forward/Back/Left/Right movement
- **Operation Controls**: CODE buttons (C, O, D, E) for specific arm functions
- **Connection Management**: Scan, connect, and disconnect from Bluetooth/serial devices
- **Visual Feedback**: Connection status indicator, command logging, and visual button feedback
- **Responsive Design**: Works on desktop and mobile browsers
- **Keyboard Support**: Keyboard arrow keys and C/O/D/E keys for control
- **Touch Support**: Optimized for touchscreen devices

## Files in Repository

- `index.html` - Main HTML file containing the user interface and JavaScript logic
- `serve.py` - Simple Python HTTP server for local testing
- `README.txt` - This file

## How to Use

### 1. Local Setup

1. Clone or download this repository to your local machine
2. Ensure you have Python installed (for the local server)
3. Start the local server:
   ```
   python serve.py
   ```
4. Open your browser and navigate to `http://localhost:8000`

### 2. Connecting to Your Scorpion Arm

1. Click the Bluetooth icon (📶) in the status bar to open the port scanner
2. Click "Request Port" to scan for available Bluetooth/serial devices
3. Select your Scorpion Arm device from the list
4. Click "Connect" to establish the connection
5. The connection label will change from "Not connected" to "Connected" when successful

### 3. Controlling the Robot Arm

#### D-Pad Controls:
- **↑ (Up/Forward)**: Press and hold to move forward (sends 'F' on press, 'S' on release)
- **↓ (Down/Back)**: Press and hold to move backward (sends 'B' on press, 'S' on release)
- **← (Left)**: Press and hold to move left (sends 'L' on press, 'S' on release)
- **→ (Right)**: Press and hold to move right (sends 'R' on press, 'S' on release)

#### CODE Buttons:
- **C**: Send 'C' on press, 'c' on release
- **O**: Send 'O' on press, 'o' on release
- **D**: Send 'D' on press, 'd' on release
- **E**: Send 'E' on press, 'e' on release

#### Keyboard Controls:
- Arrow Keys: Same functions as D-pad
- C, O, D, E keys: Same functions as CODE buttons

### 4. Monitoring Communication

The serial log at the bottom of the screen displays:
- **Timestamp** for each communication
- **Sent commands** in blue (prefixed with ▶)
- **Received data** in green (prefixed with ◀)
- **Information messages** in orange (prefixed with ℹ)
- **Error messages** in red (prefixed with ✖)

Click the "Clear Log" button to clear the communication log.

### 5. Additional Features

- **Info Button** (ℹ️): Shows/hides a modal with command reference
- **Visual Feedback**: Buttons change appearance when pressed/active
- **Hover Effects**: Buttons change border color on hover
- **Connection Status**: Bluetooth icon changes color when connected (green) vs disconnected (gray)

## Technical Details

### Communication Protocol
- **Baud Rate**: 9600
- **Data Format**: Single ASCII characters
- **Command Structure**:
  - Movement commands: Sent on press, release sends 'S' (stop)
  - CODE commands: Sent on press, release sends lowercase version
- **Data Direction**: Browser → Device (commands only in current implementation)

### Browser Requirements
- Modern browser with Web Serial API support (Chrome, Edge, Opera)
- HTTPS or localhost (required for Web Serial API)
- Bluetooth permissions granted to the browser/site

### Implementation Notes
- Pure HTML/CSS/JavaScript - no external frameworks/libraries
- Uses Web Serial API for browser-based serial communication
- Responsive design using CSS Flexbox and Grid
- Event listeners for mouse, touch, and keyboard input
- Visual feedback for button states (pressed, hovered, active)

## Troubleshooting

### Connection Issues
1. Ensure your Scorpion Arm is powered on and in pairing mode
2. Make sure Bluetooth is enabled on your computer
3. Try refreshing the page and requesting port access again
4. Some systems may require pairing the device at the OS level first

### No Response from Robot
1. Verify the connection status shows "Connected"
2. Check the serial log for sent commands (should appear in blue)
3. Ensure your robot is programmed to expect the same command set
4. Try restarting both the robot and the browser

### Performance Issues
- Close other browser tabs that might be using Bluetooth
- Ensure no other applications are connected to the same Bluetooth device
- Try a different browser if problems persist

## Customization

### Changing Commands
Edit the `btns` object in the JavaScript section to modify what characters are sent for each button.

### Adjusting Appearance
Modify the CSS variables in the `<style>` section to change colors, sizes, and spacing.

### Adding New Controls
1. Add button elements to the HTML in the appropriate container
2. Add corresponding entries to the `btns` object in JavaScript
3. Add keyboard mappings to the `keyMap` object if desired
4. Style new buttons using existing CSS classes or add new ones

## Development

To modify this interface:

1. Edit `index.html` to change the UI or functionality
2. Test changes locally using `python serve.py`
3. Ensure browser security permissions are granted for Web Serial API
4. Test with your actual Scorpion Arm hardware

## Server Script (`serve.py`)

A simple Python HTTP server for local testing:
- Serves files from the current directory
- Runs on port 8000 by default
- Provides proper MIME types for web files
- Required for Web Serial API (which needs HTTPS or localhost)

## Safety Notes

⚠️ **Important**: Always test robot movements in a safe, clear area first
⚠️ **Important**: Ensure emergency stop mechanisms are functional
⚠️ **Important**: Verify command mappings match your robot's firmware expectations

## License

This project is provided as-is for educational and hobbyist use. Please ensure you have the right to modify and use this software with your specific hardware.

---

*Scorpion Arm Bluetooth Remote Control - Built with HTML, CSS, and JavaScript*
*For use with Scorpion Arm robotic arms via Bluetooth Serial connection*
