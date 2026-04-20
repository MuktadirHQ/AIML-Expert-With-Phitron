import streamlit as st
st.title (" :streamlit: Input Your FILES", anchor=False)
st.divider()

st.audio("media/Name_in_the_Corner.mp3")
st.divider()


audio = st.file_uploader("Enter Your Audio : ",
                         type = ["mp3", "flac", 'ogg'],
                         )
print(type(audio)) # LIST, accept_multiple_files=True

if audio:
    st.audio(audio)