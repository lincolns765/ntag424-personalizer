import sys

from PySide6.QtWidgets import QApplication

import gui.windows.main_window as mw

print()
print("MainWindow imported from:")
print(mw.__file__)
print()

from gui.windows.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    app.setStyle("Fusion")

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()