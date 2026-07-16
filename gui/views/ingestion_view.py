from PySide6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from gui.services.ingestion_service import IngestionService
from gui.widgets.toolbar_widget import IngestionToolbar
from gui.widgets.statistics_widget import StatisticsWidget
from gui.widgets.media_table import MediaTable


class IngestionView(QWidget):
    """
    Media Ingestion Workspace

    Responsibilities

    • Select folder
    • Scan images
    • Pair images
    • Display statistics
    • Display media table

    Future PRs

    • GUID generation
    • Thumbnail generation
    • OpenAI processing
    • Upload to R2
    • Save to D1
    """

    def __init__(self):
        super().__init__()

        #
        # Services
        #

        self.service = IngestionService()

        #
        # UI
        #

        self.build_ui()

        #
        # Signals
        #

        self.toolbar.scan.clicked.connect(
            self.scan_folder
        )

        self.toolbar.refresh.clicked.connect(
            self.refresh_folder
        )

    ##################################################################

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)

        layout.setSpacing(15)

        ###############################################################
        # Toolbar
        ###############################################################

        self.toolbar = IngestionToolbar()

        self.toolbar.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed,
        )

        layout.addWidget(self.toolbar)

        ###############################################################
        # Statistics
        ###############################################################

        self.statistics = StatisticsWidget()

        layout.addWidget(self.statistics)

        ###############################################################
        # Media Table
        ###############################################################

        self.media_table = MediaTable()

        self.media_table.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding,
        )

        layout.addWidget(self.media_table)

    ##################################################################

    def scan_folder(self):

        print()

        print("=" * 70)

        print("Scanning Folder")

        print("=" * 70)

        result = self.service.scan(
            self.toolbar.folder.text()
        )

        ###############################################################
        # Update statistics
        ###############################################################

        self.statistics.update_statistics(

            image_count=result["image_count"],

            pair_count=result["pair_count"],

            unpaired=result["unpaired"],

            pending=result["pair_count"],

            completed=0,

        )

        ###############################################################
        # Populate table
        ###############################################################

        self.media_table.load_pairs(

            result["pairs"],

            self.toolbar.case.text(),

        )

        print(f'Images Found : {result["image_count"]}')

        print(f'Pairs Found  : {result["pair_count"]}')

        print(f'Unpaired     : {result["unpaired"]}')

        print("=" * 70)

        print()

    ##################################################################

    def refresh_folder(self):

        self.scan_folder()