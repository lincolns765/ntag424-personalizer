"""
thumbnail_processor.py

Creates thumbnail images for notebook preview.
"""

from pathlib import Path

from PIL import Image

from config.settings import THUMBNAIL_SIZE


def create_thumbnail(image_path):
    """
    Create a thumbnail from an image.

    Returns a Pillow Image object.
    """

    image_path = Path(image_path)

    image = Image.open(image_path)

    image.thumbnail(THUMBNAIL_SIZE)

    return image


def create_thumbnail_pair(front_path, back_path):
    """
    Returns

    (
        front_thumbnail,
        back_thumbnail
    )
    """

    front = create_thumbnail(front_path)

    back = create_thumbnail(back_path)

    return front, back