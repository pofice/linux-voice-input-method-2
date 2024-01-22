import streamlit as st
import pyperclip 

st.title("RTX语音输入法")

# Get the state of the input box
state = st.session_state

# Check if the input box state exists
if "user_input" not in state:
    # Initialize the input box state
    state.user_input = ""

# Create an input box
state.user_input = st.text_input("请在此输入", state.user_input)

# Check if user input is not empty
if state.user_input:
    # Copy user input to clipboard
    pyperclip.copy(state.user_input)
    st.success("文本已成功复制到剪贴板！")

# Create a button to clear the input box
if st.button("清除输入记录"):
    # Clear the input box state
    state.user_input = ""