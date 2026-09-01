# Formula Racing Data Analysis

## Project Overview

This project uses Python to clean, analyze, and visualize Formula racing data. This program analyzes the relationship between throttle position (TPS) and engine speed (RPM), along with how RPM changes during the recorded session.

The original dataset contains 14,372 sensor readings and 33 columns. After cleaning, 14,338 complete readings remained. The recording spans 157.56 seconds.

## How the Code Works

### Loading the Data

`main.py` uses `pd.read_csv()` to load `can_data.csv` into a pandas DataFrame. The DataFrame makes it possible to clean, select, calculate, and visualize the sensor data by column.

### Cleaning the Data

The `clean_data()` function in `datacleaning.py` uses `dropna()` to remove rows containing missing values. It also uses `copy()` so the original DataFrame is not modified unexpectedly.

The numeric Unix timestamps are converted into pandas date-time values using `pd.to_datetime()`. This conversion allows the timestamps to be used in time-based calculations.

- Rows before cleaning: 14,372
- Rows after cleaning: 14,338
- Incomplete rows removed: 34
- Missing values remaining: 0

### Deriving Elapsed Time

The `add_elapsed_time()` function in `dataanalysis.py` subtracts the first timestamp from every timestamp. The resulting time differences are converted to seconds using `total_seconds()` and stored in a new column named `Elapsed Time (seconds)`.

This derived value shows when each sensor reading occurred relative to the beginning of the recording. The final value revealed that the session lasted 157.56 seconds.

### Calculating Correlation

The `calculate_correlation()` function uses pandas' `corr()` method to calculate the Pearson correlation between RPM and TPS. The result was 0.75, indicating a strong positive relationship: higher throttle positions were generally associated with higher engine speeds.

This correlation is not automatically good or bad. It describes the direction and strength of the relationship. The value is below 1.00 because RPM is also affected by other factors when driving.

## Visualizations

### Throttle Position Compared with Engine RPM

This scatter plot places throttle position on the horizontal axis and RPM on the vertical axis. The overall upward pattern supports the positive correlation of 0.75. The spread of the points shows that the same throttle position can occur at multiple RPM values.

[Scatter plot comparing throttle position and engine RPM](graphs/rpm_vs_tps_scatter.png)

### Engine RPM Over Time

This line graph uses the derived elapsed-time values to show how RPM changed throughout the session. It reveals three major high-RPM intervals, including peaks above 12,000 RPM, separated by lower-RPM periods near 2,000 RPM.

[Line graph showing engine RPM over elapsed time](graphs/rpm_over_time_line.png)

## Conclusions

- Removing 34 incomplete rows produced a dataset with no remaining missing values.
- Converting the timestamps made it possible to calculate a total recording duration of 157.56 seconds.
- RPM and TPS had a strong positive correlation of 0.75.
- Higher throttle positions were generally connected with higher RPM, although other vehicle and driving conditions also affected engine speed.
- The RPM timeline showed three distinct periods of high engine activity during the recording.
- The scatter plot and line graph provide different views of the data: one shows a relationship between two variables, while the other shows change over time.