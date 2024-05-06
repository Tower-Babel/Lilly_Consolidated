import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import wikipedia

st.write("#")
st.markdown("<h1 style='color: #e87723; font-family: High Tower Text;'>Eli Lily Consolidated Revenue*</h1>", unsafe_allow_html=True)


df = pd.read_csv("output_file.csv")
cash_flow = pd.read_csv("cashflow.csv")


# filter and melt cash_flow dataFrame
filtered_cash_flow = cash_flow[cash_flow['Line Item'].isin(['Total Revenue', 'Gross Profit', 'Net Sales', 'Total Operating Expense'])]
reshaped_line_items = pd.melt(filtered_cash_flow, id_vars='Line Item', var_name='Year', value_name='Values')
reshaped_line_items['Values'] = pd.to_numeric(reshaped_line_items['Values'], errors='coerce')

def page1():
    
    ### code from template https://environmental-news.streamlit.app/
    st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css?family=Heebo'); 
    @import url('https://fonts.googleapis.com/css?family=Heebo:400,600,800,900');  

    body * { 
        -webkit-font-smoothing: subpixel-antialiased !important; 
        text-rendering:optimizeLegibility !important;
    }

    body hr {
        border-bottom: 1.5px solid rgba(23, 48, 28, 0.5); 
    }


    /*
    #MainMenu {visibility: hidden;}
    */
    footer {visibility: hidden;}

    div.stButton p {
        font-family: "Heebo";
        font-weight:600;
        font-size: 15px;
        letter-spacing: 0.25px;
        padding-top: 1px;
    }

    section[data-testid="stSidebar"] {
        top: 5rem;
        width: 200px !important; 
        background-color:#CDD4D0;
        background: #F6F4F0;
        border-right: 1.5px solid rgba(23, 48, 28, 0.5);
    }


    header[data-testid="stHeader"] {
        background: url('https://drive.google.com/file/d/1euw09JkxS3jBIdofP6kbSdrJIouPtnFP/view?usp=sharing');
        background-size: contain ;
        background-repeat: no-repeat;
        background-color: rgb(23, 48, 28);
        height: 5rem;
    }


    div[data-testid="stMarkdownContainer"] h2 {
        font-family:'Heebo';
        font-weight: 800;
        letter-spacing: 0.25px;
    }


    .appview-container {
        background: radial-gradient(rgba(23, 48, 28, 0.7), transparent);
        background: #F6F4F0;
    }
    div[data-testid="stExpander"] > details {
        bordder-radius: 0;
        border-color: rgba(255, 255, 255, 0.05);
        max-width: 74rem;
    }


    div[data-testid="stExpander"] > details > summary:hover {
        color: rgb(23, 48, 28);
    }
    
    div[data-baseweb="select"] {
        font-family: "Heebo";
        font-weight:600;
        font-size: 15px;
        letter-spacing: 0.25px;
    }


    div[data-baseweb="select"] div {
        background-color: rgba(23, 48, 28, 0.95);
        color: #F6F4F0;
        border: 0px;
    }

    div[data-baseweb="select"] svg {
        color: #F6F4F0;
    }


    </style>
    ''', unsafe_allow_html=True)
    ###

    col1, col2, col3 = st.columns(3)

    #dropdown menu
    #selected_year1 = col1.selectbox("Select Year 1", sorted(reshaped_line_items['Year'].unique()))
    #selected_year2 = col2.selectbox("Select Year 2", sorted(reshaped_line_items['Year'].unique()))
    available_years = sorted(reshaped_line_items['Year'].unique())
    available_years = [year for year in available_years if int(year) in [2021, 2022, 2023]]
    selected_year1 = col1.selectbox("Select Year 1", available_years)
    selected_year2 = col2.selectbox("Select Year 2", available_years)

    df_year1 = df[df['Year'] == selected_year1]
    df_year2 = df[df['Year'] == selected_year2]

    reshaped_line_items_year1 = reshaped_line_items[reshaped_line_items['Year'] == selected_year1]
    reshaped_line_items_year2 = reshaped_line_items[reshaped_line_items['Year'] == selected_year2]

    #KPI 1
    for kpi in reshaped_line_items_year1['Line Item'].unique():
        kpi_value = reshaped_line_items_year1.loc[reshaped_line_items_year1['Line Item'] == kpi, 'Values'].values[0]
        # Format the value according to the KPI
        formatted_value = f"${kpi_value / 1e3:.1f}B" 
        #if kpi == 'Net Income/Starting Line':
            #formatted_value = f"${kpi_value / 1e3:.1f}B"
        #if kpi == 'Total Revenue':
            #col1.metric(label=kpi + f" ({selected_year1})", value=formatted_value)
        #elif kpi == 'Gross Profit':
            #col1.metric(label=kpi + f" ({selected_year1})", value=formatted_value)
        if kpi == 'Net Sales':
            col1.metric(label=kpi + f" ({selected_year1})", value=formatted_value)    
        #elif kpi == 'Total Operating Expense':
            #col1.metric(label=kpi + f" ({selected_year1})", value=formatted_value)    

    #KPI 2
    for kpi in reshaped_line_items_year2['Line Item'].unique():
        kpi_value = reshaped_line_items_year2.loc[reshaped_line_items_year2['Line Item'] == kpi, 'Values'].values[0]
        # Format the value according to the KPI
        formatted_value = f"${kpi_value / 1e3:.1f}B"  
        #if kpi == 'Net Income/Starting Line':
        #formatted_value = f"${kpi_value / 1e3:.1f}B"  
        #if kpi == 'Total Revenue':
            #col2.metric(label=kpi + f" ({selected_year2})", value=formatted_value)
        #elif kpi == 'Gross Profit':
            #col2.metric(label=kpi + f" ({selected_year2})", value=formatted_value)
        if kpi == 'Net Sales':
            col2.metric(label=kpi + f" ({selected_year2})", value=formatted_value)    
        #elif kpi == 'Total Operating Expense':
            #col2.metric(label=kpi + f" ({selected_year2})", value=formatted_value)    

    drug_categories = {
        "Diabetes and Obesity": ["Trulicity®", "Trulicity® | Outside U.S.", "Jardiance | U.S.", "Jardiance | Outside U.S.", "Humalog® | U.S.", "Humalog® | Outside U.S.", "Humulin® | U.S.", "Humulin® | Outside U.S.", "Basaglar | U.S.", "Basaglar | Outside U.S.", "Baqsimi | U.S.", "Baqsimi | Outside U.S.", "Zepbound® | U.S.", "Zepbound® | Outside U.S."],
        "Oncology": ["Verzenio® | U.S.", "Verzenio® | Outside U.S.", "Cyramza® | U.S.", "Cyramza® | Outside U.S.", "Erbitux® | U.S.", "Erbitux® | Outside U.S.", "Alimta® | U.S.", "Alimta® | Outside U.S."],
        "Immunology": ["Taltz® | U.S.", "Taltz® | Outside U.S.", "Olumiant | U.S.", "Olumiant | Outside U.S.", "Other immunology | U.S.", "Other immunology | Outside U.S."],
        "Neuroscience": ["Zyprexa® | U.S.", "Zyprexa® | Outside U.S.", "Emgality® | U.S.", "Emgality® | Outside U.S.", "Other neuroscience | U.S.", "Other neuroscience | Outside U.S."],
        "Other": ["Forteo® | U.S.", "Forteo® | Outside U.S.", "Cialis® | U.S.", "Cialis® | Outside U.S.", "COVID-19 antibodies | U.S.", "COVID-19 antibodies | Outside U.S.", "Other | U.S.", "Other | Outside U.S."]
    }

    #sidebar
    selected_category = st.sidebar.selectbox("Select Drug Category", list(drug_categories.keys()))

    col3.write("#")
    col3.write("#")
    col3.write("#")
    col3.write("(*Net Sales include the total sales from all five drug categories)")

    selected_drugs = drug_categories[selected_category]
    df_selected = df[df["Item"].isin(selected_drugs)]

    selected_year1 = int(selected_year1)
    selected_year2 = int(selected_year2)
    df_selected['Year'].astype(int)

    df_selected_year1 = df_selected[df_selected["Year"] == selected_year1][["Year", "Item", "Values"]].sort_values(by='Values', ascending=False)
    df_selected_year2 = df_selected[df_selected["Year"] == selected_year2][["Year", "Item", "Values"]].sort_values(by='Values', ascending=False)

    #percent_change = ((df_selected_year2['Values'].values[0] - df_selected_year1['Values'].values[0]) / df_selected_year1['Values'].values[0]) * 100
    #df_year1 = df[df['Year'] == selected_year1]
    #df_year2 = df[df['Year'] == selected_year2]

    # create viz
    fig2 = make_subplots(rows=1, cols=2, shared_yaxes=True, shared_xaxes=True)

    fig2.add_trace(go.Bar(x=df_selected_year1['Values'], y=df_selected_year1['Item'], orientation='h', opacity=0.6, width=0.7, name=str(selected_year1), hovertemplate=f'{selected_year1} Revenue: $%{{x}}M', marker=dict(color='#e87723')), row=1, col=1)
    fig2.add_trace(go.Bar(x=df_selected_year2['Values'], y=df_selected_year2['Item'], orientation='h', opacity=0.6, width=0.5, name=str(selected_year2), hovertemplate=f'{selected_year2} Revenue: $%{{x}}M', marker=dict(color='grey')), row=1, col=1)

    fig2.update_layout(barmode='overlay', title=f"{selected_category}", xaxis_title='Revenue (In millions of USD)', yaxis_title='Drug')

    st.plotly_chart(fig2)

    st.sidebar.write("Click on a drug name and scroll down on main page to see details below the chart")

    #st.sidebar.dataframe(df_selected['Item'].unique() )
    unique_items = df_selected['Item'].unique()
    #st.dataframe(unique_items[["Year", "Item", "Values"]])

    for item in unique_items:
        if st.sidebar.button(item):
            st.write(f"You clicked on: {item}")
            df_selected_item = df_selected[df_selected['Item'] == item]

            df_selected_year1 = df_selected_year1[df_selected_year1['Item'] == item]
            df_selected_year2 = df_selected_year2[df_selected_year2['Item'] == item]
            ##
            df_selected_year1['Values'] = df_selected_year1['Values'].astype(int)
            df_selected_year2['Values'] = df_selected_year2['Values'].astype(int)
            percent_change = ((df_selected_year2['Values'].values[0] - df_selected_year1['Values'].values[0]) / df_selected_year1['Values'].values[0]) * 100        
            percent_change= round(percent_change, 0)
            st.write(f' {selected_year1} and {selected_year2} Percent of change: **{percent_change}%**')
            
            df_selected_item['Year'] = df_selected_item['Year'].astype(str)
            df_selected_item['Values'] = df_selected_item['Values'].astype(str) + 'M'
            df_selected_item['Values'] = df_selected_item['Values'].apply(lambda x: '$' + str(x))
            st.dataframe(df_selected_item, hide_index =True )
            #st.dataframe(df_selected_item)
            
            item = item.split("®")[0].strip()
            item = item.replace('Outside U.S.', '').replace('U.S.', '').replace('|', '').strip()
            
            expander = st.expander(f" :mag: Click Here to See {item} Description")
            if item == "Jardiance":
                item = "Empagliflozin"
            elif item == "Humalog":
                item = "Insulin lispro"
            elif item == "Humulin":
                item = "Insulin (medication)"
            elif item == "alimta":
                item = "Pemetrexed"
            elif item == "Verzenio":
                item = "Abemaciclib"
            elif item == "Erbitux":
                item = "Cetuximab"
            elif item == "Alimta":
                item = "Pemetrexed"
            elif item == "taltz":
                item = "Ixekizumab"
            elif item == "Cialis":
                item = "Tadalafil"
            elif item == "Forteo":
                item = "Teriparatide"
            selected_item = item    
            if selected_item:
                try:
                    page = wikipedia.page(selected_item)
                    expander.write(f"## {page.title}")
                    expander.write(page.content)
                except wikipedia.exceptions.DisambiguationError as e:
                    expander.write(f"Disambiguation Error for '{selected_item}': {e}")
                except wikipedia.exceptions.PageError as e:
                    expander.write(f"Page Error for '{selected_item}': {e}")

# page 2
def page2():
    st.write(
        """
        **Eli Lilly's Trillion Dollar Dream**

        (If you are viewing this page in darkmode switch to lightmode)

        In the technology industry, the term "FAANG" refers to the largest and most influential companies in the world: Facebook, Amazon, Apple, Netflix, and Google. 
        In the pharmaceutical industry, companies like Eli Lilly have the potential to reach the levels of FAANG if they achieve a valuation of 1 trillion dollars. As one of the leading pharmaceutical companies, Eli Lilly has a strong history of innovation and a diverse portfolio of products.
        #
        >"Pharmaceutical companies often possess a strong economic moat derived from their exclusive patents on life-saving drugs, enabling them to charge high prices and maintain a loyal customer base. This moat, built on patients' reliance on medication and the high cost of entry for competitors, provides a significant barrier to entry in the industry." - Five Successful Stock Investing Principles, Morningstar
        #
        Achieving a trillion-dollar valuation would not only signify Eli Lilly's financial success but also its significant impact on healthcare. Other pharmaceutical companies such as Pfizer, Johnson & Johnson, and Merck also compete in the industry. 

        **Data Sources and Preparation**
        - [Eli Lilly's current medicines](https://www.lilly.com/our-medicines/current-medicines)
        - [Eli Lilly's financial information](https://investor.lilly.com/financial-information/fundamentals/income-statement)
        - [SEC filings for Eli Lilly](https://www.sec.gov/edgar/browse/?CIK=59478)

        Data was collected from three sources and cleaned using Excel and Python. The data was joined on the Year field, and missing data points were replaced with 0 if there was no other data available to verify the drug's existence in the past.

        **Use Case**
        
        The dashboard allows for monitoring sales and performance. High-performing products can be identified and tracked to reach net sales goals.

        **Dashboard Features**
        - Analyze top-performing products by year
        - View product descriptions
        - Compare net sales for different years

        **Future Work**

        The clean data includes the past 8 years, but visuals can be updated to include more years. The dashboard can also be expanded to include more data sources and revenue cycles.

        **Streamlit Dashboard**

        [Link to Eli Lilly Dashboard](https://eli-lilly.streamlit.app/)

        **Instructions**

        If you are viewing the dashboard in dark mode, be sure to change settings to light mode:

        1. Select the far right corner button (may not appear right away)
        2. After the drop-down appears, select settings
        3. In settings, select 'Dark' and switch to light mode

        Usage Instructions:
        1. Select a category of Eli Lilly drugs
        2. Within the category, analyze the drug revenue contributing to Net Sales
        3. Change the year to compare revenue from different years
        4. Visualize revenue and compare it between other drugs within the same category
        5. Analyze the drug by year
        6. Explore the drug description powered by Wikipedia
        """
    )



selected_page = st.sidebar.selectbox("Select Page", ("Home", "ReadMe"))

# selected page
if selected_page == "Home":
    page1()
elif selected_page == "ReadMe":
    page2()
