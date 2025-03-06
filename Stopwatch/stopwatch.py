import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    """A simple stopwatch application using PyQt5."""
    
    def __init__(self):
        """Initialize the stopwatch."""
        super().__init__()
        self.time = QTime(0, 0, 0, 0)  # Stopwatch time storage
        self.timer = QTimer(self)  # Timer to track elapsed time

        # Create UI elements
        self.time_label = QLabel("00:00:00.00", self)  # Displays time
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.init_ui()  # Setup UI

    def init_ui(self):
        """Set up the user interface."""
        self.setWindowTitle("Stopwatch")
        self.setFixedSize(600, 400)  # Set a fixed window size

        # Main vertical layout
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # Style & Align the time label
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label)

        # Horizontal layout for buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        # Apply styles
        self.set_styles()

        # Connect button events
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)  # Timer event

    def set_styles(self):
        """Apply styles to the stopwatch UI."""
        self.setStyleSheet("""
                           
            QPushButton, QLabel {
                font-family: Calibri;
                font-weight: bold;
                padding: 20px;
            }
                           
            QPushButton:hover {
                background-color: #1b1f29;
            }
            
            QPushButton {
                font-size: 30px;
                color: #2c899e;
                border-radius: 15px;
                background-color: #d1e1e3;
            }
                           
            QLabel {
                font-size: 100px;
                background-color: #c2f0e9;
                border-radius: 20px; 
                color: #003366;
            }
        """)

    def start(self):
        """Start the stopwatch."""
        self.timer.start(10)  # Update every 10ms

    def stop(self):
        """Stop the stopwatch."""
        self.timer.stop()

    def reset(self):
        """Reset the stopwatch to 00:00:00.00."""
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)  # Reset time
        self.time_label.setText("00:00:00.00")  # Update display

    def update_display(self):
        """Update the stopwatch time display."""
        self.time = self.time.addMSecs(10)  # Add 10 milliseconds
        self.time_label.setText(self.format_time(self.time))  # Update UI

    def format_time(self, time):
        """Format QTime object into HH:MM:SS.ms string."""
        return f"{time.hour():02}:{time.minute():02}:{time.second():02}.{time.msec() // 10:02}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())
