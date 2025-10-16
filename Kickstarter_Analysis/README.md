# Kickstarter Data Analysis Project

This project analyzes Kickstarter campaign data to understand project success patterns and identify which categories have the highest likelihood of success.

## 🎯 Project Goals

1. **Data Structure Analysis**: Examine database schema and column headers
2. **Success Rate Analysis**: Determine which project categories have the highest success rates
3. **Pattern Discovery**: Identify factors that correlate with project success

## 📊 Dataset

**Source**: [Kickstarter Projects Dataset from Kaggle](https://www.kaggle.com/datasets/kemical/kickstarter-projects/data)

The dataset contains information about Kickstarter projects including:
- Project details (name, category, goal, pledged amount)
- Campaign timeline (launch date, deadline, duration)
- Outcomes (successful, failed, canceled, etc.)
- Geographic information (country)
- Engagement metrics (backers count)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- VS Code with Python and Jupyter extensions

### Setup
1. **Clone and navigate to the project**:
   ```bash
   git clone <repository-url>
   cd Kickstarter_Analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**:
   - Visit [Kaggle dataset page](https://www.kaggle.com/datasets/kemical/kickstarter-projects/data)
   - Download `ks-projects-201801.csv`
   - Place it in the `data/` directory

4. **Load data into database**:
   ```bash
   python scripts/load_data.py
   ```

5. **Start analysis**:
   - Open `notebooks/kickstarter_analysis.ipynb` in VS Code
   - Run all cells to perform the analysis

## 📁 Project Structure

```
Kickstarter_Analysis/
├── .github/
│   └── copilot-instructions.md    # Project context for Copilot
├── data/
│   ├── kickstarter.db            # SQLite database (created after loading)
│   └── ks-projects-201801.csv    # Raw data (download from Kaggle)
├── notebooks/
│   └── kickstarter_analysis.ipynb # Main analysis notebook
├── scripts/
│   └── load_data.py              # Data loading script
├── sql/
│   └── analysis_queries.sql      # SQL queries for analysis
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔍 Key Analysis Questions

### 1. Database Structure
- What are the column headers and data types?
- How many projects and categories are in the dataset?
- What is the overall data quality?

### 2. Success Rate Analysis
- Which project categories have the highest success rates?
- How do success rates vary by funding goal ranges?
- What is the overall success/failure distribution?

### 3. Pattern Discovery
- Is there a correlation between project volume and success rate?
- How do funding goals relate to success likelihood?
- What factors differentiate successful from failed projects?

## 📈 Key Findings

The analysis reveals several important patterns:

- **Category Performance**: Success rates vary significantly across project categories
- **Volume vs Success**: High-volume categories don't always have the highest success rates
- **Funding Goals**: There's a clear relationship between goal size and success probability

*(Detailed findings available in the Jupyter notebook)*

## 🛠️ Tools and Technologies

- **Python**: Data analysis and visualization
- **pandas**: Data manipulation and analysis
- **SQLite**: Local database for data storage
- **matplotlib/seaborn**: Static visualizations
- **plotly**: Interactive visualizations
- **Jupyter**: Interactive analysis environment
- **VS Code**: Development environment with SQL and Python extensions

## 🔄 Development Workflow

1. **Data Loading**: Use `scripts/load_data.py` to import CSV data into SQLite
2. **SQL Analysis**: Run queries from `sql/analysis_queries.sql` for database-level analysis
3. **Python Analysis**: Use Jupyter notebook for advanced analysis and visualization
4. **Iteration**: Modify queries and analysis based on findings

## 📝 SQL Queries

The project includes pre-written SQL queries for:
- Database schema inspection
- Basic statistics calculation
- Success rate analysis by category
- Funding goal range analysis
- Sample data extraction

Run these queries using VS Code's SQLTools extension or any SQLite client.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your analysis or improvements
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Dataset provided by [Mickaël Mouillé on Kaggle](https://www.kaggle.com/kemical)
- Kickstarter for making project data available for research

---

**Happy analyzing! 🚀📊**