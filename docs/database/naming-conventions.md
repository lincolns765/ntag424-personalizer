\# Naming Conventions



\## Purpose



This document defines the naming standards used throughout the Collectible Authentication Platform.



Consistent naming improves readability, maintainability, and reduces ambiguity as the platform grows.



Unless otherwise noted, all database object names use \*\*snake\_case\*\*.



\---



\# Table Names



Tables represent singular business entities.



Current tables:



```text

title



media\_item



collection



listing



authentication\_log



audit\_log

```



Future tables should follow the same convention.



Examples:



```text

user



role



marketplace



marketplace\_sync



api\_key



nft

```



\---



\# Primary Keys



Every table uses a UUID as its primary key.



Primary keys are always named:



```text

guid

```



Example:



```text

title.guid



media\_item.guid



collection.guid

```



\---



\# Foreign Keys



Foreign keys reference the primary key of another table.



Naming convention:



```text

<referenced\_table>\_guid

```



Examples:



```text

title\_guid



media\_item\_guid



collection\_guid



listing\_guid



user\_guid

```



Foreign key names should clearly indicate the referenced entity.



\---



\# Date Fields



Date and timestamp columns use descriptive names ending in `\_date` or `\_time`.



Examples:



```text

created\_date



modified\_date



deleted\_date



purchase\_date



graded\_date



distribution\_year



release\_year



list\_date



sale\_date



scan\_time

```



\---



\# Price Fields



Monetary values should include their purpose.



Examples:



```text

purchase\_price



list\_price



sale\_price

```



Future monetary fields should follow the same convention.



\---



\# URL Fields



URL fields should clearly describe the resource they reference.



Examples:



```text

listing\_url



media\_item\_image\_url\_front



media\_item\_image\_url\_back



collection\_nft\_image\_url



cover\_nft\_image\_url\_front



cover\_nft\_image\_url\_back



cover\_nft\_image\_url\_spine

```



\---



\# Image Fields



Image fields should identify both the image type and viewing angle when applicable.



Examples:



```text

media\_item\_image\_url\_front



media\_item\_image\_url\_back



cover\_nft\_image\_url\_front



cover\_nft\_image\_url\_back



cover\_nft\_image\_url\_spine

```



\---



\# Enumerated Fields



Fields with predefined values should use descriptive names.



Examples:



```text

title\_type



media\_type



condition



status



marketplace

```



Allowed values should be documented separately and validated by the application.



\---



\# Log Tables



Operational logs use descriptive table names ending with `\_log`.



Examples:



```text

authentication\_log



audit\_log

```



Future log tables should follow the same convention.



\---



\# General Standards



\- Use lowercase names.

\- Use snake\_case for all tables and columns.

\- Use singular table names.

\- Use `guid` as the primary key for every table.

\- Use `<table\_name>\_guid` for foreign keys.

\- Use descriptive column names rather than abbreviations.

\- Avoid reserved SQL keywords.

\- Prefer clarity over brevity.



These conventions should be followed consistently for all future database objects to ensure a maintainable and scalable schema.

