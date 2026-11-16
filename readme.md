# Simple Data Export Project

## Project Overview
This project uses Python and Pandas to clean a retail sales dataset and export the cleaned data into CSV and Excel formats.

## Project Objective
To learn basic data cleaning, data manipulation, and data exporting using Python.

## Technologies Used
- Python
- Pandas
- Openpyxl
- VS Code

## Project Features
- Reads a CSV dataset.
- Displays dataset information.
- Removes duplicate records.
- Handles missing values.
- Cleans column names and text values.
- Calculates total sales.
- Exports cleaned data into CSV format.
- Exports cleaned data into Excel format.
- Verifies exported files.

## Project Structure

```text
SIMPLE-DATA-EXPORT/
├── data/
│   └── retail_sales.csv
├── output/
│   ├── cleaned_sales.csv
│   └── cleaned_sales.xlsx
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Install the required libraries:

```bash
py -m pip install -r requirements.txt
```

## How to Run

Run the following command:

```bash
py main.py
```

## Output Files
1. cleaned_sales.csv
2. cleaned_sales.xlsx

Both files are saved inside the output folder.

## Sales Calculation

Total Sales = Quantity × Price

## Conclusion
This project demonstrates how to