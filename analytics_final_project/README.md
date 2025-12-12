# Global Youth Unemployment Analysis and Prediction

## 📊 Project Overview

This project analyzes global youth unemployment trends and develops predictive models to forecast future unemployment rates. Using historical data from World Bank indicators, we explore patterns across countries and regions, identify key factors influencing youth unemployment, and build machine learning models to predict future trends.

### 🎯 Objectives
- Analyze global youth unemployment patterns from 1970-2024
- Develop predictive models for youth unemployment forecasting
- Identify regional and temporal trends
- Provide actionable insights for policymakers and stakeholders
- Create an interactive web application for data exploration

### 📈 Dataset
- **Source**: World Bank World Development Indicators
- **Coverage**: 1970-2024 across 200+ countries and regions
- **Target Variable**: Youth Unemployment Rate (%)
- **Features**: Country, Year, Regional groupings

## 🛠️ Tools & Technologies
- **Language**: Python 3.9+
- **Analysis Environment**: Google Colab
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn, plotly
- **Web Framework**: Streamlit
- **Version Control**: Git/GitHub

## 📁 Repository Structure
```
├── notebooks/
│   ├── 01_eda.ipynb              # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb    # Data Cleaning & Feature Engineering
│   ├── 03_modeling.ipynb         # Model Development & Evaluation
│   └── 04_interpretation.ipynb   # Results & Business Insights
├── src/
│   ├── data_processing.py        # Data utilities
│   ├── modeling.py              # ML model functions
│   └── visualization.py         # Plotting functions
├── app/
│   └── app.py                   # Streamlit web application
├── data/
│   └── youth_unemployment_global.csv
├── visualizations/
│   └── *.png                    # Generated plots and charts
├── reports/
│   ├── Final Report 2.pdf       # Official final report (PDF format)
│   └── final_report.md          # Detailed analysis report (Markdown format)
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/youth-unemployment-analysis.git
cd youth-unemployment-analysis

# Install dependencies
pip install -r requirements.txt
```

### Running the Web Application
```bash
# Option 1: Direct Streamlit run
streamlit run app/app.py

# Option 2: Use the launcher script
python run_app.py
```

### Running the Analysis Notebooks
1. Open Google Colab
2. Upload the notebook files from `notebooks/` directory
3. Upload the dataset from `data/` directory
4. Run cells in order (01_eda.ipynb → 02_preprocessing.ipynb → 03_modeling.ipynb → 04_interpretation.ipynb)

## 📊 Google Colab Notebooks

All analysis notebooks are available on Google Colab:

1. **[Data Exploration and Cleaning](https://colab.research.google.com/drive/1FDedMcMRzmyz3cmcUJM1ZtzT_wnNK6FH?usp=sharing)** - Initial data exploration, cleaning, and preprocessing
2. **[Global Trends Analysis](https://colab.research.google.com/drive/19IXwBJNIVe9KvifvbISWh-2dLN_czIA6?usp=sharing)** - Temporal and regional trend analysis
3. **[Interactive Dashboard](https://colab.research.google.com/drive/1AZCj_lCgAyw-I6YkYn-WFR1QzvvRauU4?usp=sharing)** - Interactive visualizations and data exploration tools
4. **[Statistical Modeling & Forecasting](https://colab.research.google.com/drive/17YwizrwDq2Tlp-Sl5J5NJVlnGo8QYRw2?usp=sharing)** - Machine learning models and predictive analytics

## 🔍 Key Findings

### Global Trends
- Youth unemployment has shown varying patterns across regions
- Economic crises significantly impact youth employment
- Regional disparities highlight development gaps

### Model Performance
- Best Model: [Model Name] (R² = [score])
- Key Predictors: [Top features]
- Regional Accuracy: [Performance by region]

### Business Recommendations
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

## 📈 Interactive Dashboard

Explore the data interactively through our Streamlit web application:
- Global and regional trend analysis
- Country-specific forecasts
- Model performance visualization
- Scenario planning tools

## 🤝 Contributing

This is an academic project for portfolio purposes. Feel free to explore and learn from the code!

## 📄 Final Report

The comprehensive analysis report is available in PDF format at `reports/Final Report 2.pdf`. This document includes:

- Executive summary with key findings
- Detailed data analysis and methodology
- Business insights and strategic recommendations
- Ethics and responsible AI considerations
- Implementation roadmap

**For course submission:** Submit the PDF report (`Final Report 2.pdf`) along with the GitHub repository link as required by the assignment.

## 📄 License

This project is for educational purposes.

## 📞 Contact

For questions about this analysis, please reach out through GitHub issues.

---

*This project was completed as part of the analytics final project requirement.*
