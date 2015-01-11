# American Time Use Analysis

## Description

Use the U.S. Department of Labor's data on Americans' time use for research and analysis.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* How to use public data for analysis
* How to translate data from CSVs to relational databases
* How to publish your own data analysis as a notebook

### Performance Objectives

After completing this assignment, you should be able to:

* Use pandas to parse and analyze data
* Use matplotlib to chart data
* Clean data
* Store data in a relational database
* Extract data from a relational database

## Details

### Deliverables

* A Git repo called atus-analysis containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * an IPython notebook with your analysis
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

The U.S. Bureau of Labor Statistics publishes yearly data about Americans' use
of their time: [American Time Use Survey](http://www.bls.gov/tus/home.htm#data).
This data is used to find out information like how many hours the average person
spends per day doing household activities. You can see
[the 2013 survey results](http://www.bls.gov/news.release/atus.nr0.htm)
for more examples.

You will download the 2003-2013 multi-year files and use these to do analysis
over time. The questions you are trying to answer are up to you, but they
should:

* Show trends over time
* Compare different populations (people with children and people without, people
  of differing age groups, men and women, or other groupings)
* Answer macro-level questions and micro-level questions (for example, trends
  in the amount of leisure for the macro-level, trends in the types of things
  people do for leisure for the micro-level)

Your final analysis should be in the form of an IPython Notebook with both
narrative analysis and supporting charts. Your supporting code should be in
normal Python files.

You should have code to download the files you need and then load them into
a relational database. Further analysis can come from this database.


## Additional Resources

* [How to use ATUS microdata files](http://www.bls.gov/tus/howto.htm)
* [ATUS-X](https://www.atusdata.org/atus/) - tools to help get just the data
you need from ATUS.
* [PDFTables](https://pdftables.com/) - for extracting tables, such as the
activity lexicon, from PDF files.
* [Tabula](http://tabula.technology/) - another tool for extracting data from
PDFs.
