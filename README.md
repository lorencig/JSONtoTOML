# 🧩 JSON to TOML and TOML to JSON Converter

## 🚀 Overview

This **Streamlit** app helps manage secrets for Streamlit applications by allowing users to easily convert **JSON** secret files into **TOML** format and vice versa. Streamlit's secret management system uses TOML files, and this app simplifies the process of converting between these formats, enabling users to quickly manage their secrets in the correct format. 🌟

> **Note**: This is a **personal project** and is **not affiliated with Streamlit**. 🛠️

## 🔧 Features

- **🔄 Convert JSON to TOML**: Upload or paste a JSON file, and the app will convert it into TOML format suitable for use with Streamlit's secret management system. 📦
- **🔄 Convert TOML to JSON**: Upload or paste a TOML file, and the app will convert it back into JSON format, making it easier to work with both formats. 🔄
- **⚡ Real-time Conversion**: The app supports both manual text input and file uploads for seamless conversion between formats. 🚀

## 🎯 Purpose

This tool was created to simplify the management of secrets in Streamlit applications. After encountering challenges while figuring out the correct configuration, I decided to build this app to streamline the process of converting JSON files into TOML format (and vice versa), which is essential for working with Streamlit’s secrets. 🎉

## 📝 How to Use

1. **🔄 Convert JSON to TOML**:
   - Upload your JSON secret file, or paste the content into the provided text box.
   - The app will automatically convert it into the correct TOML format, which you can then download. 📥

2. **🔄 Convert TOML to JSON**:
   - Upload your TOML secret file, or paste the content into the provided text box.
   - The app will convert the TOML data back into JSON format, which you can download. 📥

3. **📂 Access the Secret in Your Python Code**:
   - In your Streamlit app, you can access a secret by using:
     ```python
     st.secrets["key_name"]
     ```

4. **⚠️ Important TOML Structure**:
   - To create a secret key in the TOML file, it should be structured as follows:
     ```toml
     key_name = {}
     ```

## 🔒 Privacy & Data Handling

- **🚫 No Permanent Storage**: The app does **not** store any user data. All data (including uploaded files and pasted content) is processed temporarily during your session and is cleared once the session ends. 🔒
- **💾 Download Your Converted Files**: Ensure you download or copy your converted files before closing the app, as they are not saved automatically. 📥

## ⚡ Requirements

This app requires the following Python packages:
- `streamlit` 📊
- `toml` 📄
- `json` 🔠

You can install them using the following command:
```bash
pip install streamlit toml
```

## 🛑 Disclaimer
This project is a personal initiative and is not affiliated with Streamlit in any way. It is intended as a tool to simplify secret management for Streamlit applications and should be used at your own discretion. 🚧

## 📝 License
This project is licensed under the MIT License (Open Source) - see the LICENSE file for details. 📜

