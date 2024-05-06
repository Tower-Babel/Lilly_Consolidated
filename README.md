![image](https://github.com/Tower-Babel/Lilly_Consolidated/assets/123087201/c866632e-63f9-47f1-a9df-80a4d1b40c9e)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://eli-lilly.streamlit.app/)

**Eli-Lilly's Trillion Dollar Dream**

In the technology industry, the term "FAANG" relates to the largest and most influential companies in the world: Facebook, Amazon, Apple, Netflix, and Google. 
In the pharmaceutical industry, companies like Eli Lilly have the potential to join the levels of FAANG if they reach a valuation of 1 trillion dollars. As one of the leading pharmaceutical companies, Eli Lilly has a good history of innovation and a diverse portfolio of products.
#
>"Pharmaceutical companies often possess a strong economic moat derived from their exclusive patents on life-saving drugs, enabling them to charge high prices and maintain a loyal customer base. This moat, built on patients' reliance on medication and the high cost of entry for competitors, provides a significant barrier to entry in the industry." - Five Successful Stock Investing Principles, Morningstar
#
If Eli Lilly were to achieve a trillion-dollar valuation, it would not only signify its financial success but also its significant impact on healthcare. Other pharmaceutical companies such as Pfizer, Johnson & Johnson, and Merck also compete in the industry. 

**Data Sources and Preparation**
- https://www.lilly.com/our-medicines/current-medicines
- https://investor.lilly.com/financial-information/fundamentals/income-statement
- https://www.sec.gov/edgar/browse/?CIK=59478

Data was collected from 3 sources and cleaned in Excel and Python. The data was joined on Year field and missing data was replaced with 0 if there was no other data points to verify drug existing in past.

 **Use Case**
 
 Sales and performance can be monitored usig the dashboard. High performing products can be spoted and and tracked to reach net sale goals.

 **Dashboard Features**
 - Analyze top performing products by year
 - View products description
 - Compare net sales for the year

**Future Work**

The clean data files includes 8 years of product data. In the future the visuals can be updated to include more years to show the spike in product revenue. The dashboard can be updated to include more sources and revenue cycles

**Streamlit Dashboard**

https://eli-lilly.streamlit.app/

**Instructions**

If you are viewing dashboard in dark-mode, be sure to change settings to lightmode

-A. Select far right corner button *may not appear right away

![image](https://github.com/Tower-Babel/Lilly_Consolidated/assets/123087201/6551e0b6-d5eb-4ddc-84c7-6c235009938e)



-B. After drop-down appears select settings
-C. Select 'Dark' in settings and switch to light
![image](https://github.com/Tower-Babel/Lilly_Consolidated/assets/123087201/1d984a5a-ac2b-46e0-960b-b2e4a9bbf8d8)

![image](https://github.com/Tower-Babel/Lilly_Consolidated/assets/123087201/7b49bd8c-af96-45af-818c-34580aa47ab8)

1. Select from a category of Eli Lilly Drugs
2. Within the category analyze the drug revenue that makes up the Net Sales
3. Change the year to compare different revenue years
4. Visualize the revenue and compare it between other drugs within the same category
5. Analyze the drug by year
6. Dig in to the drug description powered by wiki

