from pathlib import Path

from ingestion.folder_scanner import scan_folder
from ingestion.image_pairer import pair_images


class IngestionService:
    """
    Coordinates the media ingestion pipeline.

    Pipeline

        Scan Folder
            ↓
        Pair Images
            ↓
        Return image pairs

    No GUI code belongs here.
    """

    def __init__(self):

        self.images = []
        self.pairs = []

    ##################################################################

    def scan(self, folder):

        folder = Path(folder)

        #
        # Scan folder
        #

        self.images = scan_folder(folder)

        #
        # Pair images
        #

        self.pairs = pair_images(self.images)

        #
        # Return summary
        #

        return {

            "images": self.images,

            "pairs": self.pairs,

            "image_count": len(self.images),

            "pair_count": len(self.pairs),

            "unpaired": len(self.images) - (len(self.pairs) * 2),

        }

    ##################################################################

    def get_pairs(self):

        return self.pairs

    ##################################################################

    def image_count(self):

        return len(self.images)

    ##################################################################

    def pair_count(self):

        return len(self.pairs)

    ##################################################################

    def clear(self):

        self.images.clear()
        self.pairs.clear()