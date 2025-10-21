"""
Kickstarter Data Loader Script
Loads existing CSV kickstarter data into SQLite database
"""

import pandas as pd
import sqlite3
import os
from pathlib import Path

def download_kaggle_data():
    """
    Download Kickstarter data from Kaggle
    Note: Requires Kaggle API credentials to be set up
    """
    print("To download data from Kaggle:")
    print("1. Install kaggle: pip install kaggle")
    print("2. Set up API credentials from https://www.kaggle.com/account")
    print("3. Run: kaggle datasets download -d kemical/kickstarter-projects")
    print("4. Extract the CSV file to the data/ directory")
    print("\nAlternatively, manually download from:")
    print("https://www.kaggle.com/datasets/kemical/kickstarter-projects/data")

def load_csv_to_sqlite(csv_path, db_path):
    """
    Load CSV data into SQLite database
    """
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Read CSV file
    print(f"Loading data from {csv_path}...")
    # Try different encodings to handle potential Unicode issues
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
    except UnicodeDecodeError:
        print("UTF-8 encoding failed, trying latin-1...")
        df = pd.read_csv(csv_path, encoding='latin-1')
    
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load data into SQLite
    df.to_sql('kickstarter_projects', conn, if_exists='replace', index=False)
    
    print(f"Data loaded successfully into {db_path}")
    print(f"Table: kickstarter_projects")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    
    # Display column information
    print("\nColumn headers:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i:2d}. {col}")
    
    # Display basic info
    print(f"\nData types:")
    print(df.dtypes)
    
    conn.close()
    return df

def explore_data_structure(db_path):
    """
    Explore the structure of the loaded data
    """
    conn = sqlite3.connect(db_path)
    
    # Get table info
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(kickstarter_projects)")
    columns = cursor.fetchall()
    
    print("Database Schema:")
    print("Column | Type | Not Null | Default | Primary Key")
    print("-" * 50)
    for col in columns:
        print(f"{col[1]:<15} | {col[2]:<8} | {col[3]:<8} | {col[4]:<7} | {col[5]}")
    
    # Get row count
    cursor.execute("SELECT COUNT(*) FROM kickstarter_projects")
    count = cursor.fetchone()[0]
    print(f"\nTotal rows: {count}")
    
    # Get sample data
    cursor.execute("SELECT * FROM kickstarter_projects LIMIT 5")
    sample = cursor.fetchall()
    
    print("\nSample data (first 5 rows):")
    column_names = [description[0] for description in cursor.description]
    for i, row in enumerate(sample):
        print(f"\nRow {i+1}:")
        for col_name, value in zip(column_names, row):
            print(f"  {col_name}: {value}")
    
    conn.close()

if __name__ == "__main__":
    # File paths
    data_dir = Path("data")
    csv_file = data_dir / "ks-projects-201612.csv"  # Expected filename from Kaggle
    db_file = data_dir / "kickstarter.db"
    
    # Check if CSV exists
    if not csv_file.exists():
        print(f"CSV file not found at {csv_file}")
        download_kaggle_data()
        print(f"\nAfter downloading, place the CSV file at: {csv_file}")
    else:
        # Load data
        df = load_csv_to_sqlite(csv_file, db_file)
        
        # Explore structure
        explore_data_structure(db_file)