from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from config.settings import (
    DEFAULT_STORAGE_CASE,
    INCOMING_FOLDER,
)


class IngestionToolbar(QWidget):
    """
    Top toolbar for the Media Workbench.

    Responsibilities

    • Folder selection
    • Storage case
    • Scan
    • Refresh

    No processing occurs here.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    #####################################################################

    def build_ui(self):

        root = QVBoxLayout(self)

        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(10)

        ##############################################################
        # Folder Row
        ##############################################################

        folder_row = QHBoxLayout()

        folder_label = QLabel("Folder")

        folder_label.setFixedWidth(90)

        self.folder = QLineEdit(str(INCOMING_FOLDER))

        self.browse = QPushButton("Browse")

        self.browse.clicked.connect(
            self.select_folder
        )

        folder_row.addWidget(folder_label)

        folder_row.addWidget(self.folder, 1)

        folder_row.addWidget(self.browse)

        root.addLayout(folder_row)

        ##############################################################
        # Storage Row
        ##############################################################

        storage_row = QHBoxLayout()

        storage_label = QLabel("Storage Case")

        storage_label.setFixedWidth(90)

        self.case = QLineEdit(DEFAULT_STORAGE_CASE)

        self.case.setMaximumWidth(200)

        storage_row.addWidget(storage_label)

        storage_row.addWidget(self.case)

        storage_row.addStretch()

        root.addLayout(storage_row)

        ##############################################################
        # Buttons
        ##############################################################

        buttons = QHBoxLayout()

        self.scan = QPushButton("Scan Folder")

        self.refresh = QPushButton("Refresh")

        self.scan.setFixedSize(150, 38)

        self.refresh.setFixedSize(120, 38)

        buttons.addWidget(self.scan)

        buttons.addWidget(self.refresh)

        buttons.addStretch()

        root.addLayout(buttons)

        ##############################################################
        # Divider
        ##############################################################

        line = QFrame()

        line.setFrameShape(QFrame.HLine)

        root.addWidget(line)

    #####################################################################

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Image Folder",
            self.folder.text(),
        )

        if folder:

            self.folder.setText(folder)