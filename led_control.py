from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from gpiozero import LED
import sys

# GPIO setup for MOSFETs controlling two LCDs
mosfet1 = LED(5)  # GPIO 5 controls MOSFET for Left LCD (LCD 1)
mosfet2 = LED(6)  # GPIO 6 controls MOSFET for Left LCD (LCD 1)
mosfet3 = LED(24)  # GPIO 22 controls MOSFET for Right LCD (LCD 2)
mosfet4 = LED(23)  # GPIO 27 controls MOSFET for Right LCD (LCD 2)

class LCDControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window title and geometry
        self.setWindowTitle("LCD Control")
        self.setGeometry(200, 200, 300, 200)

        # Label to display the current state
        self.label = QLabel("Select an LCD:", self)

        # Left button (ON)
        self.left_button_on = QPushButton("Right LCD ON", self)
        self.left_button_on.clicked.connect(self.activate_left_lcd_on)

        # Left button (OFF)
        self.left_button_off = QPushButton("Right LCD OFF", self)
        self.left_button_off.clicked.connect(self.activate_left_lcd_off)

        # Right button (ON)
        self.right_button_on = QPushButton("Left LCD ON", self)
        self.right_button_on.clicked.connect(self.activate_right_lcd_on)

        # Right button (OFF)
        self.right_button_off = QPushButton("Left LCD OFF", self)
        self.right_button_off.clicked.connect(self.activate_right_lcd_off)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.left_button_on)
        layout.addWidget(self.left_button_off)
        layout.addWidget(self.right_button_on)
        layout.addWidget(self.right_button_off)

        self.setLayout(layout)

    def activate_left_lcd_off(self):
        # Turn off both MOSFETs for Left LCD
        mosfet1.off()  # GPIO 5 (Left LCD)
        mosfet2.on()  # GPIO 6 (Left LCD)

        self.label.setText("State: Left LCD OFF")
        print("State: Left LCD OFF")

    def activate_left_lcd_on(self):
        # Turn on both MOSFETs for Left LCD
        mosfet1.on()   # GPIO 5 (Left LCD)
        mosfet2.off()   # GPIO 6 (Left LCD)

        self.label.setText("State: Left LCD ON")
        print("State: Left LCD ON")

    def activate_right_lcd_off(self):
        # Turn off both MOSFETs for Right LCD
        mosfet3.off()  # GPIO 22 (Right LCD)
        mosfet4.on()  # GPIO 27 (Right LCD)

        self.label.setText("State: Right LCD OFF")
        print("State: Right LCD OFF")

    def activate_right_lcd_on(self):
        # Turn on both MOSFETs for Right LCD
        mosfet3.on()   # GPIO 22 (Right LCD)
        mosfet4.off()   # GPIO 27 (Right LCD)

        self.label.setText("State: Right LCD ON")
        print("State: Right LCD ON")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LCDControlApp()
    window.show()
    sys.exit(app.exec())
