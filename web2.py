import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

content = """Apple designs Macs, the best personal computers in the world, along with OS X, iLife, iWork, and professional software. Apple leads the digital music revolution with its iPods and iTunes online store. Apple has reinvented the mobile phone with its revolutionary iPhone and App Store, 
            and is defining the future of mobile media and computing devices with iPad."""""
st.info(content)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data (1).csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])


