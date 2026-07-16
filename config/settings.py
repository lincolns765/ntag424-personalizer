from pathlib import Path

# =============================================================================
# Project Root
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =============================================================================
# Media Folders
# =============================================================================

MEDIA_ROOT = PROJECT_ROOT / "media"

INCOMING_FOLDER = MEDIA_ROOT / "incoming"
PROCESSING_FOLDER = MEDIA_ROOT / "processing"
COMPLETED_FOLDER = MEDIA_ROOT / "completed"
FAILED_FOLDER = MEDIA_ROOT / "failed"
ARCHIVE_FOLDER = MEDIA_ROOT / "archive"

# =============================================================================
# Cloudflare
# =============================================================================

R2_BUCKET = "collectible-platform-images-dev"
D1_DATABASE = "collectible-platform-dev"

# =============================================================================
# OpenAI
# =============================================================================

OPENAI_MODEL = "gpt-4.1"

# =============================================================================
# Default Values
# =============================================================================

DEFAULT_STORAGE_CASE = "Case-001"

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}