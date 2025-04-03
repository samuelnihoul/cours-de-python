import pandas as pd
import os

def read_file(file_path):
    """
    Read a file and return its content as a DataFrame based on the file extension.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        pd.DataFrame: DataFrame containing the file content
    """
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() == '.csv':
        return pd.read_csv(file_path)
    elif file_extension.lower() == '.xlsx':
        return pd.read_excel(file_path)
    elif file_extension.lower() == '.json':
        return pd.read_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

def filter_boolean_yes(df, column_name='boolean'):
    """
    Filter rows where the specified boolean column equals 'Yes'.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column_name (str): Name of the boolean column
        
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    return df[df[column_name] == 'yes']

def filter_url_contains_reddit(df, column_name='url'):
    """
    Filter rows where the URL column contains 'reddit'.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column_name (str): Name of the URL column
        
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    return df[df[column_name].str.contains('reddit', case=False, na=False)]

def calculate_percentage(df, condition1_df, condition2_df):
    """
    Calculate the percentage of rows that meet both conditions.
    
    Args:
        df (pd.DataFrame): Original DataFrame
        condition1_df (pd.DataFrame): DataFrame with first condition
        condition2_df (pd.DataFrame): DataFrame with second condition
        
    Returns:
        tuple: (percentage_condition1, percentage_condition2)
    """
    total_rows = len(df)
    percentage_condition1 = (len(condition1_df) / total_rows) * 100
    percentage_condition2 = (len(condition2_df) / total_rows) * 100
    
    return percentage_condition1, percentage_condition2

def save_filtered_dataframes(original_df, condition1_df, condition2_df, output_dir='.'):
    """
    Save filtered DataFrames to CSV files.
    
    Args:
        original_df (pd.DataFrame): Original DataFrame
        condition1_df (pd.DataFrame): DataFrame with first condition
        condition2_df (pd.DataFrame): DataFrame with second condition
        output_dir (str): Directory to save the files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Save filtered DataFrames
    condition1_df.to_csv(os.path.join(output_dir, 'boolean_yes.csv'), index=False)
    condition2_df.to_csv(os.path.join(output_dir, 'url_reddit.csv'), index=False) 