\# Data Dictionary



\## Purpose



This document defines every table and column used within the Collectible Authentication Platform database.



It serves as the authoritative reference for database development and should remain synchronized with the Entity Relationship Diagram (ERD) and SQL schema.



Unless otherwise specified:



\- UUIDs are stored as `TEXT`

\- Dates and timestamps are stored as `TEXT` in ISO-8601 format

\- Monetary values are stored as `REAL`

\- Strings are stored as `TEXT`



\---



\# Table: title



\## Description



Represents a unique movie or television series.



Each Title may have one or more Media Items.



| Column | Type | Nullable | Default | Description |

|---------|------|----------|---------|-------------|

| guid | TEXT | No | None | Primary Key (UUID) |

| title | TEXT | No | None | Official title of the movie or television series |

| title\_type | TEXT | No | None | Movie or TV |

| release\_year | INTEGER | Yes | None | Original release year |

| genre | TEXT | Yes | None | Primary genre |

| sub\_genre | TEXT | Yes | None | Secondary genre |

| seasons | INTEGER | Yes | None | Number of seasons (TV only) |

| episodes | INTEGER | Yes | None | Number of episodes (TV only) |

| created\_date | TEXT | No | CURRENT\_TIMESTAMP | Record creation date |

| modified\_date | TEXT | No | CURRENT\_TIMESTAMP | Last modification date |



\---



\# Table: collection



\## Description



Represents a collectible grouping within the inventory.



Collections own the NFC identity for authentication.



| Column | Type | Nullable | Default | Description |

|---------|------|----------|---------|-------------|

| guid | TEXT | No | None | Primary Key (UUID) |

| volume | TEXT | Yes | None | Volume number or designation |

| edition | TEXT | Yes | None | Collection edition |

| theme | TEXT | Yes | None | Collection theme |

| serial\_number | TEXT | No | None | Internal serial number |

| nfc\_token | TEXT | No | None | NFC token assigned to the collectible |

| created\_date | TEXT | No | CURRENT\_TIMESTAMP | Record creation date |

| modified\_date | TEXT | No | CURRENT\_TIMESTAMP | Last modification date |

| collection\_nft\_image\_url | TEXT | Yes | None | NFT artwork image |

| cover\_nft\_image\_url\_front | TEXT | Yes | None | Front NFT artwork |

| cover\_nft\_image\_url\_back | TEXT | Yes | None | Back NFT artwork |

| cover\_nft\_image\_url\_spine | TEXT | Yes | None | Spine NFT artwork |



\---



\# Table: media\_item



\## Description



Represents a specific physical release of a Title.



| Column | Type | Nullable | Default | Description |

|---------|------|----------|---------|-------------|

| guid | TEXT | No | None | Primary Key (UUID) |

| title\_guid | TEXT | No | None | Foreign Key to Title |

| collection\_guid | TEXT | No | None | Foreign Key to Collection |

| media\_type | TEXT | No | None | DVD, DVD10, VHS, Blu-ray, Ultra HD 4K |

| edition | TEXT | Yes | None | Release edition |

| distribution\_year | INTEGER | Yes | None | Commercial distribution year |

| media\_item\_image\_url\_front | TEXT | Yes | None | Front cover image |

| media\_item\_image\_url\_back | TEXT | Yes | None | Back cover image |

| distributor | TEXT | Yes | None | Distributor or publisher |

| upc | TEXT | Yes | None | Universal Product Code |

| created\_date | TEXT | No | CURRENT\_TIMESTAMP | Record creation date |

| modified\_date | TEXT | No | CURRENT\_TIMESTAMP | Last modification date |

| purchase\_date | TEXT | Yes | None | Date purchased |

| purchase\_price | REAL | Yes | None | Purchase price |

| grade\_text | TEXT | Yes | None | Overall grade |

| grade\_rubric | TEXT | Yes | None | Grading notes or rubric |

| grading\_company | TEXT | Yes | None | Grading organization |

| graded\_date | TEXT | Yes | None | Date graded |

| condition | TEXT | Yes | None | sealed, complete, or used |



\---



\# Table: listing



\## Description



Represents a marketplace listing associated with a Collection.



