# PIH Stork Solutions
Created at WHACK 2016

We are addressing the discrepancy between true demand and distribution-based demand of medical supplies to sites with poor internet access. The current model uses distribution-based demand, which is subject to inaccuracy due to lack of internet and other information systems infrastructure access.

Our solution attempts to solve this by:
* using the Twilio API so that users can **text orders** instead of needing Internet access
* creating a webapp with **an interactive visualization** of the demand of supplies by location

The webapp will inform Partners In Health (the supplier) as well as the hospital or clinic (the client) about **demand trends** and _when_ to prepare for a higher discrepancy between true demand and distribution-based demand.

Made with a Flask backend, uses HPE Vertica as the database, visualization done with d3.js, and frontend uses JQuery and ajax.
