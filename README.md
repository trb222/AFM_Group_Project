# AFM_Group_Project
Advanced Financial Modeling Group Project (Stock Screener)


Link to Run Program (EASIEST WAY TO RUN), copy into any browser
https://afmgroupproject-kttkottuk8ypcfmryapach.streamlit.app/

**Stock Screener Application**

    This Stock Screener Application is built using Streamlit and allows users to filter and score stocks based on various financial metrics and investor preferences. It provides a user-friendly interface for stock analysis and includes features like data visualization and CSV export for the filtered results.

**Features**
    
    Load and Clean Data
      Automatically cleans and formats the dataset to ensure proper analysis.
      Renames columns for better readability.
      Converts percentage values into decimals for consistency.
      Filter Stocks
    
    Allows filtering stocks based on the following financial metrics:
      Price/Earnings to Growth (PEG Ratio)
      Price to Book (P/B Ratio)
      Price/Earnings (P/E Ratio)
      Return on Equity (ROE)
      Dividend Yield (DY)
      Dividend Payout Ratio (DPR)
      Scoring System
      
    Calculates a score for each stock based on the selected Investor Type:
      Value Investor
      Growth Investor
      Income Investor
      Custom weights are applied to each metric to align with the selected investment strategy.
      
    Visualization
      Generates bar charts for key metrics such as PEG, P/B, P/E, ROE, DY, DPR, and the calculated scores.
      Provides insights into the selected stocks' performance.
      Download Filtered Results

    Export the filtered and scored stock data as a CSV file.

**How to Use**

      Step 1: Load Dataset
        Place the dataset (actuallythefinaldataset.csv) in the designated path.
        Ensure the dataset contains columns like PEG, PE, PTB, ROE, DIVY, and DPR. The app will automatically rename and format them for analysis.
      
      Step 2: Set Filter Criteria
        Use the Sidebar to define your filtering preferences:
        PEG Ratio: Set minimum and maximum thresholds.
        Price to Book: Set minimum and maximum thresholds.
        Price/Earnings: Set minimum and maximum thresholds.
        Return on Equity: Set the minimum value.
        Dividend Yield: Set the minimum value.
        Dividend Payout Ratio: Set the maximum value.
        
      Step 3: Select Investor Type
        Choose your investor type:
        Value Investor: Focuses on undervalued stocks.
        Growth Investor: Emphasizes high growth potential.
        Income Investor: Prioritizes dividend income.
        
      Step 4: View Filtered Results
        The app will display stocks that meet the filter criteria.
        A scoring table highlights the performance of stocks according to the selected investor type.
        
      Step 5: Visualize Metrics
        Generate bar charts to analyze the performance of filtered stocks.
        Select metrics to compare stock performance visually.
        
      Step 6: Export Data
        Download the filtered results as a CSV file for further analysis.
        Installation
        Clone or download this repository.

**Install the required Python packages using pip:**

      pip install streamlit pandas matplotlib seaborn

**Run the application:**

      streamlit run groupproject.py
      File Requirements
      Ensure your dataset matches the following structure:
    
      Column	Description
      PEG	Price/Earnings to Growth Ratio
      PE	Price/Earnings Ratio
      PTB	Price to Book Ratio
      ROE	Return on Equity (%)
      DIVY	Dividend Yield (%)
      DPR	Dividend Payout Ratio (%)
      The application will automatically rename and format these columns for consistency.
    
      **OR JUST CLICK THE LINK AT THE TOP**

**Key Functions**

      load_data()
        Cleans the dataset and ensures numeric columns are properly formatted for analysis.
      
      filter_stocks(data, ...)
        Applies filters to the dataset based on user-defined criteria.
      
      calculate_scores(data, investor_type)
        Calculates a score for each stock based on the selected investor type.
      
      show_visualizations(data)
        Generates bar charts for selected metrics to help visualize stock performance.
      
      display_score_interpretation()
        Provides guidance on interpreting the scoring system.


**Scoring System**

      Each investor type uses a different set of weights for the metrics:

    **Metric	Value Investor,	Growth Investor,	Income Investor**
      Price/Earnings to Growth	0.2	0.1	0.1
                Price to Book	 0.25	0.1	0.1
              Price/Earnings	 0.25	0.1	0.1
              Return on Equity	0.1	0.5	0.1
                Dividend Yield	0.1	0.1	0.4
          Dividend Payout Ratio	0.1	0.1	0.2
      The scoring system is calculated as a weighted sum of these metrics, with adjustments for preferred values.

**Visualization Options**

      Select metrics for visualization from the following:
      Price/Earnings to Growth (PEG)
      Price to Book (P/B)
      Price/Earnings (P/E)
      Return on Equity (ROE)
      Dividend Yield (DY)
      Dividend Payout Ratio (DPR)
      Score
      Bar charts are generated for a clear comparison of stock metrics.

**Troubleshooting**
    
      File Not Found Error: Ensure the dataset is placed in the correct path and named correctly.
      No Data After Filtering: Adjust filter criteria to include a broader range of values.
      Visualization Issues: Verify that there is data in the filtered results.
      
**Future Enhancements**

      Add support for live stock data via APIs.
      Include advanced visualizations like scatter plots or heatmaps.
      Provide user-friendly templates for uploading datasets.


**Acknowledgments**
    
      Streamlit for enabling the creation of interactive applications.
      Pandas, Matplotlib, and Seaborn for data manipulation and visualization tools.
