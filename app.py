"""
UrbanRoof AI DDR Generator
Streamlit Web Interface
"""

import streamlit as st
import os
from extract_data import extract_text_and_images
from generate_ddr import generate_ddr


# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="UrbanRoof DDR Generator",
    page_icon="🏠",
    layout="wide"
)


# ---- HEADER ----
st.title("🏠 UrbanRoof AI Report Generator")

st.markdown(
"""
Generate **Detailed Diagnostic Reports (DDR)** from inspection and thermal documents.

Upload the reports below and the system will automatically analyze them.
"""
)

st.divider()


# ---- FILE UPLOAD SECTION ----
col1, col2 = st.columns(2)

with col1:
    inspection_file = st.file_uploader(
        "Upload Inspection Report",
        type=["pdf"]
    )

with col2:
    thermal_file = st.file_uploader(
        "Upload Thermal Report",
        type=["pdf"]
    )


st.divider()


# ---- GENERATE BUTTON ----
if st.button("Generate DDR Report"):

    if inspection_file and thermal_file:

        progress = st.progress(0)

        os.makedirs("temp", exist_ok=True)
        os.makedirs("extracted_images", exist_ok=True)

        st.write("Saving uploaded files...")
        progress.progress(20)

        inspection_path = "temp/inspection_report.pdf"
        thermal_path = "temp/thermal_report.pdf"

        with open(inspection_path, "wb") as f:
            f.write(inspection_file.read())

        with open(thermal_path, "wb") as f:
            f.write(thermal_file.read())


        st.write("Extracting data from inspection report...")
        progress.progress(40)

        inspection_text, inspection_images = extract_text_and_images(
            inspection_path,
            "extracted_images"
        )


        st.write("Extracting data from thermal report...")
        progress.progress(60)

        thermal_text, thermal_images = extract_text_and_images(
            thermal_path,
            "extracted_images"
        )


        all_images = inspection_images + thermal_images

        st.write("Generating AI diagnostic report...")
        progress.progress(80)

        report = generate_ddr(
            inspection_text,
            thermal_text,
            all_images
        )

        progress.progress(100)

        st.success("DDR Report Generated Successfully")

        st.subheader("UrbanRoof Diagnostic Report")

        st.markdown(report)


        # ---- SHOW IMAGES ----
        if all_images:

            st.subheader("Extracted Inspection Images")

            cols = st.columns(3)

            for i, img in enumerate(all_images):
                with cols[i % 3]:
                    st.image(img, use_container_width=True)

    else:

        st.warning("Please upload both reports before generating the DDR.")


# ---- FOOTER ----
st.divider()

st.markdown(
"""
UrbanRoof AI Inspection Assistant  
Automated building diagnostics using AI-driven report generation.
"""
)