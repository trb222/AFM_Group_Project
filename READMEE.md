Stock Screener Application
This Stock Screener Application is a web-based tool built with Streamlit. It allows users to filter and score stocks based on specific financial metrics and investment strategies. The application calculates a custom score for each stock based on the selected investor type and presents the results in a tabular format, along with visualizations.

Features
User Input Filters: Filter stocks based on metrics such as PEG Ratio, Price-to-Book, Price/Earnings, Return on Equity, Dividend Yield, and Dividend Payout Ratio.
Custom Scoring System: Scores stocks based on selected investor types:
Value Investor
Growth Investor
Income Investor
Data Visualization: Provides bar chart visualizations for financial metrics and scores.
Exportable Results: Allows users to download the filtered results as a CSV file.
Interactive Interface: Simple and interactive UI for ease of use.
Table of Contents
Requirements
Installation
Running the Application
Program Functionality
Data Formatting
Scoring Interpretation
File Structure
Troubleshooting
License
Requirements
Ensure you have the following installed:

Python 3.7 or later
The following Python libraries:
streamlit
pandas
matplotlib
seaborn
Installation
Clone this repository or download the source files.

Install the required Python packages using the following command:

bash
Copy code
pip install -r requirements.txt
Make sure the requirements.txt file contains the necessary dependencies:

text
Copy code
streamlit
pandas
matplotlib
seaborn
Running the Application
Navigate to the folder containing the script and run the following command:

bash
Copy code
streamlit run <script_name>.py
Replace <script_name> with the name of the script file, e.g., stock_screener.py.

The application will open in your default web browser. If it doesn't, copy the URL shown in the terminal (usually http://localhost:8501) and open it in a browser.

Program Functionality
Filtering Stocks
Users can filter stocks based on the following criteria:

PEG Ratio: Min/Max range
Price-to-Book Ratio: Min/Max range
Price/Earnings Ratio: Min/Max range
Return on Equity: Minimum percentage
Dividend Yield: Minimum percentage
Dividend Payout Ratio: Maximum percentage
Scoring System
Scores are calculated differently based on the selected investor type:

Value Investor: Focuses on low PEG, Price-to-Book, and Price/Earnings ratios.
Growth Investor: Prioritizes high Return on Equity.
Income Investor: Emphasizes high Dividend Yield and sustainable Dividend Payout Ratios.
Data Formatting
The program expects the input dataset to have the following columns:

PEG: Price/Earnings to Growth Ratio
PE: Price/Earnings Ratio
PTB: Price-to-Book Ratio
ROE: Return on Equity (in percentage)
DIVY: Dividend Yield (in percentage)
DPR: Dividend Payout Ratio (in percentage)
Example Input Data Format
csv
Copy code
TICKER,PEG,PE,PTB,ROE,DIVY,DPR
AAPL,1.5,25,15,20%,0.5%,50%
MSFT,2,30,12,25%,1%,45%
Data Processing
Columns are renamed internally for consistency:
PEG → Price/Earnings to Growth
PE → Price/Earnings
PTB → Price to Book
ROE → Return on Equity
DIVY → Dividend Yield
DPR → Dividend Payout Ratio
Percentage values are converted to decimals for calculations (e.g., 20% → 0.2).
Scoring Interpretation
Score Range:
Score > 5: Great Candidate
Score 1 - 5: Average Candidate (requires further review)
Score < 1: Poor Candidate
Each score is calculated using weighted metrics based on the selected investor type.

File Structure
plaintext
Copy code
project/
│
├── stock_screener.py          # Main application script
├── actuallythefinaldataset.csv  # Dataset to be uploaded
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation (this file)
Troubleshooting
Common Issues:
Error: "ModuleNotFoundError" Ensure all required libraries are installed:

bash
Copy code
pip install -r requirements.txt
Dataset Not Found Verify the dataset path is correct and the file is in the expected format.

Visualization Not Displaying Ensure that matplotlib and seaborn are installed. Run:

bash
Copy code
pip install matplotlib seaborn
Application Not Starting Ensure Streamlit is installed and run:

bash
Copy code
streamlit run stock_screener.py
