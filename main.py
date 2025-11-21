import pandas as pd
import plotly.express as px

# loads CSV
df = pd.read_csv("can_data.csv")

# dynamically remove all 'Analog Input' columns where ALL values are constant


dead_cols = [
    col for col in df.columns
    if "Analog Input" in col and df[col].nunique() == 1
]
df = df.drop(columns=dead_cols)

print("Removed dead analog columns:", dead_cols)


# plot RPM over time
fig_rpm = px.line(df, x=df.columns[0], y="RPM", title="RPM Over Time")
fig_rpm.show()

# plot TPS over time
fig_tps = px.line(df, x=df.columns[0], y="TPS", title="TPS Over Time")
fig_tps.show()

