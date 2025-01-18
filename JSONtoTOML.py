import streamlit as st
import json
import toml
def convert_json_to_toml(json_content):
    try:
        json_data = json.loads(json_content)
        toml_data = toml.dumps(json_data)
        return toml_data
    except Exception as e:
        return f"Error: {e}"
def convert_toml_to_json(toml_content):
    try:
        toml_data = toml.loads(toml_content)
        json_data = json.dumps(toml_data, indent=4)
        return json_data
    except Exception as e:
        return f"Error: {e}"
st.set_page_config(page_title="JSON to TOML Converter and vice versa", layout="wide")
st.markdown("<h1 style='text-align: center;'>JSON to TOML or TOML to JSON Converter</h1>", unsafe_allow_html=True)
st.markdown("""
    "This Streamlit app is designed to simplify the management of secrets for your Streamlit applications (after I personally spent hours figuring out the right configuration). You can easily convert your JSON secret files into TOML format, which is the correct format for Streamlit's secret management system, or for any other purposes. Additionally, the app allows you to convert TOML files back into JSON format, making it easier to work with both formats and verify the conversion."
    
    **Important**: 
    - To create a secret key in the TOML, it should be structured like this:
      ```toml
      key_name = {}
      ```
    - In your Python code, access the secret using:
      ```python
      st.secrets["key_name"]
      ```

    For more details, refer to [Secrets Management from Streamlit](https://www.notion.so/snowflake-corp/Secrets-Management-730c82af2fc048d383d668c4049fb9bf). """)
st.markdown('##')
col1, col2 = st.columns([2, 3])
with col1:
    st.subheader("INPUT")
    file_type = st.radio("Choose file type to convert", ("JSON to TOML", "TOML to JSON"), key="file_type", label_visibility="collapsed")
    if file_type == "JSON to TOML":
        uploaded_json_file = st.file_uploader("Upload a JSON file", type="json", key="json_file")
        json_text = st.text_area("Or paste your JSON here", height=300, key="json_text")
        if uploaded_json_file is not None:
            json_text = uploaded_json_file.read().decode("utf-8")
    elif file_type == "TOML to JSON":
        uploaded_toml_file = st.file_uploader("Upload a TOML file", type="toml", key="toml_file")
        toml_text = st.text_area("Or paste your TOML here", height=300, key="toml_text")
        if uploaded_toml_file is not None:
            toml_text = uploaded_toml_file.read().decode("utf-8")
    if st.button("Clear", key="clear_button"):
        st.session_state.json_text = ""
        st.session_state.toml_text = ""
        st.session_state.file_type = "JSON to TOML"  
with col2:
    st.subheader("OUTPUT")
    if file_type == "JSON to TOML":
        if json_text.strip():
            toml_text = convert_json_to_toml(json_text)
            if toml_text.startswith("Error"):
                st.error(toml_text)
            else:
                st.text_area("Generated TOML", toml_text, height=300)
                st.download_button(
                    label="Download TOML",
                    data=toml_text,
                    file_name="secrets.toml",
                    mime="text/plain",
                )
                st.button("Copy to Clipboard", on_click=st.experimental_set_query_params, args=("clipboard", toml_text))
        else:
            st.info("Please upload a JSON file or paste JSON content to convert.")
    elif file_type == "TOML to JSON":
        if toml_text.strip():
            json_text = convert_toml_to_json(toml_text)
            if json_text.startswith("Error"):
                st.error(json_text)
            else:
                st.text_area("Generated JSON", json_text, height=300)
                st.download_button(
                    label="Download JSON",
                    data=json_text,
                    file_name="secrets.json",
                    mime="application/json",
                )
                st.button("Copy to Clipboard", on_click=st.experimental_set_query_params, args=("clipboard", json_text))
        else:
            st.info("Please upload a TOML file or paste TOML content to convert.")
st.markdown('##')
st.markdown("""
    <div style="text-align: center;">
        <strong>Important Notice:</strong><br><br>
        <strong> (Not affiliated with Streamlit).</strong> Your data (including uploaded files and pasted content) is processed temporarily during your session and is not stored or saved beyond that. Once the session ends, all data is cleared. The app does not save or store any user data on the server. All data is processed in-memory and discarded after the session.
    </div>
""", unsafe_allow_html=True)
