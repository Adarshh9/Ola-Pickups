import streamlit as st
import pandas as pd
import numpy as np

st.title('OLA PICKUPS IN BHIWANDI')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading the data......')
data = load_data(100000)
data_load_state.text('Loading Done!')


if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)


st.subheader('Number of pickups by hour')
hist_value = np.histogram(data[DATE_COLUMN].dt.hour ,bins=24,range=(0 ,24))[0]
st.bar_chart(hist_value)


hour_to_filter = st.slider('Hour',0,23,17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]


st.subheader('Maps of all pickups at %s:00'%hour_to_filter)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.296664,73.063121],
    columns=['lat', 'lon'])

st.map(df)