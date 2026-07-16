\# Business Rules



\## Titles



A Title represents a unique movie or television series.



A Title contains only information common to every release of that title.



A Title may have one or many Media Items.



Titles are never associated directly with NFC tags, collections, listings, or authentication events.



\---



\## Media Items



A Media Item represents a specific physical release of a Title.



Examples include:



\- DVD

\- DVD10

\- VHS

\- Blu-ray

\- Ultra HD 4K



A Title may have multiple Media Items representing different editions or distribution formats.



Each Media Item stores release-specific metadata including:



\- Media type

\- Edition

\- Distributor

\- UPC

\- Cover images

\- Distribution year

\- Purchase information

\- Grading information

\- Physical condition



Each Media Item belongs to exactly one Title.



\---



\## Collections



A Collection represents a collectible grouping for one or more Media Items.



Each Collection owns exactly one NFC tag.



The Collection stores collectible-specific information including:



\- NFC token

\- Serial number

\- Theme

\- Volume

\- NFT artwork

\- Cover artwork



The Collection serves as the object authenticated by the NFC platform.



\---



\## Listings



Marketplace listings belong to Collections.



A Collection may have zero or many Listings over its lifetime.



Each Listing records:



\- Marketplace

\- Marketplace listing identifier

\- Listing URL

\- Listing status

\- List price

\- Sale price

\- Listing date

\- Sale date



Moving a collectible between marketplaces should only require creating or updating Listing records.



The NFC tag never changes when marketplace listings change.



\---



\## Authentication



Every NFC scan generates an Authentication Log entry.



Each Authentication Log belongs to one Collection.



Authentication records include:



\- Scan timestamp

\- Authentication result

\- Worker version

\- IP address

\- Country

\- Browser

\- Device

\- Referrer

\- Response time



Authentication history is never deleted.



\---



\## Audit Logging



Every significant modification should create an Audit Log record.



Audit Logs record:



\- Table modified

\- Record modified

\- Action performed

\- Previous value

\- New value

\- User responsible

\- Creation timestamp

\- Modification timestamp

\- Deletion timestamp (when applicable)



Audit Logs provide a permanent history of changes for troubleshooting, security, and reporting.



\---



\## Marketplace Independence



Marketplace information is intentionally separated from collectible metadata.



This allows a collectible to move between:



\- OpenSea

\- Shopify

\- eBay

\- Whatnot

\- Future marketplaces



without modifying the NFC tag or collectible identity.



\---



\## NFC Identity



Each Collection owns exactly one NFC token.



The NFC token uniquely identifies the collectible.



The NFC token should remain permanent for the lifetime of the Collection.



Marketplace listings, URLs, and ownership may change without requiring the NFC tag to be rewritten.



\---



\## Future Expansion



The database architecture is designed to support future additions including:



\- NFT ownership

\- User accounts

\- Administrative portal

\- Marketplace synchronization

\- Authentication analytics

\- Scan history reporting

\- Mobile applications

\- Additional physical media formats



Future functionality should be added by extending the existing schema rather than redesigning core entities.

