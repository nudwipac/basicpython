import streamlit as st
import qrcode
from datetime import datetime

# function CLEAR


def clear_text():
    st.session_state.clear["input"] = ""


# input data
st.title("QR Code Generator program")
data = st.text_input("Pls enter data : ", key="input")
data_placeholder = st.empty()

# Button to gen QR
if st.button("gen QR code"):
    if data:  # not null
        img = qrcode.make(f'{data}')
        img_path = f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png"
        img.save(img_path)
        # preview image
        st.image(img_path, width=300)
        st.success("QR code saved successfully")
        # clear data
        # data.clear()
    else:
        st.warning("Pls enter data before click button")
