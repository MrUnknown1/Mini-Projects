import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    """A simple digital clock with a custom font and real-time updates."""

    def __init__(self):
        """Initialize the digital clock application."""
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Sets up the UI layout, styling, and starts the timer."""
        self.setWindowTitle("Digital Clock")  # Set window title
        self.setGeometry(550, 400, 500, 200)  # Set window size and position

        # Create a vertical layout and add the time label
        layout = QVBoxLayout(self)
        self.time_label = QLabel(alignment=Qt.AlignCenter)  # Center align the label
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        # Apply general styles
        self.setStyleSheet("background-color: #171616;")  # Dark background
        self.time_label.setStyleSheet("font-size: 200px; color: #7da5d4;")  # Font styling

        # Set the font (custom or fallback)
        self.set_custom_font()

        # Set up a timer to update the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)  # Connect timer to update function
        self.timer.start(1000)  # Trigger every 1000ms (1 second)

        self.update_time()  # Display the time immediately on startup

    def set_custom_font(self):
        """Attempts to load a custom font; falls back to a system font if loading fails."""
        font_path = "DS-DIGI.TTF"  # Path to the digital clock font
        font_id = QFontDatabase.addApplicationFont(font_path)  # Load font

        if font_id != -1:  # Check if the font loaded successfully
            font_families = QFontDatabase.applicationFontFamilies(font_id)  # Get font families
            if font_families:  # Ensure the list isn't empty
                font_family = font_families[0]  # Use the first available font
                self.time_label.setFont(QFont(font_family, 150))  # Apply font with size
            else:
                print("Warning: No font families found, using default font.")
                self.time_label.setFont(QFont("Arial", 150))  # Fallback font
        else:
            print(f"Warning: Failed to load font '{font_path}', using default font.")
            self.time_label.setFont(QFont("Arial", 150))  # Fallback to system font

    def update_time(self):
        """Updates the displayed time every second."""
        self.time_label.setText(QTime.currentTime().toString("hh:mm:ss AP"))

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    clock = DigitalClock()  # Create the clock window
    clock.show()  # Display the clock
    sys.exit(app.exec_())  # Start the event loop
