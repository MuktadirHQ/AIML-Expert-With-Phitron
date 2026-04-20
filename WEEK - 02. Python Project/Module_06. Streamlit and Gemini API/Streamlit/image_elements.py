import streamlit as st
st.title (" :streamlit: Input Your FILES", anchor=False)
st.divider()

st.audio("media/Name_in_the_Corner.mp3")

st.divider()
images = st.file_uploader("Enter Your Image : ", type=['jpg', "png", 'jpeg'], accept_multiple_files=True)
print(type(images))

if images:
    col = st.columns(len(images))
    
    for i, per_image in enumerate(images):
        with col[i]:
            st.image(per_image)
            

st.divider()
st.image("media/focus.jpg") # Storage
st.image("https://avatars.githubusercontent.com/u/57536328?v=4") # URL

