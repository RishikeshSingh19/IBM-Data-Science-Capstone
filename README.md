# SpaceX Falcon 9 First Stage Landing Prediction

## Project Overview

This project was completed as part of the IBM Data Science Capstone. The objective is to predict whether the first stage of a SpaceX Falcon 9 rocket will successfully land using historical launch data. Successful landings significantly reduce launch costs and are a key factor in the commercial success of reusable rockets.

The project follows a complete end-to-end data science workflow, including data collection, data wrangling, exploratory data analysis, interactive visualization, dashboard development, and machine learning.

---

## Project Workflow

1. Data Collection using SpaceX API
2. Data Collection using Web Scraping
3. Data Wrangling and Data Cleaning
4. Exploratory Data Analysis (EDA) with Visualization
5. Exploratory Data Analysis (EDA) with SQL
6. Interactive Visual Analytics using Folium
7. Dashboard Development using Plotly Dash
8. Machine Learning Prediction

---

## Repository Structure

```text
.
├── dashboard/
│   └── spacex_dash_app.py
│
├── notebooks/
│   ├── spacex-data-collection-api.ipynb
│   ├── spacex-data-collection-webscraping.ipynb
│   ├── spacex-Data-wrangling.ipynb
│   ├── spacex-eda-visualization.ipynb
│   ├── spacex-eda-sql-lite.ipynb
│   ├── spacex-folium.ipynb
│   └── spacex_Machine-Learning-Prediction.ipynb
│
├── presentation/
│   └── IBM-Data-Science-Capstone.pdf
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQL
* Folium
* Plotly Dash
* Scikit-learn
* Jupyter Notebook

---

## Project Components

### Data Collection

* Retrieved launch data using the SpaceX API.
* Collected additional launch information through web scraping.

### Data Wrangling

* Cleaned and transformed raw data.
* Handled missing values and prepared datasets for analysis.

### Exploratory Data Analysis

* Investigated launch success rates across launch sites.
* Examined the relationship between payload mass, orbit type, and landing success.
* Performed both visualization-based and SQL-based analysis.

### Interactive Visual Analytics

* Developed interactive maps using Folium.
* Visualized launch site locations and mission outcomes geographically.

### Dashboard Development

* Built an interactive Plotly Dash dashboard.
* Enabled dynamic exploration of launch outcomes and payload trends.

### Machine Learning Prediction

* Trained and evaluated classification models to predict first-stage landing success.
* Compared multiple machine learning algorithms and assessed their performance.

---

## Results

The analysis identified several factors associated with successful Falcon 9 first-stage landings, including launch site characteristics, orbit selection, and payload mass.

Machine learning models were trained using historical launch data to predict landing outcomes and demonstrate the application of predictive analytics in aerospace operations.

---

## Final Project Report

The complete project report and presentation can be found in:

`presentation/IBM-Data-Science-Capstone.pdf`

---

## Skills Demonstrated

* Data Collection
* Web Scraping
* Data Wrangling
* Exploratory Data Analysis
* SQL Analysis
* Geospatial Visualization
* Dashboard Development
* Machine Learning
* Data Storytelling
* Technical Documentation

---

## Author

**Rishikesh Singh**

Based on the IBM Data Science Capstone Project. Notebook completed and extended by Rishikesh Singh.
