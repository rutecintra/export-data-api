#!/bin/bash
streamlit run app.py &
sleep 3
open http://localhost:8501  # For macOS
# xdg-open http://localhost:8501  # For Linux