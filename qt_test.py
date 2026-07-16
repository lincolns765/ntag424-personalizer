import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Qt Test")
window.resize(400, 200)

layout = QVBoxLayout(window)

label = QLabel("Hello World")
button = QPushButton("Browse...")

layout.addWidget(label)
layout.addWidget(button)

window.show()

sys.exit(app.exec())