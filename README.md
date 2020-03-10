

The data is from a kaggle competition, you can find it here : https://www.kaggle.com/carrie1/ecommerce-data/kernels  

<div>
<img src="https://cdn.pixabay.com/photo/2016/09/30/19/10/ecommerce-1706103_1280.png" width="150" align="right"/>
</div>

It contians information from transactions from a UK retailer. The fields are: 
- InvoiceNo: purchase identifier
- StockCode: product identifier
- Description: description of the product
- Quantity: amount of items for that product that are contained in the purchase
- InvoiceDate: date of the purchase
- UnitPrice: price of the product
- CustomerID: customer identifier 
- Country: country that purchase took place

The examples provided are: 

1. [Data Cleaning:](data_cleaning.ipynb) clean the data, filling missing inforation
2. [Data Exploration:](data_exploration.ipynb) see how the data is distributed, find outliers  
3. [Clustering:](clustering.ipynb) perform clustering methods to find patterns in the data
4. [Classification:](classification.ipynb) classify sales according to the money spent 
5. [Recommender System:](recommender-system.ipynb) generate recommendations based on the users' history 


The examples 2,3,4 and 5 use the cleaned data result from the data cleaning process.

**TODO: document how to create environment*
