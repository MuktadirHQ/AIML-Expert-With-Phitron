import streamlit as st
st.header("Notes Summarry and Quiz Generator", anchor=False)
st.markdown("Upload upto 3 images to generate Note summarray and Quizzes")
st.divider()


with st.sidebar:
    st.header("Controls")
    
    images = st.file_uploader(
        "Upload The photos of your note",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )
    st.subheader("Your uploaded Images")
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            
            
            
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
                    
                    
    selected = st.selectbox("Enter the difficulty of your quiz", 
                 ("Easy", 'Medium', "Hard"),
                 index=None
                 )
    
    ini_button = st.button("Initiate", type="primary")
    
if ini_button:
    if not images:
        st.error("You must upload at least 1 Image")
    if not selected:
        st.error("You must select a difficulty")
        
    if images and selected:
        
        with st.container(border=True):
            st.subheader("Your Note", anchor=False)
            st.text("Note will be shown")

        with st.container(border=True):
            st.subheader("Audio Transcription", anchor=False)
            st.text("Will be shown here.")
       
            
        with st.container(border=True):
            st.subheader(f"Quiz ({selected}) Difficulty", anchor=False)
            st.text("Will be shown here.")
    
    