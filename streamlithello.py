import streamlit as st

# Basic command
st.title("Hello Streamlit")
st.header("Header line")
st.subheader("Subheader line")
st.markdown("**Markdown** line")
st.code("print('Hello Streamlit')", language="python")
st.latex('''(a+b)^2 = a^2+ 2ab + b^2''')

# Button
if st.button("Click me"):
    st.write("You clicked button!")
else:
    st.write("Pls click button")

# Input text
data = st.text_input("pls input data here")
if st.button("Submit"):
    st.write(f"Your data is {data}")

# Slider
score = st.slider("Pls enter your score",
                  min_value=0,
                  max_value=10,
                  value=3)
st.write(f"your score is {score}")
