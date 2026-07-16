from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])

button = QPushButton("Browse...")
button.resize(200, 60)
button.show()

app.exec()