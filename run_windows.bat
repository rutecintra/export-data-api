@echo off
start streamlit run app.py
timeout /t 3
start http://localhost:8501