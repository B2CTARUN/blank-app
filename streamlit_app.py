import cv2
import numpy as np
import streamlit as st
from pyzbar.pyzbar import decode
from streamlit_camera_input import camera_input

def main():
    st.title("Real-time QR Code Scanner")

    # Continuous camera input
    frame = camera_input("Capture QR Code")

    if frame is not None:
        # Decode QR codes in the frame
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            st.success(f'Scanned QR Code Data: {qr_data}')
            break  # Stop after the first QR code is found

        # Convert the frame to RGB format for Streamlit
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame_rgb, channels="RGB", use_column_width=True)

if __name__ == "__main__":
    main()
