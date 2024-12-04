import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
def load_data():
    # Load the uploaded dataset
    data = pd.read_csv(r"actuallythefinaldataset.csv")  
    # Rename columns to align with references in the code
    data.rename(columns={
        'PEG': 'Price/Earnings to Growth',  # Corrected for PEG
        'PE': 'Price/Earnings',            # Corrected for PE
        'PTB': 'Price to Book',
        'ROE': 'Return on Equity',
        'DIVY': 'Dividend Yield',
        'DPR': 'Dividend Payout Ratio'
    }, inplace=True)
    
    # Convert percentages and handle numeric data types
    data['Dividend Yield'] = data['Dividend Yield'].str.rstrip('%').astype(float) / 100
    data['Dividend Payout Ratio'] = pd.to_numeric(data['Dividend Payout Ratio'], errors='coerce')
    data['Price/Earnings to Growth'] = pd.to_numeric(data['Price/Earnings to Growth'], errors='coerce')
    data['Price to Book'] = pd.to_numeric(data['Price to Book'], errors='coerce')
    data['Return on Equity'] = pd.to_numeric(data['Return on Equity'], errors='coerce')
    data['Price/Earnings'] = pd.to_numeric(data['Price/Earnings'], errors='coerce')  # Ensure PE is numeric
    
    return data

# Filter stocks based on user inputs
def filter_stocks(data, peg_min, peg_max, pb_min, pb_max, pe_min, pe_max, roe_min, dy_min, dp_max):
    # Apply filters to the data
    filtered_data = data[
        (data['Price/Earnings to Growth'] >= peg_min) & 
        (data['Price/Earnings to Growth'] <= peg_max) &
        (data['Price to Book'] >= pb_min) &
        (data['Price to Book'] <= pb_max) &
        (data['Price/Earnings'] >= pe_min) &
        (data['Price/Earnings'] <= pe_max) &
        (data['Return on Equity'] >= roe_min) &
        (data['Dividend Yield'] >= dy_min) &
        (data['Dividend Payout Ratio'] <= dp_max)
    ]
    
    return filtered_data

# Calculate scores based on investor type
def calculate_scores(data, investor_type):
    # Define weights based on investor type
    if investor_type == "Value Investor":
        weights = {
            'Price/Earnings to Growth': 0.2,  # Lower PEG preferred
            'Price to Book': 0.25,           # Lower PB preferred
            'Price/Earnings': 0.25,          # Lower PE preferred
            'Return on Equity': 0.1,         # Neutral for ROE
            'Dividend Yield': 0.1,           # Minimal impact
            'Dividend Payout Ratio': 0.1     # Lower DPR preferred
        }
    elif investor_type == "Growth Investor":
        weights = {
            'Price/Earnings to Growth': 0.1,  # Somewhat low PEG preferred
            'Price to Book': 0.1,            # Minimal PB focus
            'Price/Earnings': 0.1,           # Lower PE less critical
            'Return on Equity': 0.5,         # High ROE preferred
            'Dividend Yield': 0.1,           # Minimal importance
            'Dividend Payout Ratio': 0.1     # Moderate impact for stability
        }
    elif investor_type == "Income Investor":
        weights = {
            'Price/Earnings to Growth': 0.1,  # Minimal importance
            'Price to Book': 0.1,            # Minimal impact
            'Price/Earnings': 0.1,           # Neutral
            'Return on Equity': 0.1,         # Moderate impact for sustainability
            'Dividend Yield': 0.4,           # High weight for income
            'Dividend Payout Ratio': 0.2     # Ensure sustainable dividends
        }
    else:
        raise ValueError("Invalid investor type")

    # Calculate the score based on weights
    data['Score'] = (
        (weights['Price/Earnings to Growth'] / data['Price/Earnings to Growth'].replace(0, 1)) +  # Lower PEG preferred
        (weights['Price to Book'] / data['Price to Book'].replace(0, 1)) +  # Lower PB preferred
        (weights['Price/Earnings'] / data['Price/Earnings'].replace(0, 1)) +  # Lower PE preferred
        (weights['Return on Equity'] * data['Return on Equity']) +  # Higher ROE preferred
        (weights['Dividend Yield'] * data['Dividend Yield']) +  # Higher Dividend Yield preferred
        (weights['Dividend Payout Ratio'] / data['Dividend Payout Ratio'].replace(0, 1))  # Lower DPR preferred
    )

    # Sort by score
    return data.sort_values(by='Score', ascending=False)

