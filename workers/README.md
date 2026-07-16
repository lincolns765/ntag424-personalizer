\# Cloudflare Workers



This directory contains all Cloudflare Worker projects used by the Collectible Authentication Platform.



Workers provide the serverless backend for the application and run at Cloudflare's edge locations around the world.



\## Planned Workers



\### Authentication Worker



Authenticates NTAG424 DNA NFC tags using Secure Dynamic Messaging (SUN).



Responsibilities:



\- Verify NFC tag authenticity

\- Validate SUN message

\- Detect cloned tags

\- Log scan events

\- Redirect authenticated users



\---



\### API Worker



Future REST API for:



\- Inventory

\- Grading

\- Marketplace management

\- Administration



\---



\### Admin Worker



Future administration portal.



Responsibilities:



\- Inventory management

\- User authentication

\- Reporting

\- Configuration



\---



\## Related Cloudflare Services



Workers communicate with:



\- Cloudflare D1

\- Cloudflare R2

\- Cloudflare KV



Workers never communicate directly with NFC hardware.



Python performs NFC personalization.



Workers perform cloud authentication.

