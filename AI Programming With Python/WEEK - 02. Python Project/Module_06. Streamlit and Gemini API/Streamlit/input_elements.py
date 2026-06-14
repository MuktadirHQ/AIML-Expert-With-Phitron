import streamlit as st
st.title (" :streamlit: Input Your Information", anchor=False)

name = st.text_input("Enter Your Name : ")
st.write("Your Name is : ", name)
print(type(name))


age = st.number_input("Enter Your Age : ", value=None, placeholder="Type Your Age Here")
print(type(age))
st.write("Your Age is : ", age)

st.divider()

password = st.text_input("Enter Your Password : ", type="password")
print(type(password))
st.write("Your Password is : ", password) 

pressed = st.button("Enter to confirm", type="primary")

selected = st.selectbox("Choose Your Profession", ("Student", "Teacher", "Businessman"),
                        index=None, 
                        accept_new_options=True
                        )

print(type(selected))
st.write("You Selected : ", selected)


if pressed:
    st.write(f"Your name is {name} and your age is {age}")