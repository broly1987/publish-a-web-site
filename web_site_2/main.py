import streamlit as st
import pandas

data = {
  'series_1':[1,2,3,4,5],
  'series_2':[4,6,7,8,12]
}
dt = pandas.DataFrame(data)
st.title('our first website')
st.subheader('Introducing streamlit in Automate everything with python')
st.write('this is our first app')
st.write(dt)
