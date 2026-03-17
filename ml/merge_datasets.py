import pandas as pd

# ---------- KAGGLE ----------
k_fake = pd.read_csv("data/kaggle/Fake.csv")
k_true = pd.read_csv("data/kaggle/True.csv")

k_fake["label"] = "FAKE"
k_true["label"] = "REAL"

kaggle_df = pd.concat([k_fake, k_true])
kaggle_df = kaggle_df[["text", "label"]]

# ---------- ISOT ----------
i_fake = pd.read_csv("data/isot/Fake.csv")
i_true = pd.read_csv("data/isot/True.csv")

i_fake["label"] = "FAKE"
i_true["label"] = "REAL"

isot_df = pd.concat([i_fake, i_true])
isot_df = isot_df[["text", "label"]]

# ---------- LIAR ----------
columns = ["id","label","statement","subject","speaker",
           "speaker_job","state","party","barely_true",
           "false","half_true","mostly_true","pants_on_fire","context"]

liar = pd.read_csv("data/liar/train.tsv", sep="\t", names=columns)

# Convert LIAR labels to binary
def convert_label(x):
    if x in ["false", "pants-fire"]:
        return "FAKE"
    else:
        return "REAL"

liar["label"] = liar["label"].apply(convert_label)
liar_df = liar[["statement", "label"]]
liar_df.columns = ["text", "label"]

# ---------- COMBINE ----------
final_df = pd.concat([kaggle_df, isot_df, liar_df])

# Remove nulls
final_df = final_df.dropna()

# Shuffle
final_df = final_df.sample(frac=1)

# Save
final_df.to_csv("data/final_dataset.csv", index=False)

print("✅ Dataset merged successfully!")