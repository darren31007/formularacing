def calculate_correlation(data, first_column, second_column):
    correlation = data[first_column].corr(data[second_column])

    return correlation