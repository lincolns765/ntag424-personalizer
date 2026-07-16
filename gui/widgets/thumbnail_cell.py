from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class ThumbnailCell(QWidget):
    """
    Widget displayed inside a MediaTable cell.

    Displays

        Thumbnail
        Filename

    The thumbnail image is expected to already exist.
    """

    ##################################################################

    def __init__(
        self,
        thumbnail_path,
        filename,
    ):
        super().__init__()

        self.thumbnail_path = Path(thumbnail_path)
        self.filename = filename

        self.build_ui()

    ##################################################################

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(6, 6, 6, 6)
        layout.setSpacing(6)

        #
        # Thumbnail
        #

        self.image = QLabel()

        self.image.setAlignment(Qt.AlignCenter)

        self.image.setMinimumSize(150, 150)
        self.image.setMaximumSize(150, 150)

        if self.thumbnail_path.exists():

            pixmap = QPixmap(str(self.thumbnail_path))

            pixmap = pixmap.scaled(
                150,
                150,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

            self.image.setPixmap(pixmap)

        else:

            self.image.setText("No Preview")

        #
        # Filename
        #

        self.filename_label = QLabel(self.filename)

        self.filename_label.setAlignment(Qt.AlignCenter)

        self.filename_label.setWordWrap(True)

        #
        # Layout
        #

        layout.addWidget(self.image)

        layout.addWidget(self.filename_label)

    ##################################################################

    def update_thumbnail(
        self,
        thumbnail_path,
    ):
        """
        Replace the displayed thumbnail.
        """

        self.thumbnail_path = Path(thumbnail_path)

        if self.thumbnail_path.exists():

            pixmap = QPixmap(str(self.thumbnail_path))

            pixmap = pixmap.scaled(
                150,
                150,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

            self.image.setPixmap(pixmap)

        else:

            self.image.clear()

            self.image.setText("No Preview")