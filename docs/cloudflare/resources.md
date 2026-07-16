# Cloudflare Resources

## D1

Purpose

Primary application database.

Stores:

- Titles
- Releases
- Physical copies
- Collection items
- Grades
- Marketplace listings
- Authentication logs


 ⛅️ wrangler 4.108.0 (update available 4.109.0)
───────────────────────────────────────────────
✅ Successfully created DB 'collectible-platform-dev' in region ENAM
Created your new D1 database.

To access your new D1 Database in your Worker, add the following snippet to your configuration file:
[[d1_databases]]
binding = "collectible_platform_dev"
database_name = "collectible-platform-dev"
database_id = "2f3d888a-4493-4cdb-bb69-b0dd048ae2dc"


---

## R2

Purpose

Object storage.

Stores:

- Grade photographs
- NFT images
- Export files
- Reports

 ⛅️ wrangler 4.108.0 (update available 4.109.0)
───────────────────────────────────────────────
Creating bucket 'collectible-platform-images-dev'...
✅ Created bucket 'collectible-platform-images-dev' with default storage class of Standard.
To access your new R2 Bucket in your Worker, add the following snippet to your configuration file:
[[r2_buckets]]
bucket_name = "collectible-platform-images-dev"
binding = "collectible_platform_images_dev"


---

## Workers KV

Purpose

Ultra-fast key/value storage.

Stores:

- Redirect mappings
- Configuration values
- Cached metadata

KV should not be used as the primary database.

 ⛅️ wrangler 4.108.0 (update available 4.109.0)
───────────────────────────────────────────────
Resource location: remote

🌀 Creating namespace with title "CACHE"
✨ Success!
To access your new KV Namespace in your Worker, add the following snippet to your configuration file:
[[kv_namespaces]]
binding = "CACHE"
id = "28e50cd1bd0b4735829b50fec5944677"


 ⛅️ wrangler 4.108.0 (update available 4.109.0)
───────────────────────────────────────────────
Resource location: remote

🌀 Creating namespace with title "CONFIG"
✨ Success!
To access your new KV Namespace in your Worker, add the following snippet to your configuration file:
[[kv_namespaces]]
binding = "CONFIG"
id = "0be9b56c400e4d9d84e51a78effb8195"


---

## Workers

Authentication Worker

Future REST API

Future Admin Portal

---

## Secrets

Future secrets include:

- Shopify API key
- OpenSea API key
- Encryption keys