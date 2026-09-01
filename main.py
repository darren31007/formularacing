import pandas as pd
import matplotlib as plt
import datacleaning
import dataanalysis
import datavisualization


file_path = "/Users/darrento/Desktop/formularacing/can_data.csv"
df = pd.read_csv(file_path)

clean_df = datacleaning.clean_data(df)

analyzed_df = dataanalysis.add_elapsed_time(clean_df)
recording_duration = analyzed_df["Elapsed Time (seconds)"].iloc[-1]

print(f"\nRecording duration: {recording_duration:.2f} seconds")

rpm_tps_correlation = dataanalysis.calculate_correlation(
    analyzed_df,
    "RPM",
    "TPS"
)
print(f"\nCorrelation between RPM and TPS: {rpm_tps_correlation:.2f}")
datavisualization.create_rpm_tps_scatter(analyzed_df)
datavisualization.create_rpm_timeline(analyzed_df)