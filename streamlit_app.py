import streamlit as st
from uuid6 import uuid6, uuid7, uuid8

def create():
    with tab1:
        st.subheader("UUID version 6")
        for i in range(10):
            st.write(uuid6())
    with tab2:
        st.subheader("UUID version 7")
        for i in range(10):
            st.write(uuid7())
    with tab3:
        st.subheader("UUID version 8")
        for i in range(10):
            st.write(uuid8())

tab1, tab2, tab3 = st.tabs(["UUID6", "UUID7", "UUID8"])

if st.button('Recreate'):
    tab1.empty()
    tab2.empty()
    tab3.empty()

create()