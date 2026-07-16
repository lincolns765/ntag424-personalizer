from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class StatisticsWidget(QFrame):
    """
    Displays ingestion statistics.

    Updated after every scan.

    Images
    Pairs
    Unpaired
    Pending
    Completed
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    ##################################################################

    def build_ui(self):

        self.setFrameShape(QFrame.StyledPanel)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed,
        )

        layout = QVBoxLayout(self)

        title = QLabel("Scan Statistics")

        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        grid = QGridLayout()

        layout.addLayout(grid)

        #
        # Images
        #

        grid.addWidget(QLabel("Images Found"), 0, 0)

        self.images = QLabel("0")

        self.images.setAlignment(Qt.AlignRight)

        grid.addWidget(self.images, 0, 1)

        #
        # Pairs
        #

        grid.addWidget(QLabel("Pairs Found"), 0, 2)

        self.pairs = QLabel("0")

        self.pairs.setAlignment(Qt.AlignRight)

        grid.addWidget(self.pairs, 0, 3)

        #
        # Unpaired
        #

        grid.addWidget(QLabel("Unpaired"), 1, 0)

        self.unpaired = QLabel("0")

        self.unpaired.setAlignment(Qt.AlignRight)

        grid.addWidget(self.unpaired, 1, 1)

        #
        # Pending
        #

        grid.addWidget(QLabel("Pending"), 1, 2)

        self.pending = QLabel("0")

        self.pending.setAlignment(Qt.AlignRight)

        grid.addWidget(self.pending, 1, 3)

        #
        # Completed
        #

        grid.addWidget(QLabel("Completed"), 2, 0)

        self.completed = QLabel("0")

        self.completed.setAlignment(Qt.AlignRight)

        grid.addWidget(self.completed, 2, 1)

        grid.setColumnStretch(4, 1)

    ##################################################################

    def update_statistics(
        self,
        image_count,
        pair_count,
        unpaired,
        pending,
        completed,
    ):

        self.images.setText(str(image_count))

        self.pairs.setText(str(pair_count))

        self.unpaired.setText(str(unpaired))

        self.pending.setText(str(pending))

        self.completed.setText(str(completed))