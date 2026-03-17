import pandas as pd

fake = pd.read_csv("data/Fake.csv")
real = pd.read_csv("data/True.csv")

fake["label"] = "FAKE"
real["label"] = "REAL"

data = pd.concat([fake, real])

data = data[["text", "label"]]

data.to_csv("data/news.csv", index=False)

print("✅ Dataset created successfully")