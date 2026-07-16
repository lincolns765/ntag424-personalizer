\# Entity Relationship Diagram



\## Purpose



This document defines the logical data model for the Collectible Authentication Platform.



The Entity Relationship Diagram (ERD) serves as the blueprint for the application's database architecture and establishes how all core entities interact before implementation begins.



The ERD defines:



\- System entities

\- Primary Keys (PK)

\- Foreign Keys (FK)

\- Entity relationships

\- Relationship cardinality

\- Business ownership of data

\- Future expansion points



The ERD is the authoritative source for database design and should be reviewed and approved before creating the Cloudflare D1 schema or database migrations.



\---



\## Core Entity Hierarchy



The platform is organized around six primary entities.



```

Title

&#x20;   │

&#x20;   ▼

Media Item

&#x20;   │

&#x20;   ▼

Collection

&#x20;   │

&#x20;   ├───────────────┐

&#x20;   ▼               ▼

Listing      Authentication Log



Audit Log

```



\### Title



Represents a unique movie or television series.



A Title contains information that is common across every physical release regardless of media format.



Examples:



\- The Matrix

\- Breaking Bad

\- Star Wars



\---



\### Media Item



Represents a specific commercially distributed release of a Title.



Examples include:



\- DVD

\- DVD10

\- VHS

\- Blu-ray

\- Ultra HD 4K



Each Media Item stores release-specific information including edition, distributor, UPC, artwork, grading information, purchase information, and physical condition.



\---



\### Collection



Represents a collectible grouping within the inventory.



The Collection owns the permanent collectible identity and is responsible for:



\- NFC token

\- Serial number

\- NFT artwork

\- Cover artwork

\- Collection metadata



Every NFC tag permanently identifies a Collection.



\---



\### Listing



Represents a marketplace listing for a Collection.



Listings are intentionally separated from collectible data to allow the same collectible to move between marketplaces without changing its NFC identity.



Supported marketplaces may include:



\- OpenSea

\- Shopify

\- eBay

\- Whatnot

\- Future marketplace integrations



\---



\### Authentication Log



Represents an NFC authentication event.



Every scan generates one Authentication Log record.



Authentication history provides:



\- Scan history

\- Device information

\- Geographic information

\- Worker version

\- Performance metrics

\- Security auditing



Authentication history should never be deleted.



\---



\### Audit Log



Represents a permanent history of changes made throughout the system.



Audit Logs capture:



\- Record changes

\- Previous values

\- New values

\- User actions

\- Timestamps



Audit Logs support troubleshooting, reporting, and long-term traceability.



\---



\## Diagram Files



The editable ERD is maintained in:



```

docs/database/images/collectible-platform-erd.drawio

```



The exported reference image is maintained in:



```

docs/database/images/collectible-platform-erd.png

```



Both files should be updated whenever the database architecture changes.



\---



\## Design Principles



The Entity Relationship Diagram has been designed with the following objectives:



\- Normalize shared data

\- Separate content from collectible inventory

\- Support multiple media formats

\- Support multiple marketplace integrations

\- Maintain permanent NFC identities

\- Preserve complete authentication history

\- Preserve complete audit history

\- Support future NFT functionality

\- Support future user management

\- Minimize future schema redesign



The ERD should be considered the authoritative reference for all future database implementation work.

