def calculate_correlation(data, first_column, second_column):
    correlation = data[first_column].corr(data[second_column])

    return correlation


# calculate the time difference between each reading and the first reading.
def add_elapsed_time(data):
    analyzed_data = data.copy()
    first_timestamp = analyzed_data["timestamp"].iloc[0]
    time_differences = analyzed_data["timestamp"] - first_timestamp
    elapsed_seconds = time_differences.dt.total_seconds()
    analyzed_data["Elapsed Time (seconds)"] = elapsed_seconds
    return analyzed_data