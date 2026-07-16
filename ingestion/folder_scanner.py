from pathlib import Path

from config.settings import (
    INCOMING_FOLDER,
    SUPPORTED_EXTENSIONS,
)


def scan_folder(folder=INCOMING_FOLDER):
    """
    Scan folder for supported images.

    Returns a sorted list of pathlib.Path objects.
    """

    folder = Path(folder)

    files = [
        file
        for file in folder.iterdir()
        if file.is_file()
        and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    return sorted(files)