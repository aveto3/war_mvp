# war_mvp
Adrian Veto, Graham Xavier, Noah Berger, Jonathan Manela

### Overview
This project, made as a project for Wolverine Sports Analytics at the University of Michigan, attempts to determine if the correlation between bWAR and awards voting has increased in the modern era. As advanced analytics have become more mainstream, it has become a common comment that the BWAA determines the winners of awards solely based on their WAR. This project aims to address that comment – is it true that WAR is more of a deciding factor in voting, and if so, is that a bad thing?

This project is written entirely in Python and uses the BeautifulSoup, MatPlotLib, Numpy and Pandas libraries.

### Files
- ```mvp_webscraping.py``` contains the code for scraping Baseball Reference's pages for MVP Winners (can easily be adjusted to work for Cy Young, Rookie of the Year, etc.). Written in Python using BeautifulSoup for the webscraping.
- ```plots_starter.py``` contains sample code for creating plots using the data scraped from Baseball Reference, including the correlation between WAR and award placements. Written in Python using MatPlotLib and Pandas.
- ```csv_files``` contains three .csv files consisting of data for award winners. ```csv_files/full_large.csv``` contains the full dataset. ```csv_files/modern_large.csv``` contains data since 2012, and ```csv_files/old_large.csv``` contains data before 2012.
- ```demo_plots``` contains the plots made in ```plots_starter.py```.

*Note: ```mvp_webscraping.py``` may have to run multiple times with adjusted start dates to scrape the entire data, as Baseball Reference will timeout a computer that submits too many requests.*
