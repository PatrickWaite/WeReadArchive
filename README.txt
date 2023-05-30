Project Title: WeReadArchive Collection Analysis

Author: Patrick Waite

Purpose: The broad purpose of this project is to narrow down a list of materials vetted by WeReadArchives for the  evaluation and potential purchase and addition to our collecitons.  the main challenge we came across is trying to find the titles within the archive list that didn't already exist in our collections.

--Phase 1: Compare WeReadArchive ISBN values against the Library's FOLIO database records looking for titles that are already owned by our institution.  
	---FOLIO ILS record lookup based on ISBN information provided to the system. 

--Phase 2:  The WeReadArchive data provides urls and links to the titles including estimated price data.  for phase 2 we will be looking at ways to automatically extract this price data and add it to the over all dataset.  this will allow us to have a realistic expectation of cost for the colleciton.

--Phase 3: Gobi collection integration. Ultimatley we would like to streamline the order, if approved, within our GOBI instance for our organization. 

******************************************************************************************************************
[programming notes]
within the extract.py file one of the imports is 'dbConnect'. as this file contains our organization's database address and information. The connection string file that I've uploaded is 'GP_dbConnect' it contains the string patterns but none of the organization data. to use this file you must first enter your relivent database information, and modify the import statment in extract.py. 