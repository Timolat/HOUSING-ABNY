# HOUSING-ABNY

Overview / Introduction
This project aims to analyze Airbnb listings in New York City to understand pricing patterns, host behavior, and rental trends. The analysis is motivated by the need to identify key factors influencing rental prices and occupancy rates, which can help hosts optimize their listings and assist travelers in making informed decisions.
Problem Statement:
•	What are the key factors influencing Airbnb prices in NYC?
•	How do different boroughs compare in terms of rental availability and pricing?
•	Are there significant data integrity issues, such as missing values or outliers, affecting the analysis?
________________________________________
# Data Collection & Description
•	Data Source: The dataset was obtained from Kaggle, containing Airbnb listings for NYC in 2019.
•	Dataset Structure: 
o	Rows: Approx. 49,000 listings
o	Columns: 16 features including listing details, host information, price, and location
# Key Variables:
•	name: Name of the listing
•	host_name: Name of the host
•	neighbourhood_group: Borough in NYC (Manhattan, Brooklyn, etc.)
•	neighbourhood: Specific neighborhood
•	latitude & longitude: Location coordinates
•	room_type: Type of listing 
•	price: Price per night
•	minimum_nights: Minimum nights required
•	number_of_reviews: Total number of reviews
•	last_review: Date of the last review
•	reviews_per_month: Review frequency
# Data Preprocessing Steps:
1.	Handling Missing Data: 
o	name and host_name missing values filled with "Unknown"
o	reviews_per_month missing values filled with 0
o	last_review missing values replaced with "2000-01-01"
2.	Duplicate Removal: No duplicates found.
3.	Data Standardization: Formatting dates and ensuring numerical consistency.
________________________________________
# Exploratory Data Analysis (EDA)
Summary Statistics:
•	Price Analysis: 
o	Mean: $152.72, Median: $106
o	Standard Deviation: High variation in prices
•	Minimum Nights Analysis: 
o	Some extreme values (e.g., listings with 365+ minimum nights)
•	Review Trends: 
o	Many properties have low review counts; few have significantly high reviews
Data Visualization:
•	Histograms: Distribution of price, minimum nights, and reviews per month.
•	Box Plots: Identifying outliers in pricing and minimum night stays.
•	Scatter Plots: Relationship between price and number of reviews.
•	Correlation Matrix: Understanding relationships between numerical variables.
________________________________________
# Data Cleaning & Preprocessing
1.	Outlier Handling: 
o	Price outliers capped at 75th percentile + 1.5 IQR.
o	Minimum nights capped similarly to avoid unrealistic values.
2.	Feature Engineering: 
o	Creating a price_category column (Low, Medium, High pricing tiers).
o	Extracting year and month from last_review for trend analysis.
3.	Encoding: 
o	Converting categorical variables (room_type, neighbourhood_group) into numerical values.
________________________________________
# Methodology / Approach
•	Analytical Techniques Used: 
o	Descriptive statistics for understanding dataset properties.
o	Data visualization for patterns and trends.
o	Machine learning models (if applicable) for price prediction.
•	Model Choices: 
o	Regression models (Linear Regression, Random Forest) for price prediction.
o	Clustering (K-Means) to identify neighborhood-based pricing patterns.
________________________________________
# Data Analysis / Modeling
•	Implemented Using: Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
•	Model Performance Metrics: 
o	RMSE for regression models to measure price prediction accuracy.
o	R² score to determine variance explained by the model.
________________________________________
# Results & Interpretation
•	Key Findings: 
o	Manhattan has the highest median rental prices.
o	Entire homes/apartments cost significantly more than private rooms.
o	Listings with higher review counts tend to have lower prices.
•	Implications: 
o	Hosts in high-demand areas can optimize pricing strategies.
o	Budget travelers can identify boroughs with cheaper listings.
________________________________________
# Challenges & Limitations
•	Data Quality Issues: Missing values in reviews_per_month, last_review.
•	Outliers: Extremely high values in minimum_nights and price affected initial analysis.
•	Assumptions: 
o	Imputation of missing values may introduce slight biases.
o	Capping outliers assumes extreme values are errors.
________________________________________
# Conclusion & Recommendations
	Major Findings: 
o	Room type and location significantly impact price variations.
o	High-priced listings often have fewer reviews.
•	Recommendations: 
o	Hosts should consider dynamic pricing strategies.
o	Further analysis with time-series data could improve forecasting.
