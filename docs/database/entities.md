\# Entity Definitions



\## Core Entities



\### Title



Represents a unique movie or television series.



The Title entity stores information common to every release of a title regardless of media format.



Examples:



\- The Matrix

\- Breaking Bad

\- The Lord of the Rings



A Title may have one or many Media Items.



Stores:



\- Title

\- Title Type

\- Original Release Year

\- Genre

\- Sub Genre

\- Seasons (TV only)

\- Episodes (TV only)



\---



\### Media Item



Represents a specific commercially distributed release of a Title.



A Media Item describes the release itself rather than the collectible or marketplace listing.



Examples:



\- The Matrix DVD

\- The Matrix Collector's Edition DVD

\- The Matrix Blu-ray

\- The Matrix Ultra HD 4K

\- Breaking Bad Season 1 DVD



Each Media Item belongs to exactly one Title.



Stores:



\- Media Type

\- Edition

\- Distribution Year

\- Distributor

\- UPC

\- Front Cover Image

\- Back Cover Image

\- Purchase Information

\- Grading Information

\- Physical Condition



\---



\### Collection



Represents a collectible grouping within the inventory.



A Collection owns the collectible identity used throughout the platform and is the entity associated with NFC authentication.



Each Collection stores:



\- NFC Token

\- Serial Number

\- Theme

\- Volume

\- NFT Artwork

\- Front Cover NFT Image

\- Back Cover NFT Image

\- Spine NFT Image



Collections provide the permanent identity that marketplace listings and authentication events reference.



\---



\### Listing



Represents a marketplace listing for a Collection.



A Collection may have multiple Listings over its lifetime as it moves between marketplaces.



Each Listing stores:



\- Marketplace

\- Marketplace Listing ID

\- Listing URL

\- Listing Status

\- List Price

\- Sale Price

\- List Date

\- Sale Date



Listings are independent of the NFC identity.



Changing marketplaces should only require creating or updating Listing records.



\---



\### Authentication Log



Represents a single NFC authentication event.



Every scan of an NFC tag creates one Authentication Log record.



Stores:



\- Scan Time

\- Authentication Result

\- Worker Version

\- IP Address

\- Country

\- Browser

\- Device

\- Referrer

\- Response Time



Authentication history is retained for security, analytics, and reporting.



\---



\### Audit Log



Represents a permanent history of changes made to system records.



Every significant modification should create an Audit Log entry.



Stores:



\- Table Name

\- Record Identifier

\- Action Performed

\- Previous Value

\- New Value

\- User Identifier

\- Created Date

\- Modified Date

\- Deleted Date



Audit Logs support troubleshooting, security investigations, and historical reporting.