| Column | Type | Nullable | Default | Description |

|---------|------|----------|---------|-------------|

| guid | TEXT | No | None | Primary Key (UUID) |

| collection\_guid | TEXT | No | None | Foreign Key to Collection |

| list\_date | TEXT | Yes | None | Listing date |

| sale\_date | TEXT | Yes | None | Sale date |

| sale\_price | REAL | Yes | None | Final sale price |

| list\_price | REAL | Yes | None | Initial listing price |

| listing\_url | TEXT | Yes | None | Marketplace URL |

| marketplace | TEXT | Yes | None | Marketplace name |

| listing\_id | TEXT | Yes | None | Marketplace listing identifier |

| status | TEXT | No | None | listed or unlisted |

| created\_date | TEXT | No | CURRENT\_TIMESTAMP | Record creation date |

| modified\_date | TEXT | No | CURRENT\_TIMESTAMP | Last modification date |



\---



\# Table: authentication\_log



\## Description



Represents one NFC authentication event.



Each NFC scan creates one Authentication Log record.



| Column | Type | Nullable | Default | Description |

|---------|------|----------|---------|-------------|

| guid | TEXT | No | None | Primary Key (UUID) |

| collection\_guid | TEXT | No | None | Foreign Key to Collection |

| scan\_time | TEXT | No | None | Scan timestamp |

| result | TEXT | No | None | Authentication result |

| worker\_version | TEXT | Yes | None | Worker version used |

| ip\_country | TEXT | Yes | None | Country of request |

| ip\_address | TEXT | Yes | None | IP address |

| device | TEXT | Yes | None | Device type |

| browser | TEXT | Yes | None | Browser information |

| referrer | TEXT | Yes | None | Referring URL |

| response\_time\_ms | INTEGER | Yes | None | Worker response time (milliseconds) |



\---



\# Table: audit\_log



\## Description



Represents a permanent record of significant changes within the system.



Audit Logs support reporting, troubleshooting, and historical analysis.



| Column | Type | Nullable | Default | Description |

|---------|------|----------|---------|-------------|

| guid | TEXT | No | None | Primary Key (UUID) |

| table\_name | TEXT | No | None | Name of modified table |

| record\_guid | TEXT | No | None | GUID of modified record |

| action | TEXT | No | None | Action performed (INSERT, UPDATE, DELETE) |

| old\_value | TEXT | Yes | None | Previous value before modification |

| new\_value | TEXT | Yes | None | New value after modification |

| user\_guid | TEXT | Yes | None | User responsible for the change |

| created\_date | TEXT | No | CURRENT\_TIMESTAMP | Date the audit record was created |

| deleted\_date | TEXT | Yes | None | Date the record was deleted (if applicable) |

| modified\_date | TEXT | No | CURRENT\_TIMESTAMP | Last modification date |



\---



\# Enumerated Values



\## title\_type



| Value | Description |

|--------|-------------|

| Movie | Motion picture |

| TV | Television series |



\---



\## media\_type



| Value | Description |

|--------|-------------|

| dvd | Standard DVD |

| dvd10 | Dual-sided DVD-10 |

| vhs | VHS Cassette |

| blueray | Blu-ray Disc |

| ultrahd4k | Ultra HD 4K Disc |



\---



\## condition



| Value | Description |

|--------|-------------|

| sealed | Factory sealed |

| complete | Open but complete |

| used | Previously used |



\---



\## listing.status



| Value | Description |

|--------|-------------|

| listed | Active marketplace listing |

| unlisted | Not currently listed |



\---



\# Data Standards



\- All primary keys are UUIDs.

\- All foreign keys reference UUIDs.

\- All timestamps use ISO-8601 format.

\- Monetary values use REAL.

\- URLs are stored as TEXT.

\- UUIDs are immutable.

\- NFC tokens are unique.

\- Serial numbers are unique.

\- Marketplace listings are associated with Collections.

\- Authentication history should never be deleted.

\- Audit history should be preserved permanently.



\---



\# Version



Current Database Version



\*\*001\_initial\_schema\*\*



Last Updated



\*\*PR-004 – Cloudflare D1 Database Schema\*\*

