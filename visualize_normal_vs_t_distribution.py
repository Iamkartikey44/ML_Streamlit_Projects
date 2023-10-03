import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


st.set_page_config(page_title="Normal VS t-Distribution Comparison",layout='wide')
st.title("Normal and t-distribution Comparison")

with st.sidebar:
    st.header("Input Parameters")
    degress_of_freedom = st.slider("Degrees of Freedom",1,100,5,1)

#Generating data for normal distribution
x = np.linspace(-5,5,1000)
y_norm = stats.norm.pdf(x)

#Generating data for t-distribution
y_t = stats.t.pdf(x,df=degress_of_freedom)

#Create the plot
fig,ax = plt.subplots(figsize=(10,6))

ax.plot(x,y_norm,label="Normal Distribution",color='blue')
ax.plot(x,y_t,label=f"Student's t-distribution (df={degress_of_freedom})",color='red')
ax.set_xlabel("x")
ax.set_ylabel("Probability Density")
ax.set_title("Normal and t-distribution Comparison")
ax.legend()

#Display the plot
st.pyplot(fig)
