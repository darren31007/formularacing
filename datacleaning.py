import pandas as pd

def clean_data(data):
    #remove rows containing missing data
    cleaned_data = data.dropna().copy()

    #convert timestamps to a more readable way
    cleaned_data["timestamp"] = pd.to_datetime(cleaned_data["timestamp"], unit = 's')

    return cleaned_data