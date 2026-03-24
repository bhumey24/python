import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("cleaned_customer_dataset.xlsx")


data = df["Age"]    


plt.boxplot(data)

plt.title("Boxplot of Dataset")
plt.show()