import streamlit as st
import time
import threading
from steamlite import globlerror, main

# Set page title and configuration
st.set_page_config(
    page_title="GPay URL Scraper Monitor",
    page_icon="🔍",
    layout="wide"
)

# Create header
st.title("GPay URL Scraper Monitor")

# Create a placeholder for the error message
error_placeholder = st.empty()

# Start the worker thread in the background
worker_thread = threading.Thread(target=main)
worker_thread.daemon = True  # Make thread terminate when main program exits
worker_thread.start()

# Display the current global error with automatic refresh
while True:
    if globlerror:
        error_placeholder.error(f"Current Error: {globlerror}")
    else:
        error_placeholder.success("No errors currently")
    
    # Add metrics or status indicators
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Status", value="Running")
    with col2:
        st.metric(label="Last Updated", value=time.strftime("%H:%M:%S"))
    
    # Sleep for a while before refreshing
    time.sleep(1)