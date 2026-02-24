import matplotlib.pyplot as plt 
labels=[]
values=[]
n =int(input("enter number of categories:"))
for i in range (n):
     label=input(f"enter label {i+1}:")
     value=float(input(f"enter value for {label}:"))
     labels.append(label)
     values.append(value)
     plt.pie(values,labels=labels)
     plt.title("dynamic pie chart")
     plt.axis('equal')
     plt.show()