import streamlit as st
import pandas as pd
import time
from datetime import datetime

ts=time.time()#Records the real time
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
df = pd.read_csv("Attendance/Attendance_" + date + ".csv")#Creates the data frame for the given file
st.dataframe(df.style.highlight_max(axis=0))#Used to highlight the column