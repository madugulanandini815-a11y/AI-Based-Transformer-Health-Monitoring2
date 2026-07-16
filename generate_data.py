import pandas as pd
import numpy as np

np.random.seed(42)

rows = 3000

districts = ["coimbatore","madurai","salem","trichy","tenkasi$env:Path += ";

data = pd.DataFrame({
    "Transformer_ID": np.arange(1, rows+1),
    "District": np.random.choice(districts, rows),
    "Load_kW": np.random.normal(100, 30, rows),
    "Temp_C": np.random.normal(60, 15, rows),
    "Voltage": np.random.normal(230, 10, rows),
    "Oil_Level": np.random.normal(70, 20, rows),
    "Age_Years": np.random.randint(1, 25, rows)
})

# Create base failure score
failure_score = (
    0.4*(data["Load_kW"]/150) +
    0.3*(data["Temp_C"]/100) +
    0.2*((100-data["Oil_Level"])/100) +
    0.1*(data["Age_Years"]/25)
)

# Add random noise
noise = np.random.normal(0, 0.05, rows)

final_score = failure_score + noise

# Convert to binary failure using probability threshold
data["Failure"] = (final_score > 0.65).astype(int)

data.to_csv("transformer_data.csv", index=False)

print("Realistic Dataset Created!")