import streamlit as st
import requests
import config
from iex import IEXStock
from helpers import format_number
#input field for ticker symbol
symbol= st.sidebar.text_input("Symbol", value="AMZN")

#main stock
stock = IEXStock(config.IEX_API_TOKEN, symbol)
#main screen selection
screen = st.sidebar.selectbox("View", ("Overview", "Fundamentals", "News", "Ownership", "Technicals"))

st.write(symbol)

st.title(screen)
#gives an overview of the firm
if screen == 'Overview':
    logo = stock.get_logo()
    companyInfo = stock.get_companyInfo()

    col1, col2 = st.columns([1,4])

    with col1:
        st.image(logo['url'])
    
    with col2:
     st.subheader(companyInfo['companyName'])
     st.subheader("Description")
     st.write(companyInfo['description'])
     st.subheader("Industry")
     st.write(companyInfo['industry'])
     st.subheader('CEO')
     st.write(companyInfo['CEO'])



#shows fundamentals
if screen == 'Fundamentals':
    stats = stock.get_stats()

    st.subheader("Market Cap")
    st.write(format_number(stats['marketcap']))

    col1, col2 = st.columns([2,2])

    with col1:
        st.subheader("52 week High")
        st.write(stats["week52high"])
        st.subheader("Week 52 High Split Adjust Only")
        st.write(stats['week52highSplitAdjustOnly'])
        st.subheader("52 Week change")
        st.write(stats['week52change'])
        st.subheader("Average 30 day volume")
        st.write(stats["avg30Volume"])
        st.subheader("ttmEPS")
        st.write(stats["ttmEPS"])
        st.subheader("Dividend Yield")
        st.write(stats["dividendYield"])


 
    
    with col2:
     st.subheader("52 week Low")
     st.write(stats['week52low'])
     st.subheader("Week 52 Low Split Adjust Only")
     st.write(stats['week52lowSplitAdjustOnly'])
     st.subheader("Shares Outstanding")
     st.write(stats["sharesOutstanding"])
     st.subheader("Average 10 day volume")
     st.write(stats["avg10Volume"])
     st.subheader("ttmDividendRate")
     st.write(stats["ttmDividendRate"])

    


    


    
    

