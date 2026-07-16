from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class MediaTable(QWidget):
    """
    Main media review table.

    This widget becomes the primary workspace of the application.

    Every row represents one media item (front/back pair).

    Future PRs will populate this table from the ingestion
    pipeline and later directly from D1.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    ##################################################################

    def build_ui(self):

        layout = QVBoxLayout(self)

        self.table = QTableWidget()

        ##############################################################
        # Columns
        ##############################################################

        columns = [
            "Front",
            "Back",
            "Storage Case",
            "GUID",
            "Status",
        ]

        self.table.setColumnCount(len(columns))
        self.table.setHorizontalHeaderLabels(columns)

        ##############################################################
        # Appearance
        ##############################################################

        self.table.setAlternatingRowColors(True)

        self.table.setSortingEnabled(False)

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.table.setEditTriggers(
            QAbstractItemView.DoubleClicked
            | QAbstractItemView.SelectedClicked
        )

        self.table.verticalHeader().setVisible(False)

        header = self.table.horizontalHeader()

        header.setStretchLastSection(True)

        header.setSectionResizeMode(
            QHeaderView.ResizeToContents
        )

        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 140)
        self.table.setColumnWidth(3, 260)

        layout.addWidget(self.table)

    ##################################################################

    def clear(self):

        self.table.setRowCount(0)

    ##################################################################

    def add_pair(
        self,
        pair_number,
        front_name,
        back_name,
        storage_case,
        guid="",
        status="Pending",
    ):

        row = self.table.rowCount()

        self.table.insertRow(row)

        #
        # Front
        #

        self.table.setItem(
            row,
            0,
            QTableWidgetItem(front_name),
        )

        #
        # Back
        #

        self.table.setItem(
            row,
            1,
            QTableWidgetItem(back_name),
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
        """
        Populate the table from the image pair list.

        pairs

        [
            (front_path, back_path),
            ...
        ]
        """

        self.clear()

        for i, pair in enumerate(
            pairs,
            start=1,
        ):

            self.add_pair(
                pair_number=i,
                front_name=pair[0].name,
                back_name=pair[1].name,
                storage_case=storage_case,
            )