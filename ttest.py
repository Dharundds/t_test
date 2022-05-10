from math import sqrt
import pandas as pd


# population dataset

df = pd.read_csv("avax.csv")


# --------------------------------------------------------------------------------------------

# Creating sample dataset

# df1 = pd.DataFrame({

#     "TB_base_volume": df['TB Base Volume'].head(10),

#     "TB_quote_volume": df['TB Quote Volume'].head(10)

# })

# print(df['TB Base Volume'].head(10))

# print(df['TB Quote Volume'].head(10))

# df1.to_csv('sample1.csv')


# ----------------------------------------------------------------------------------------------


# Z Test calculations

df1 = pd.read_csv("sample1.csv")
alpha = 0.05

print("Statistical hypothesis:")
print("\tH0: u is from the large population")
print("\tH1: u is not from the large population")

mean1 = df1['TB_base_volume'].mean()

mean2 = df['TB Base Volume'].mean()


std1 = df['TB Base Volume'].std()

stderr1 = std1/sqrt(10)


t = (mean1-mean2)/(stderr1)

print("Conclusion:")
if t < 1.96 and t > -1.96:

    print("\tretain H0, this sample is from the large population")
else:
    print("\treject H0,this sample is not from the large population")
