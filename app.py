import streamlit as st
import pandas as pd

slider = st.slider("This is a slider.")
df = pd.read_csv('https://nightly.omniscope.me/Richard/timeSeries.csv?download')

st.dataframe(df)  # Same as st.write(df)

code = '''
import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

slider = st.slider("This is a slider.")
df = pd.read_csv('https://nightly.omniscope.me/Richard/timeSeries.csv?download')

st.dataframe(df)  # Same as st.write(df)

'''
st.code(code, language='python')
