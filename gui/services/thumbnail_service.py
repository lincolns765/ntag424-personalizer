"""
thumbnail_service.py

Manages thumbnail generation and caching.

Responsibilities
----------------
• Determine thumbnail locations
• Generate thumbnails when missing
• Reuse cached thumbnails
• Clear thumbnail cache

This service contains NO GUI code.
"""

from pathlib import Path

from config.settings import THUMBNAIL_FOLDER

from processing.processors.thumbnail_processor import (
    create_thumbnail,
)


class ThumbnailService:

    def __init__(self):

        THUMBNAIL_FOLDER.mkdir(
            parents=True,
            exist_ok=True,
        )

    ##################################################################

    def thumbnail_path(
        self,
        image_path,
    ):
        """
        Returns the cache location for a single image.
        """

        image_path = Path(image_path)

        return (
            THUMBNAIL_FOLDER
            / f"{image_path.stem}_thumb.jpg"
        )

    ##################################################################

    def ensure_thumbnail(
        self,
        image_path,
    ):
        """
        Returns a thumbnail path.

        Generates the thumbnail if it does not already exist.
        """

        image_path = Path(image_path)

        thumb_path = self.thumbnail_path(
            image_path
        )

        #
        # Cache hit
        #

        if thumb_path.exists():

            return thumb_path

        #
        # Generate thumbnail
        #

        thumbnail = create_thumbnail(
            image_path
        )

        thumbnail.save(
            thumb_path,
            "JPEG",
            quality=90,
        )

        return thumb_path

    ##################################################################

    def ensure_pair(
        self,
        front_image,
        back_image,
    ):
        """
        Ensure both thumbnails exist.

        Returns

        (
            front_thumbnail_path,
            back_thumbnail_path
        )
        """

        front_thumb = self.ensure_thumbnail(
            front_image
        )

        back_thumb = self.ensure_thumbnail(
            back_image
        )

        return (
            front_thumb,
            back_thumb,
        )

    ##################################################################

    def cache_exists(
        self,
        image_path,
    ):

        return self.thumbnail_path(
            image_path
        ).exists()

    ##################################################################

    def cache_size(self):
        """
        Number of cached thumbnails.
        """

        return len(
            list(
                THUMBNAIL_FOLDER.glob(
                    "*_thumb.jpg"
                )
            )
        )

    ##################################################################

    def clear_cache(self):
        """
        Delete every cached thumbnail.
        """

        for thumbnail in THUMBNAIL_FOLDER.glob(
            "*_thumb.jpg"
        ):

            thumbnail.unlink(
                missing_ok=True,
            )