# Scoring Interpretation in Streamlit
def display_score_interpretation():
    st.write("### Score Interpretation Scale")
    st.markdown("""
    - **Score > 5:** Strong Candidate
    - **Score 1 - 5:** Average Candidate (requires closer review)
    - **Score < 1:** Below Average Candidate (likely not ideal)
    """)

# Create bar chart visualizations
def show_visualizations(data):
    st.header("Visualization")
    selected_metric = st.selectbox(
        "Select Metric for Bar Chart",
        ["Price/Earnings to Growth", "Price to Book", "Price/Earnings", "Return on Equity", "Dividend Yield", "Dividend Payout Ratio", "Score"]
    )
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x="TICKER", y=selected_metric)
    plt.xticks(rotation=90)
    plt.title(f"Bar Chart of {selected_metric}")
    st.pyplot(plt)

# Main app function
def main():
    st.title("Stock Screener Application")
    st.sidebar.header("Filter Criteria")
    
    # User input for filters
    peg_min = st.sidebar.number_input("PEG Ratio Min", value=0.0, step=0.1)
    peg_max = st.sidebar.number_input("PEG Ratio Max (Leave blank for no max)", value=None, step=0.1) or 1_000_000.0
    pb_min = st.sidebar.number_input("Price-to-Book Min", value=0.0, step=0.1)
    pb_max = st.sidebar.number_input("Price-to-Book Max (Leave blank for no max)", value=None, step=0.1) or 1_000_000.0
    pe_min = st.sidebar.number_input("Price/Earnings Min", value=0.0, step=0.1)
    pe_max = st.sidebar.number_input("Price/Earnings Max (Leave blank for no max)", value=None, step=0.1) or 1_000_000.0
    roe_min = st.sidebar.number_input("Return on Equity Min (%)", value=0.0, step=1.0)
    dy_min = st.sidebar.number_input("Dividend Yield Min (%)", value=0.0, step=0.1)
    dp_max = st.sidebar.number_input("Dividend Payout Ratio Max (Leave blank for no max)", value=None, step=1.0) or 1_000_000.0
    
    # Investor type selection
    investor_type = st.sidebar.selectbox(
        "Select Investor Type",
        ["Value Investor", "Growth Investor", "Income Investor"]
    )
    
    # Load dataset
    data = load_data()
    
    # Filter data based on user criteria
    filtered_data = filter_stocks(data, peg_min, peg_max, pb_min, pb_max, pe_min, pe_max, roe_min, dy_min / 100, dp_max / 100)
    
    if not filtered_data.empty:
        # Calculate scores based on investor type
        filtered_data = calculate_scores(filtered_data, investor_type)
        
        # Display filtered results
        st.header("Filtered Results")
        st.write(f"Found {len(filtered_data)} stocks meeting your criteria.")
        st.dataframe(filtered_data[['TICKER', 'Price/Earnings to Growth', 'Price to Book', 'Price/Earnings',
                                    'Return on Equity', 'Dividend Yield', 'Dividend Payout Ratio']])
        
        # Display scoring results
        st.header("Scoring Results")
        st.write("The following table displays the scores for the filtered stocks:")
        st.table(filtered_data[['TICKER', 'Score']].style.format({'Score': '{:.2f}'}))
        
        # Display revised scoring interpretation
        display_score_interpretation()

        # Visualization module
        show_visualizations(filtered_data)
        
        # Download filtered results as CSV
        csv = filtered_data.to_csv(index=False)
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name='filtered_stocks.csv',
            mime='text/csv',
        )
    else:
        st.header("Filtered Results")
        st.write("No stocks meet the selected criteria. Please adjust your filters and try again.")

# Run the app
if __name__ == "__main__":
    main()
