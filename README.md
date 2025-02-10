# API Data Query Application

A user-friendly interface to query API data and export results to Excel. Now with one-click execution!

![API Data Query Demo](assets/apidataquery.png)

## Features
- One-click launch (Windows/macOS/Linux)
- Multi-period query capability
- Automatic pagination handling
- Excel export functionality
- Data preview in app

## Requirements
- Python 3.7+
- Streamlit
- Pandas
- Requests
- Openpyxl (for Excel export)

## Installation
```bash
git clone https://github.com/rutecintra/export-data-api.git
cd export-data-api
pip install -r requirements.txt
```

## Quick Start

### Windows
1. Install [Python 3.7+](https://www.python.org/downloads/)
2. Double-click `install_dependencies.bat`
3. Double-click `run_windows.bat`

### macOS/Linux
1. Install Python 3.7+:
```bash
brew install python  # macOS
sudo apt-get install python3 python3-pip # Linux
```
2. Make scripts executable:
```bash
chmod +x install_dependencies.sh run_mac_linux.sh
```
3. Double-click or run:
```bash
./install_dependencies.sh
./run_mac_linux.sh
```