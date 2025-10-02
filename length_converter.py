import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QVBoxLayout,QHBoxLayout,QPushButton,QComboBox,QLineEdit)
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Length Converter")
        self.setGeometry(400,500,800,400)
        self.converterUI()

    def converterUI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()

        self.heading = QLabel("📏 Length Converter")
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 30px; color: navy; margin: 20px; font-family: Segoe Script ;")
        main_layout.addWidget(self.heading)

        self.input_label = QLineEdit(self)
        self.input_label.setPlaceholderText("Enter length")
        self.input_label.setFixedHeight(50)
        self.input_label.setStyleSheet("font-size: 30px; font-family: Arial;")
        self.input_label.returnPressed.connect(self.convert)
        main_layout.addWidget(self.input_label)

        dropdown_layout = QHBoxLayout()
        self.from_unit = QComboBox()
        self.to_unit = QComboBox()

        units = ["kilometre","metre","centimetre","millimetre","micrometre","nanometre","mile","yard","foot","inch","nautical mile"]
        self.from_unit.addItems(units)
        self.to_unit.addItems(units)
        self.from_unit.setCurrentText(units[1])
        self.to_unit.setCurrentText(units[2])

        self.symbol = QLabel("🟰")
        self.symbol.setAlignment(Qt.AlignCenter)
        self.symbol.setStyleSheet("font-size: 30px; margin: 0px 10px;")


        self.setStyleSheet("""
            QComboBox{
                    font-size: 30px;
                    margin: 20px 5px;
                    font-family: Comic Sans MS;
                }
        """)

        dropdown_layout.setSpacing(10)
        dropdown_layout.addWidget(self.from_unit)
        dropdown_layout.addWidget(self.symbol)
        dropdown_layout.addWidget(self.to_unit)
        main_layout.addLayout(dropdown_layout)

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setStyleSheet("""
                font-size: 40px; 
                padding: 10px;
                font-weight: bold; 
                font-family: Goudy Old Style;
                border: transparent;
                background-color: hsl(29, 98%, 50%);
                color: white;
                border-radius: 10px; 
            """)
        self.convert_btn.clicked.connect(self.convert)
        main_layout.addWidget(self.convert_btn)

        self.result_label = QLabel(self)
        self.result_label.setStyleSheet("""
                font-size: 30px;
                font-family: Comic Sans MS;
                font-weight: bold;
                margin: 30px 20px;
            """)
        main_layout.addWidget(self.result_label)

    
        self.unit_to_meter = {
                            "kilometre": 1000,
                            "metre": 1,
                            "centimetre": 0.01,
                            "millimetre": 0.001,
                            "micrometre": 1e-6,
                            "nanometre": 1e-9,
                            "mile": 1609.344,
                            "yard": 0.9144,
                            "foot": 0.3048,
                            "inch": 0.0254,
                            "nautical mile": 1852
                        }


        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def convert(self):
        try:
            value = float(self.input_label.text())
            from_unit = self.from_unit.currentText()
            to_unit = self.to_unit.currentText()

            # Convert to meters
            value_in_meters = value * self.unit_to_meter[from_unit]
            # Convert to target unit
            result = value_in_meters / self.unit_to_meter[to_unit]

            self.result_label.setText(f"Result: {value} {from_unit} = {result:.6f} {to_unit}")
        except ValueError:
            self.result_label.setText("⚠️ Please enter a valid number")

        
        

def main():
    app = QApplication(sys.argv)
    my_window = Window()
    my_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

