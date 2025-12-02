import pandas as pd


df = pd.read_excel("data.xlsx")


df = df.rename(columns={
    "column1": "fruit",
    "column2": "colour",
    "column3": "rate"
})


print("Updated column names:")
print(df.columns.tolist())


df.to_excel("data_renamed.xlsx", index=False)

print("Columns renamed successfully and saved to data_renamed.xlsx")
