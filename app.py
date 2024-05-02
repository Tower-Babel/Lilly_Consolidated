import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.markdown("<h1 style='color: #e87723;'>Eli Lily Consolidated Revenue</h1>", unsafe_allow_html=True)

df = pd.read_csv("sheet2.csv")
cash_flow = pd.read_csv("cashflow.csv")

# filter and melt cash_flow dataFrame
filtered_cash_flow = cash_flow[cash_flow['Line Item'].isin(['Total Revenue', 'Gross Profit', 'Net Sales', 'Total Operating Expense'])]
reshaped_line_items = pd.melt(filtered_cash_flow, id_vars='Line Item', var_name='Year', value_name='Values')
reshaped_line_items['Values'] = pd.to_numeric(reshaped_line_items['Values'], errors='coerce')


col1, col2, col3 = st.columns(3)

#dropdown menu
selected_year1 = col1.selectbox("Select Year 1", sorted(reshaped_line_items['Year'].unique()))
selected_year2 = col2.selectbox("Select Year 2", sorted(reshaped_line_items['Year'].unique()))

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

#filter
selected_drugs = drug_categories[selected_category]
df_selected = df[df["Item"].isin(selected_drugs)]

selected_year1 = int(selected_year1)
selected_year2 = int(selected_year2)

df_selected_year1 = df_selected[df_selected["Year"] == selected_year1][["Year", "Item", "Values"]].sort_values(by='Values', ascending=False)
df_selected_year2 = df_selected[df_selected["Year"] == selected_year2][["Year", "Item", "Values"]].sort_values(by='Values', ascending=False)

# create viz
fig2 = make_subplots(rows=1, cols=2, shared_yaxes=True, shared_xaxes=True)

fig2.add_trace(go.Bar(x=df_selected_year1['Values'], y=df_selected_year1['Item'], orientation='h', opacity=0.6, width=0.7, name=str(selected_year1), hovertemplate='%{x}', marker=dict(color='#e87723')), row=1, col=1)
fig2.add_trace(go.Bar(x=df_selected_year2['Values'], y=df_selected_year2['Item'], orientation='h', opacity=0.6, width=0.5, name=str(selected_year2), hovertemplate='%{x}', marker=dict(color='grey')), row=1, col=1)

fig2.update_layout(barmode='overlay', title=f"{selected_category}", xaxis_title='Revenue', yaxis_title='Drug')
st.plotly_chart(fig2)


#Go back and clean data for years 2014-2020 and upload to csv