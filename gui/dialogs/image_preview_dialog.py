from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)


class ImagePreviewDialog(QDialog):
    """
    Displays the original front and back images.

    This dialog is opened by double-clicking a row
    in the Media Table.

    Images are scaled to fit while preserving
    aspect ratio.
    """

    ##################################################################

    def __init__(
        self,
        front_image,
        back_image,
        parent=None,
    ):
        super().__init__(parent)

        self.front_image = Path(front_image)
        self.back_image = Path(back_image)

        self.setWindowTitle("Image Preview")

        self.resize(1400, 850)

        self.build_ui()

    ##################################################################

    def build_ui(self):

        root = QVBoxLayout(self)

        images = QHBoxLayout()

        #
        # Front
        #

        front_layout = QVBoxLayout()

        front_title = QLabel("Front")

        front_title.setAlignment(Qt.AlignCenter)

        self.front_label = QLabel()

        self.front_label.setAlignment(Qt.AlignCenter)

        self.front_label.setMinimumSize(600, 700)

        front_layout.addWidget(front_title)

        front_layout.addWidget(self.front_label)

        #
        # Back
        #

        back_layout = QVBoxLayout()

        back_title = QLabel("Back")

        back_title.setAlignment(Qt.AlignCenter)

        self.back_label = QLabel()

        self.back_label.setAlignment(Qt.AlignCenter)

        self.back_label.setMinimumSize(600, 700)

        back_layout.addWidget(back_title)

        back_layout.addWidget(self.back_label)

        #
        # Combine
        #

        images.addLayout(front_layout)

        images.addLayout(back_layout)

        root.addLayout(images)

        self.load_images()

    ##################################################################

    def load_images(self):

        self.load_image(
            self.front_label,
            self.front_image,
        )

        self.load_image(
            self.back_label,
            self.back_image,
        )

    ##################################################################

    def load_image(
        self,
        label,
        image_path,
    ):

        if not image_path.exists():

            label.setText("Image not found")

            return

        pixmap = QPixmap(str(image_path))

        pixmap = pixmap.scaled(
            600,
            700,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation,
        )

        label.setPixmap(pixmap)

    ##################################################################

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:

            self.close()

            return

        super().keyPressEvent(event)