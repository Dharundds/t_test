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


# T Test calculations

df1 = pd.read_csv("sample1.csv")

alpha = 0.5

degreeOfFreedom = 10-1

mean1 = df1['TB_base_volume'].mean()

mean2 = df['TB Base Volume'].mean()


std1 = df['TB Base Volume'].std()

stderr1 = std1/sqrt(10)


t = (mean1-mean2)/(stderr1)


if t < 2.262 and t > -2.262:

    print("retain H0, this sample is from the large population")


else:

    print("reject H0,this sample is not from the large population")
