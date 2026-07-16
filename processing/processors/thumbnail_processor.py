"""
thumbnail_processor.py

Thumbnail generation utilities.

Responsibilities
----------------
• Open images safely
• Normalize EXIF orientation
• Generate high-quality thumbnails
• Return Pillow Image objects

This module performs NO file caching.
Caching is handled by ThumbnailService.
"""

from pathlib import Path

from PIL import Image
from PIL import ImageOps

from config.settings import THUMBNAIL_SIZE


# ---------------------------------------------------------------------
# Internal Helpers
# ---------------------------------------------------------------------


def _open_image(image_path: Path) -> Image.Image:
    """
    Open an image and normalize its orientation.

    Parameters
    ----------
    image_path : Path

    Returns
    -------
    Pillow Image
    """

    image = Image.open(image_path)

    #
    # Correct phone camera orientation
    #

    image = ImageOps.exif_transpose(image)

    #
    # Always work in RGB
    #

    if image.mode != "RGB":
        image = image.convert("RGB")

    return image


# ---------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------


def create_thumbnail(
    image_path,
    size=THUMBNAIL_SIZE,
):
    """
    Generate a thumbnail.

    Parameters
    ----------
    image_path
        Image file

    size
        Thumbnail size tuple

    Returns
    -------
    Pillow Image
    """

    image_path = Path(image_path)

    image = _open_image(image_path)

    #
    # High quality resize
    #

    image.thumbnail(
        size,
        Image.Resampling.LANCZOS,
    )

    return image


def create_thumbnail_pair(
    front_path,
    back_path,
    size=THUMBNAIL_SIZE,
):
    """
    Generate thumbnails for a front/back image pair.

    Returns
    -------
    (
        front_thumbnail,
        back_thumbnail
    )
    """

    front = create_thumbnail(
        front_path,
        size=size,
    )

    back = create_thumbnail(
        back_path,
        size=size,
    )

    return (
        front,
        back,
    )