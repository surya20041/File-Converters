import pandas as pd
read_file = pd.read_csv("C:/Users/surya/OneDrive/Documents/Programs/File converters/Diabetes.txt")
read_file.to_csv ("C:/Users/surya/OneDrive/Documents/Programs/File converters/Diabetesfinal.csv", index=None)