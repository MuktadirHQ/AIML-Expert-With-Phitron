import streamlit as st
st.title (" :streamlit: Input Your FILES", anchor=False)
st.divider()

st.video("media/video.mp4")
st.divider()


video = st.file_uploader("Enter Your Video : ",
                         type = ["mp4", "MPEG4", 'mkv'],
                         )

print(type(video)) # LIST, accept_multiple_files=True
button = st.button("Click to Upload")

if button:
    if video:
        st.success("Your file is uploaded successfully")
        st.video(video)
    else:
        st.error("You must upload a file")