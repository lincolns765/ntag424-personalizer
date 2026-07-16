from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QStatusBar,
    QToolBar,
    QWidget,
)

from ..widgets.navigation import Navigation
from ..views.dashboard_view import DashboardView
from ..views.ingestion_view import IngestionView


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Collectible Authentication Platform")
        self.resize(1600, 900)

        self.build_toolbar()
        self.build_statusbar()
        self.build_ui()

    def build_toolbar(self):

        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

    def build_statusbar(self):

        status = QStatusBar()
        status.showMessage("Ready")
        self.setStatusBar(status)

    def build_ui(self):

        root = QWidget()

        layout = QHBoxLayout(root)

        #
        # Navigation
        #

        self.navigation = Navigation()
        layout.addWidget(self.navigation)

        #
        # Pages
        #

        self.pages = QStackedWidget()

        self.dashboard = DashboardView()
        self.ingestion = IngestionView()

        self.pages.addWidget(self.dashboard)
        self.pages.addWidget(self.ingestion)

        layout.addWidget(self.pages, 1)

        self.setCentralWidget(root)

        #
        # Signals
        #

        self.navigation.currentRowChanged.connect(self.change_page)

    def change_page(self, index):

        if index == 0:
            self.pages.setCurrentWidget(self.dashboard)

        elif index == 1:
            self.pages.setCurrentWidget(self.ingestion)

        else:
            self.pages.setCurrentWidget(self.dashboard)