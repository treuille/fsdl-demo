import streamlit as st

num_hellos = st.slider("Num hellos 2", 1, 100)
if st.checkbox("Set the text?"):
    the_text = st.text_input("Something to repeat")
else:
    the_text = "Hello world"
for i in range(num_hellos):
    st.write(i, the_text)
