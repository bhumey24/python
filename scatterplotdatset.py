import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel("cleaned_customer_dataset.xlsx")     

x = data["LastPurchaseAmount"]
y = data["AnnualIncome"]

plt.scatter(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot from Excel Dataset")

plt.show()