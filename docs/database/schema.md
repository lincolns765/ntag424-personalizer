\# Database Schema



\## Purpose



This document describes the production database schema for the Collectible Authentication Platform.



The schema is implemented using \*\*Cloudflare D1 (SQLite)\*\* and is based on the architecture approved during PR-003.



The schema is intended to provide a scalable, normalized foundation for collectible authentication, inventory management, marketplace integrations, NFC verification, and future platform expansion.



\---



\# Database Platform



| Property | Value |

|----------|-------|

| Database Engine | Cloudflare D1 |

| SQL Dialect | SQLite |

| Environment | Development |

| Database Name | collectible-platform-dev |



\---



\# Schema Overview



The current database consists of six core entities.



```

Title

&#x20;   │

&#x20;   ▼

Media Item

&#x20;   │

&#x20;   ▼

Collection

&#x20;   │

&#x20;   ├──────────────┐

&#x20;   ▼              ▼

Listing      Authentication Log



Audit Log

```



Each entity represents a distinct business concept and has a clearly defined responsibility.



\---



\# Tables



\## title



\### Purpose



Represents a unique movie or television series.



Examples:



\- The Matrix

\- Star Wars

\- Breaking Bad



\### Primary Key



```

guid

```



\### Relationships



One Title may have one or more Media Items.



\### Stores



\- Title

\- Title Type

\- Release Year

\- Genre

\- Sub Genre

\- Seasons

\- Episodes

\- Created Date

\- Modified Date



\---



\## media\_item



\### Purpose



Represents a specific commercially distributed release of a Title.



Examples include:



\- DVD

\- DVD10

\- VHS

\- Blu-ray

\- Ultra HD 4K



\### Primary Key



```

guid

```



\### Foreign Keys



```

title\_guid



collection\_guid

```



\### Stores



\- Media Type

\- Edition

\- Distribution Year

\- Distributor

\- UPC

\- Front Cover Image

\- Back Cover Image

\- Purchase Information

\- Grade Information

\- Physical Condition



\---



\## collection



\### Purpose



Represents a collectible grouping within the inventory.



Collections own the permanent NFC identity used by the platform.



\### Primary Key



```

guid

```



\### Stores



\- Volume

\- Edition

\- Theme

\- Serial Number

\- NFC Token

\- NFT Artwork

\- NFT Cover Images



\### Business Responsibilities



\- NFC identity

\- Collectible metadata

\- NFT assets



\---



\## listing



\### Purpose



Represents a marketplace listing for a Collection.



Marketplace information is intentionally separated from collectible metadata.



\### Primary Key



```

guid

```



\### Foreign Key



```

collection\_guid

```



\### Stores



\- Marketplace

\- Listing URL

\- Marketplace Listing ID

\- Listing Status

\- List Price

\- Sale Price

\- Listing Date

\- Sale Date



\---



\## authentication\_log



\### Purpose



Represents one NFC authentication event.



Every NFC scan creates one Authentication Log record.



\### Primary Key



```

guid

```



\### Foreign Key



```

collection\_guid

```



\### Stores



\- Scan Time

\- Authentication Result

\- Worker Version

\- Country

\- IP Address

\- Browser

\- Device

\- Referrer

\- Response Time



Authentication history is never deleted.



\---



\## audit\_log



\### Purpose



Maintains a permanent history of changes made throughout the platform.



Audit Logs support reporting, security, troubleshooting, and compliance.



\### Primary Key



```

guid

```



\### Stores



\- Table Name

\- Record GUID

\- Action

\- Previous Value

\- New Value

\- User GUID

\- Created Date

\- Modified Date

\- Deleted Date



Audit Logs are intentionally independent of individual business tables to allow auditing across the entire application.



\---



\# Relationships



| Parent | Child | Relationship |

|----------|---------|-------------|

| Title | Media Item | One-to-Many |

| Collection | Media Item | One-to-Many |

| Collection | Listing | One-to-Many |

| Collection | Authentication Log | One-to-Many |

| Audit Log | Any Entity | Reference by GUID |



\---



\# Constraints



The schema enforces database integrity through:



\## Primary Keys



Every table uses:



```

guid TEXT PRIMARY KEY

```



\---



\## Foreign Keys



Foreign Keys maintain referential integrity between related entities.



Examples include:



```

media\_item.title\_guid



media\_item.collection\_guid



listing.collection\_guid



authentication\_log.collection\_guid

```



\---



\## Unique Constraints



Unique values include:



\- Serial Number

\- NFC Token

\- UPC

\- Listing ID



These prevent duplicate collectible identifiers.



\---



\## CHECK Constraints



Enumerated fields enforce valid values.



\### title\_type



```

Movie



TV

```



\### media\_type



```

dvd



dvd10



vhs



blueray



ultrahd4k

```



\### condition



```

sealed



complete



used

```



\### listing.status



```

listed



unlisted

```



\---



\# Indexes



Indexes improve lookup performance for frequently queried data.



Current indexes include:



\- title

\- title\_guid

\- collection\_guid

\- serial\_number

\- nfc\_token

\- marketplace

\- listing\_url

\- upc

\- created\_date



Additional indexes may be introduced as query patterns evolve.



\---



\# UUID Strategy



All entities use UUIDs as their primary identifiers.



Benefits include:



\- Globally unique identifiers

\- Cloudflare independent

\- Database independent

\- Safe external references

\- NFC compatibility

\- Marketplace compatibility



UUIDs are immutable and should never be modified after creation.



\---



\# Timestamp Strategy



All entities follow a consistent timestamp convention.



```

created\_date



modified\_date

```



Additional timestamps are used where appropriate:



```

purchase\_date



graded\_date



list\_date



sale\_date



scan\_time



deleted\_date

```



All timestamps should be stored in ISO-8601 format.



\---



\# Deployment



The schema is deployed using Wrangler.



Example:



```powershell

wrangler d1 execute collectible-platform-dev --file database/schema/001\_initial\_schema.sql

```



Verify deployment:



```powershell

wrangler d1 execute collectible-platform-dev --command ".tables"



wrangler d1 execute collectible-platform-dev --command ".schema"

```



\---



\# Design Principles



The schema has been designed to:



\- Normalize shared data

\- Separate business responsibilities

\- Support multiple media formats

\- Support multiple marketplace integrations

\- Maintain permanent NFC identities

\- Preserve complete authentication history

\- Preserve audit history

\- Support future NFT functionality

\- Scale without major redesign



\---



\# Future Expansion



The schema has been designed to support future entities including:



\- User

\- Role

\- Marketplace

\- NFT

\- API Key

\- Marketplace Synchronization



Future features should extend the existing schema without requiring significant changes to the core architecture.



\---



\# Version



Schema Version



\*\*001\_initial\_schema\*\*



Status



\*\*Production Design\*\*



Implemented In



\*\*PR-004 – Cloudflare D1 Database Schema\*\*

