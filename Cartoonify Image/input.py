import streamlit as st
from cartoonify_image import * 

st.title("Cartoonify")

col1, col2= st.columns([1,1])

with col1:
    st.markdown("## Reference")
    reference_face_upload = st.file_uploader("Upload an image")
    if reference_face_upload is not None:
        reference_face_image = Image.open(reference_face_upload)

with col2:
    st.markdown("## Converting")
    check_face_upload = st.file_uploader("Upload image for Conversion")
    if check_face_upload is not None:
        check_face_image = Image.open(check_face_upload)
        

if reference_face_upload is not None:
    with st.spinner("Converting to cartoon Image"):
        result = cartoonify(reference_face_image)
    if True in result:
        st.write("Conversion Succesful!")
    else:
        st.write("Conversion Failed!")
