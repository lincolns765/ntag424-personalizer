\# Relationships



\## Overview



The Collectible Authentication Platform is organized around six core entities:



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

Listing     Authentication Log



Audit Log

```



Each entity has a specific responsibility and is designed to minimize data duplication while supporting future expansion.



\---



\# Title → Media Item



Relationship



\*\*One-to-Many (1:N)\*\*



A Title may have one or many Media Items.



Each Media Item belongs to exactly one Title.



Examples:



```

The Matrix

&#x20;   ├── DVD

&#x20;   ├── DVD Collector's Edition

&#x20;   ├── Blu-ray

&#x20;   ├── Ultra HD 4K

```



\---



\# Media Item → Collection



Relationship



\*\*One-to-One (1:1)\*\*



Each Media Item belongs to one Collection.



Each Collection represents a collectible grouping within the inventory.



The Collection stores collectible-specific metadata including:



\- NFC Token

\- Serial Number

\- Theme

\- Volume

\- NFT Images



The Collection provides the permanent identity used throughout the platform.



\---



\# Collection → Listing



Relationship



\*\*One-to-Many (1:N)\*\*



A Collection may have zero or many Listings.



Each Listing belongs to exactly one Collection.



Listings contain marketplace-specific information including:



\- Marketplace

\- Listing URL

\- Marketplace Listing ID

\- List Price

\- Sale Price

\- Listing Status



Separating Listings from Collections allows collectibles to move between marketplaces without changing their NFC identity.



\---



\# Collection → Authentication Log



Relationship



\*\*One-to-Many (1:N)\*\*



Every NFC scan creates one Authentication Log record.



A Collection may have zero or many Authentication Log entries.



Authentication Logs record:



\- Scan Time

\- Authentication Result

\- Worker Version

\- IP Address

\- Country

\- Browser

\- Device

\- Referrer

\- Response Time



Authentication history should never be deleted.



\---



\# Audit Log



Relationship



\*\*Reference Entity\*\*



Audit Logs may reference records from any table in the system.



Each Audit Log records:



\- Table modified

\- Record modified

\- Action performed

\- Previous value

\- New value

\- User responsible

\- Timestamps



Audit Logs provide a permanent history of significant changes for troubleshooting, reporting, and security investigations.



\---



\# NFC Identity



Each Collection owns exactly one NFC token.



The NFC token uniquely identifies the collectible.



The NFC identity should remain permanent throughout the lifetime of the Collection.



Marketplace listings may change without requiring the NFC tag to be rewritten.



\---



\# Marketplace Independence



Marketplace information is intentionally separated from collectible metadata.



A collectible may be listed on multiple marketplaces over its lifetime, including:



\- OpenSea

\- Shopify

\- eBay

\- Whatnot

\- Future marketplaces



Moving a collectible between marketplaces should only require creating or updating Listing records.



The Collection and its NFC identity remain unchanged.



\---



\# Relationship Summary



| Parent Entity | Child Entity | Cardinality |

|---------------|--------------|-------------|

| Title | Media Item | 1 : Many |

| Media Item | Collection | 1 : 1 |

| Collection | Listing | 1 : Many |

| Collection | Authentication Log | 1 : Many |

| Audit Log | Any Entity | Many : 1 (Reference) |

