# Digital Clock (PyQt5)

A simple digital clock application built using **PyQt5**. It displays the current time with a stylish digital font and updates in real-time.

## Features
- 🕒 Displays the current time in **hh:mm:ss AP** format
- 🎨 Customizable **digital font** (DS-DIGI.TTF)
- ⏳ Updates every second using **QTimer**
- 🖥️ Simple and elegant **UI design** with a dark theme
- 🔄 **Fallback mechanism** in case the font file is missing

## Requirements
Make sure you have **Python 3.x** installed along with the required dependencies.

### Install Dependencies
```sh
pip install PyQt5
```

## How to Run
1. Copy the code:
2. Ensure the font file **DS-DIGI.TTF** is present in the project folder (or you can use your own .TTF file).
3. Run the script:
   ```sh
   python digital_clock.py
   ```

## File Structure
```
📂 digital-clock/
│-- 📄 digital_clock.py  # Main script
│-- 📄 README.md         # Project documentation
│-- 🎨 DS-DIGI.TTF       # Digital clock font
```

## Screenshots
![Digital Clock Screenshot](https://your-image-link.com/screenshot.png)  

## Troubleshooting
- **Font not loading?** Ensure `DS-DIGI.TTF` is in the same directory as `digital_clock.py`.
- **PyQt5 not found?** Install it using `pip install PyQt5`.

