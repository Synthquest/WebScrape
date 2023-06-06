1. Open https://a16z.com/portfolio/
2. Inspect element
3. Right click "body" element containing all other elements
4. Copy Inner -> paste to htmlCode_Binance.html
5. run htmlScrape.py to export CSV of webpage info
6. Copy/paste results and override the descriptions.csv file
7. run descriptionSearch.py - you need to have a google ID & search key in your .env to run this
    it essentially runs a google search for each link and grabs the description on the page
8. run merge.py to merge the descriptions with the ventures.csv to create mergedVentures.csv
9. youll need to run CexVentures.py to combine this to the main csv
