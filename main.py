import streamlit as st
import dashboard
import ui_update
import ui_input
import ui_delete

# Sidebar
with st.sidebar:
    mode = st.radio(
        "Option",
        ("Dashboard", "User input", "User update", 'User delete')
    )

if mode == "Dashboard":
    dashboard.render()
elif mode == 'User input':
    ui_input.render()
elif mode == 'User update':
    ui_update.render()
elif mode == 'User delete':
    ui_delete.render()
else:
    st.write('please choose application mode on the sidebar')
