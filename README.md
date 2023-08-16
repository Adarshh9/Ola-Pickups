# OLA Pickups - Streamlit App

This Streamlit app visualizes OLA pickup data in Bhiwandi. It uses the Streamlit library along with Pandas and NumPy for data processing and visualization.

## Prerequisites

Before running the Streamlit app, ensure you have the following:

- Python 3.x installed on your system.
- Required Python packages: `streamlit`, `pandas`, `numpy`.

## Installation

1. Install the required Python packages:

```bash
pip install streamlit pandas numpy
```

## Usage

1. Clone the repository or download the script file.

2. Run the Streamlit app using the following command:

```bash
streamlit run your_script_name.py
```

Replace `your_script_name.py` with the actual name of your Python script.

3. The Streamlit app will open in your default web browser. You'll see a title "OLA PICKUPS IN BHIWANDI" and various interactive elements to explore the data.

## Features

- Data Loading: The app loads OLA pickup data from a provided URL and preprocesses it.
- Raw Data Display: You can choose to display the raw data by checking the "Show Raw Data" checkbox.
- Number of Pickups by Hour: The app displays a bar chart showing the number of pickups for each hour.
- Hourly Filter: Use the slider to filter the data based on the selected hour.
- Maps of Pickups: The app shows a map with randomly generated pickup points around Bhiwandi.

## Contributing

Contributions to this project are welcome. If you find any issues or want to enhance the project, feel free to create a pull request.

## Notes

- The data used in this app is fetched from the provided URL.
- The app is designed for educational and demonstrative purposes.

---
