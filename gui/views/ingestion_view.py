from PySide6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from gui.services.ingestion_service import IngestionService
from gui.widgets.media_table import MediaTable
from gui.widgets.statistics_widget import StatisticsWidget
from gui.widgets.toolbar_widget import IngestionToolbar


class IngestionView(QWidget):
    """
    Media Ingestion Workspace

    Responsibilities
    ----------------
    • Select folder
    • Scan folder
    • Pair images
    • Display statistics
    • Display review table

    Future PRs
    ----------
    • Thumbnail generation
    • Image preview
    • GUID generation
    • OpenAI metadata
    • Cloudflare upload
    • Database persistence
    """

    ##################################################################

    def __init__(self):
        super().__init__()

        self.service = IngestionService()

        self.build_ui()

        self.connect_signals()

    ##################################################################

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)

        layout.setSpacing(15)

        #
        # Toolbar
        #

        self.toolbar = IngestionToolbar()

        self.toolbar.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed,
        )

        layout.addWidget(self.toolbar)

        #
        # Statistics
        #

        self.statistics = StatisticsWidget()

        layout.addWidget(self.statistics)

        #
        # Review Table
        #

        self.media_table = MediaTable()

        self.media_table.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding,
        )

        layout.addWidget(self.media_table)

    ##################################################################

    def connect_signals(self):

        self.toolbar.scan.clicked.connect(
            self.scan_folder
        )

        self.toolbar.refresh.clicked.connect(
            self.refresh_folder
        )

    ##################################################################

    def scan_folder(self):

        folder = self.toolbar.folder.text()

        storage_case = self.toolbar.case.text()

        result = self.service.scan(folder)

        #
        # Update statistics
        #

        self.statistics.update_statistics(

            image_count=result["image_count"],

            pair_count=result["pair_count"],

            unpaired=result["unpaired"],

            pending=result["pair_count"],

            completed=0,

        )

        #
        # Populate review table
        #

        self.media_table.load_pairs(

            result["pairs"],

            storage_case,

        )

        #
        # Console output
        #

        print()

        print("=" * 70)

        print("SCAN COMPLETE")

        print("=" * 70)

        print(f"Folder      : {folder}")

        print(f"Images      : {result['image_count']}")

        print(f"Pairs       : {result['pair_count']}")

        print(f"Unpaired    : {result['unpaired']}")

        print("=" * 70)

        print()

    ##################################################################

    def refresh_folder(self):

        self.scan_folder()