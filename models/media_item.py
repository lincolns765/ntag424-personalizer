from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class MediaItem:
    """
    Represents one collectible.

    One MediaItem always contains exactly one
    front image and one back image.

    Every stage of the pipeline modifies this
    object rather than passing around tuples.
    """

    #
    # Required
    #

    front_image: Path
    back_image: Path

    #
    # Generated during processing
    #

    front_thumbnail: Path | None = None
    back_thumbnail: Path | None = None

    guid: str = ""

    storage_case: str = ""

    status: str = "Pending"

    #
    # AI Metadata
    #

    title: str = ""

    media_type: str = ""

    edition: str = ""

    upc: str = ""

    year: str = ""

    publisher: str = ""

    studio: str = ""

    region: str = ""

    language: str = ""

    disc_count: int = 1

    #
    # Cloudflare
    #

    front_r2_url: str = ""

    back_r2_url: str = ""

    #
    # Database
    #

    database_id: int | None = None

    processed: bool = False

    uploaded: bool = False

    ai_complete: bool = False