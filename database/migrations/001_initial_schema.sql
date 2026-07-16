-- =============================================================================
-- Collectible Authentication Platform
-- Initial Database Schema
--
-- File:
-- database/schema/001_initial_schema.sql
--
-- Cloudflare D1 / SQLite
-- =============================================================================

-- =============================================================================
-- TITLE
-- =============================================================================

CREATE TABLE title (
    guid TEXT PRIMARY KEY,

    title TEXT NOT NULL,

    title_type TEXT NOT NULL
        CHECK(title_type IN ('Movie','TV')),

    release_year INTEGER,

    genre TEXT,

    sub_genre TEXT,

    seasons INTEGER,

    episodes INTEGER,

    created_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    modified_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- =============================================================================
-- COLLECTION
-- =============================================================================

CREATE TABLE collection (

    guid TEXT PRIMARY KEY,

    volume TEXT,

    edition TEXT,

    theme TEXT,

    serial_number TEXT NOT NULL UNIQUE,

    nfc_token TEXT NOT NULL UNIQUE,

    created_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    modified_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    collection_nft_image_url TEXT,

    cover_nft_image_url_front TEXT,

    cover_nft_image_url_back TEXT,

    cover_nft_image_url_spine TEXT
);

-- =============================================================================
-- MEDIA ITEM
-- =============================================================================

CREATE TABLE media_item (

    guid TEXT PRIMARY KEY,

    title_guid TEXT NOT NULL,

    collection_guid TEXT NOT NULL,

    media_type TEXT NOT NULL
        CHECK(
            media_type IN (
                'dvd',
                'dvd10',
                'vhs',
                'blueray',
                'ultrahd4k'
            )
        ),

    edition TEXT,

    distribution_year INTEGER,

    media_item_image_url_front TEXT,

    media_item_image_url_back TEXT,

    distributor TEXT,

    upc TEXT UNIQUE,

    created_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    modified_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    purchase_date TEXT,

    purchase_price REAL,

    grade_text TEXT,

    grade_rubric TEXT,

    grading_company TEXT,

    graded_date TEXT,

    condition TEXT
        CHECK(
            condition IN (
                'sealed',
                'complete',
                'used'
            )
        ),

    FOREIGN KEY(title_guid)
        REFERENCES title(guid),

    FOREIGN KEY(collection_guid)
        REFERENCES collection(guid)
);

-- =============================================================================
-- LISTING
-- =============================================================================

CREATE TABLE listing (

    guid TEXT PRIMARY KEY,

    collection_guid TEXT NOT NULL,

    list_date TEXT,

    sale_date TEXT,

    sale_price REAL,

    list_price REAL,

    listing_url TEXT,

    marketplace TEXT,

    listing_id TEXT UNIQUE,

    status TEXT NOT NULL
        CHECK(
            status IN (
                'listed',
                'unlisted'
            )
        ),

    created_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    modified_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(collection_guid)
        REFERENCES collection(guid)
);

-- =============================================================================
-- AUTHENTICATION LOG
-- =============================================================================

CREATE TABLE authentication_log (

    guid TEXT PRIMARY KEY,

    collection_guid TEXT NOT NULL,

    scan_time TEXT NOT NULL,

    result TEXT NOT NULL,

    worker_version TEXT,

    ip_country TEXT,

    ip_address TEXT,

    device TEXT,

    browser TEXT,

    referrer TEXT,

    response_time_ms INTEGER,

    FOREIGN KEY(collection_guid)
        REFERENCES collection(guid)
);

-- =============================================================================
-- AUDIT LOG
-- =============================================================================

CREATE TABLE audit_log (

    guid TEXT PRIMARY KEY,

    table_name TEXT NOT NULL,

    record_guid TEXT NOT NULL,

    action TEXT NOT NULL,

    old_value TEXT,

    new_value TEXT,

    user_guid TEXT,

    created_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

    deleted_date TEXT,

    modified_date TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- =============================================================================
-- INDEXES
-- =============================================================================

CREATE INDEX idx_title_title
ON title(title);

CREATE INDEX idx_title_type
ON title(title_type);

CREATE INDEX idx_media_title_guid
ON media_item(title_guid);

CREATE INDEX idx_media_collection_guid
ON media_item(collection_guid);

CREATE INDEX idx_media_upc
ON media_item(upc);

CREATE INDEX idx_collection_serial
ON collection(serial_number);

CREATE INDEX idx_collection_nfc
ON collection(nfc_token);

CREATE INDEX idx_listing_collection_guid
ON listing(collection_guid);

CREATE INDEX idx_listing_marketplace
ON listing(marketplace);

CREATE INDEX idx_listing_status
ON listing(status);

CREATE INDEX idx_auth_collection_guid
ON authentication_log(collection_guid);

CREATE INDEX idx_auth_scan_time
ON authentication_log(scan_time);

CREATE INDEX idx_audit_record
ON audit_log(record_guid);

CREATE INDEX idx_audit_table
ON audit_log(table_name);
