from PySide6.QtWidgets import (
    QMainWindow,
    QStatusBar,
    QToolBar,
)

from gui.views.ingestion_view import IngestionView


class MainWindow(QMainWindow):
    """
    Main application window.

    During PR-007 we are hosting only the
    Media Ingestion page while the rest
    of the application is under development.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Collectible Authentication Platform")

        self.resize(1600, 900)

        self.build_toolbar()

        self.build_statusbar()

        self.build_central_widget()

    ##################################################################

    def build_toolbar(self):

        toolbar = QToolBar("Main Toolbar")

        toolbar.setMovable(False)

        self.addToolBar(toolbar)

    ##################################################################

    def build_statusbar(self):

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

    ##################################################################

    def build_central_widget(self):

        self.ingestion = IngestionView()

        self.setCentralWidget(self.ingestion)