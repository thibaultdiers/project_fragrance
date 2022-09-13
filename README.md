# AI Perfumer (The Lab 2.0)

We explored the potential of data on perfumes (olfactory notes) to understand how note compositions influence successful fragrance formulas (i.e., the success of perfumes is assessed based on customer ratings). Our project was designed for helping perfumers to create unique and successful perfumes (i.e., given a combination of fragrance, predict the commercial success of a perfume).

Check out our LIVE Heroku Webpage here: http://fragrance-demo.herokuapp.com/

# General info

## Team Members

- Philine Oberhansberg
- Tiago Mendonça
- Thibault Diers

## Data Sources

Web Scraping Data : Fragrantica website

## Technologies

- Python
- Pandas
- Sklearn
- CSS
- BeautifulSoup
- JSON
- Streamlit

# Data Processing

The fragrantica.com website provided information on more than 4,000 perfumes and their olfactory notes including the following:
- Fragrance name and brand,
- Top notes, middle notes, and base notes, and
- Perfume rating (out of 5)
- Number of reviews

## Web Scraping

We used web-scraping to collect the above information on perfumes from the fragrantica.com website. Despite some web scraping limitations, and before cleaning the data, we were able to collect information about 4,834 perfumes. After cleaning the data, namely droping missing values and duplicates, we were able to scrape a total of 3,797 perfumes during the project timeframe (i.e., 2 weeks) as well as a total of 1,935 olfactory notes including 619 top notes, 787 middle notes and 529 base notes. 

## Encoding

### The features

The perfume notes are divided as top, middle and base notes. 

We used labelencoder to create a database where we treated the olfactory notes as features and assigned them different importance according to their corresponding compositional influence in typical perfumes: 
- top notes were marked as 0.2 since top notes generally make up about 20% of the blend,
- middle notes were marked as 0.7 since middle notes generally make up about 70% of the blend, and
- base notes were marked as 0.1 since base notes generally make up about 10% of the blend.

If a note was not an ingredient in the perfume, it was marked as 0. 

### The rating

We set our target feature out to be the rating of the perfumes, it was a binary classification. Based on the distributions of the review scores, we decided on a success threshold of 4.3. Hence, a value of "0" was assigned to all unsuccessful perfumes and a value of "1" to all perfumes with an average review score of above 4.3. 

## The Machine Learning Model

We trained various machine learning models (i.e., Logistic regression, Decision tree classifier, Catboost classifier, Adaboost classifier, Suport vector machine, Random Forest classifier) and picked our best model, namely Random Forest classifier (i.e., accuracy score of approx. 82%).
