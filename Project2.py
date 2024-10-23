#Code for :
#STUDENT RESULT ANALYSIS USING PYTHON



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Expanded_data_with_more_features.csv")
print(df.head())
print(df.describe())
print(df.info())
print(df.isnull().sum())
df = df.drop("Unnamed: 0",axis=1)
print(df.head())
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()
gb = df.groupby("ParentEduc").agg({"MathScore": 'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)
sns.heatmap(gb,annot=True)
plt.title("Marks Distribution According to Parents Education")
plt.show()
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": 'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)
sns.heatmap(gb1,annot=True)
plt.title("Marks Distribution According to Parents Marital Status")
plt.show()
sns.boxplot(data=df,x="MathScore")
plt.title("Maths Score")
plt.show()
sns.boxplot(data=df,x="ReadingScore")
plt.title("Reading Score")
plt.show()
sns.boxplot(data=df,x="WritingScore")
plt.title("Writing Score")
plt.show()
print(df["EthnicGroup"].unique())

groupA=df.loc[(df["EthnicGroup"]=="group A" )].count()
groupB=df.loc[(df["EthnicGroup"]=="group B" )].count()
groupC=df.loc[(df["EthnicGroup"]=="group C" )].count()
groupD=df.loc[(df["EthnicGroup"]=="group D" )].count()
groupE=df.loc[(df["EthnicGroup"]=="group E" )].count()

l=["group A","group B","group C","group D","group E"]
mylist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mylist,labels=l,autopct="%1.2f%%")
plt.title("Distribution Of Ethnic Groups")
plt.show()
