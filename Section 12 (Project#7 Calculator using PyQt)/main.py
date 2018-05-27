import sys
from PyQt5.QtWidgets import *

# Customized Button class
class Button():
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handle_input(self.text))  # if button is clicked, calling function

    # handling which button is clicked for different functionality
    def handle_input(self, value):
        if value is "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif value is "AC":
            self.results.setText("")
        elif value is "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        elif value is "%":
            current_value = self.results.text()
            v = float(current_value)/100
            self.results.setText(str(v))
        else:
            current_value = self.results.text()
            new_value = current_value + str(value)
            self.results.setText(new_value)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # initializing the parent class
        self.setWindowTitle("PyCalculator 1.0")  # setting the window title
        self.create_app()

    # initializes all the layout, widgets and show
    def create_app(self):
        # creating layouts, buttons and other widgets
        grid_layout = QGridLayout()
        display = QLineEdit()

        # buttons we need
        buttons = ["AC", "DEL", "%", "/",
                   7,8,9, "*",
                   4,5,6, "-",
                   1,2,3, "+",
                   0, ".", "="]
        row = 0
        column = 0

        # adding the display at the top of the grid layout
        # grid_layout.addWidget(object, row number, column number, row spacing, column spacing)
        grid_layout.addWidget(display, row, column, 1, 4)

        row += 1

        # adding all the buttons to the grid layout
        for button in buttons:
            if column > 3:  # setting three columns (buttons) per row
                column = 0
                row +=1

            # instantiating the custom button class
            buttonobject = Button(button, display)

            # creating each button
            if button is 0:
                grid_layout.addWidget(buttonobject.b, row, column, 1, 2)
                column += 1
            else:
                grid_layout.addWidget(buttonobject.b, row, column,1,1)
            column += 1

        # setting the layout in the window
        self.setLayout(grid_layout)
        # showing the window
        self.show()


# starting the QApplication from main.py
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

