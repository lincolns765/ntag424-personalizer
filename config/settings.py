from pathlib import Path
import os

# =============================================================================
# Project Root
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =============================================================================
# Media Root
# =============================================================================

MEDIA_ROOT = PROJECT_ROOT / "media"

INCOMING_FOLDER = MEDIA_ROOT / "incoming"
PROCESSING_FOLDER = MEDIA_ROOT / "processing"
COMPLETED_FOLDER = MEDIA_ROOT / "completed"
FAILED_FOLDER = MEDIA_ROOT / "failed"
ARCHIVE_FOLDER = MEDIA_ROOT / "archive"

# =============================================================================
# Storage
# =============================================================================

THUMBNAIL_FOLDER = PROJECT_ROOT / "storage" / "thumbnails"
CACHE_FOLDER = PROJECT_ROOT / "storage" / "cache"
TEMP_FOLDER = PROJECT_ROOT / "storage" / "temp"

# =============================================================================
# Cloudflare
# =============================================================================

R2_BUCKET = "collectible-platform-images-dev"
D1_DATABASE = "collectible-platform-dev"

# =============================================================================
# OpenAI
# =============================================================================

OPENAI_MODEL = "gpt-4.1"

# Read API key from environment variable.
# Never hardcode secrets in source code.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# =============================================================================
# Defaults
# =============================================================================

DEFAULT_STORAGE_CASE = "Case-001"

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
}

THUMBNAIL_SIZE = (250, 250)

# =============================================================================
# Display
# =============================================================================

PREVIEW_ROWS = 100

SHOW_THUMBNAILS = True

AUTO_SORT_IMAGES = True