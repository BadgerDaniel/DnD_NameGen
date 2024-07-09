import pandas as pd
import random as rm
import numpy as np
#import will2live
import streamlit as st
df=pd.read_csv('NameGenerator.csv')
df.drop(['No.'],axis=1,inplace=True)
df.rename(columns={'+ Noun (a)':'Noun (a)','+ Noun (b)':'Noun (b)'},inplace=True)

#  define the varied naming methods
methods = [
    lambda row: f"{row['First Name']} {row['Epithet (a)']}-{row['Noun (a)']}",
    lambda row: f"{row['First Name']} {row['Epithet (b)']}-{row['Noun (b)']}",
    lambda row: f"{row['First Name']} {row['Epithet (a)']}-{row['Noun (b)']}",
    lambda row: f"{row['First Name']} {row['Epithet (b)']}-{row['Noun (a)']}",
    lambda row: f"{row['First Name']} The {row['Epithet (a)'].capitalize()}",
    lambda row: f"{row['First Name']} The {row['Epithet (b)'].capitalize()}",
    lambda row: f"{row['First Name']} The {row['Noun (a)'].capitalize()}",
    lambda row: f"{row['First Name']} The {row['Noun (b)'].capitalize()}",
]

# func to generate 5 names
def generate_names(df, n=5):
    names = []
    for _ in range(n):
        row = df.sample().iloc[0]  # Randomly pick a row
        method = rm.choice(methods)  # Randomly pick a method
        name = method(row)
        names.append(name)
    return sorted(names)  # Sort names alphabetically




# Initialize session state
if 'batch_counter' not in st.session_state:
    st.session_state.batch_counter = 0
if 'names' not in st.session_state:
    st.session_state.names = []

# Streamlit app layout
st.title("Random Fantasy Name Generator")

if st.button("Generate Names"):
    st.session_state.batch_counter += 1
    batch_name = f"\~Batch {st.session_state.batch_counter}\~"
    new_names = generate_names(df)
    st.session_state.names.append((batch_name, new_names))

# Display the names
for batch_name, names in st.session_state.names:
    st.write(batch_name)
    for name in names:
        st.write(name)
#%%
