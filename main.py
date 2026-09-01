import pandas as pd
import matplotlib as plt
import datacleaning
import dataanalysis
import datavisualization


file_path = "/Users/darrento/Desktop/formularacing/can_data.csv"
df = pd.read_csv(file_path)

clean_df = datacleaning.clean_data(df)

rpm_tps_correlation = dataanalysis.calculate_correlation(
    clean_df,
    "RPM",
    "TPS"
)
print(df.info)
print(f"\nCorrelation between RPM and TPS: {rpm_tps_correlation:.2f}")
datavisualization.create_rpm_tps_scatter(clean_df)