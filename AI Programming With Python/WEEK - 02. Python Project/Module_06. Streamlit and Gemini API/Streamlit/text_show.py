import streamlit as st
st.title(" :streamlit: My First Streamlit App", anchor=False)
st.header("Content-1", divider=True)
st.subheader("Content-2", divider=True)
st.text("Hello this is a text Line")


st.markdown(":red[**Hello**], *World!*")
st.markdown(":green[**Hello**], *World!*")
st.markdown(":red-background[**Hello**, *World!*] :open_mouth:")

a = 10
b = 20
st.write(a, b)