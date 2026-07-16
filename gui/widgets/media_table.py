from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from gui.dialogs.image_preview_dialog import ImagePreviewDialog
from gui.services.thumbnail_service import ThumbnailService
from gui.widgets.thumbnail_cell import ThumbnailCell


class MediaTable(QWidget):
    """
    Main media review table.

    Displays every discovered image pair using
    thumbnail widgets.

    Double-clicking any row opens the original
    front/back images in a preview dialog.
    """

    ##################################################################

    def __init__(self):
        super().__init__()

        self.thumbnail_service = ThumbnailService()

        #
        # Keep the original image paths so the
        # preview dialog can display full-size images.
        #

        self.image_pairs = []

        self.build_ui()

    ##################################################################

    def build_ui(self):

        layout = QVBoxLayout(self)

        self.table = QTableWidget()

        columns = [
            "Front",
            "Back",
            "Storage Case",
            "GUID",
            "Status",
        ]

        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)

        self.table.setAlternatingRowColors(True)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        self.table.verticalHeader().setVisible(False)

        self.table.verticalHeader().setDefaultSectionSize(185)

        header = self.table.horizontalHeader()

        header.setStretchLastSection(False)

        header.setSectionResizeMode(
            QHeaderView.Interactive
        )

        self.table.setColumnWidth(0, 190)
        self.table.setColumnWidth(1, 190)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 260)
        self.table.setColumnWidth(4, 120)

        #
        # Double-click preview
        #

        self.table.cellDoubleClicked.connect(
            self.open_preview
        )

        layout.addWidget(self.table)

    ##################################################################

    def clear(self):

        self.table.setRowCount(0)

        self.image_pairs.clear()

    ##################################################################

    def add_pair(
        self,
        front_path,
        back_path,
        storage_case,
        guid="",
        status="Pending",
    ):

        row = self.table.rowCount()

        self.table.insertRow(row)

        #
        # Save original image paths
        #

        self.image_pairs.append(
            (
                front_path,
                back_path,
            )
        )

        #
        # Create or retrieve cached thumbnails
        #

        front_thumb, back_thumb = (
            self.thumbnail_service.ensure_pair(
                front_path,
                back_path,
            )
        )

        #
        # Front thumbnail
        #

        self.table.setCellWidget(
            row,
            0,
            ThumbnailCell(
                front_thumb,
                front_path.name,
            ),
        )

        #
        # Back thumbnail
        #

        self.table.setCellWidget(
            row,
            1,
            ThumbnailCell(
                back_thumb,
                back_path.name,
            ),
        )

        #
        # Storage Case
        #

        self.table.setItem(
            row,
            2,
            QTableWidgetItem(storage_case),
        )

        #
        # GUID
        #

        self.table.setItem(
            row,
            3,
            QTableWidgetItem(guid),
        )

        #
        # Status
        #

        status_item = QTableWidgetItem(status)

        if status == "Pending":

            status_item.setBackground(
                QColor(255, 245, 180)
            )

        elif status == "Completed":

            status_item.setBackground(
                QColor(190, 255, 190)
            )

        elif status == "Failed":

            status_item.setBackground(
                QColor(255, 190, 190)
            )

        self.table.setItem(
            row,
            4,
            status_item,
        )

    ##################################################################

    def load_pairs(
        self,
        pairs,
        storage_case,
    ):

        self.clear()

        for front, back in pairs:

            self.add_pair(
                front_path=front,
                back_path=back,
                storage_case=storage_case,
                guid="",
                status="Pending",
            )

    ##################################################################

    def open_preview(
        self,
        row,
        column,
    ):
        """
        Open the original images for the selected row.
        """

        if row >= len(self.image_pairs):

            return

        front_path, back_path = self.image_pairs[row]

        dialog = ImagePreviewDialog(
            front_path,
            back_path,
            self,
        )

        dialog.exec()