import streamlit as st
from docx import Document
from docx.shared import Inches

def generate_biodata():
    # ... (rest of your code remains the same)

    # Download the document
    if st.button("Generate Biodata"):
        doc.save(f"{full_name}_Biodata.docx")  # Save the document

        # Read the file contents as binary data
        with open(f"{full_name}_Biodata.docx", "rb") as file:
            biodata_content = file.read()  

        st.download_button(
            label="Download Biodata",
            data=biodata_content,  # Pass the binary data
            file_name=f"{full_name}_Biodata.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

if __name__ == "__main__":
    st.set_page_config(page_title="Biodata Generator")
    st.title("Biodata Generator for Marriage")
    generate_biodata()
