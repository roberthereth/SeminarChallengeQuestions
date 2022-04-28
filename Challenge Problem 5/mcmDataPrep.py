import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Getting File from User Window
root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilename()

# Reading Data and Column Names
data = pd.read_csv(files)
cols = data.columns

# Making Institution ID Numbers
ins = data[cols[0]]
insDic = {"0":"0"}
n = 1
for i in ins:
    if(i not in insDic):
        insDic[i] = n
        n += 1
insID = []
for i in ins:
    insID.append(insDic[i])

# Prepping Institution CSV
insDS = pd.DataFrame()
insDS["Institution ID"] = insID
insDS["Institution Name"] = ins
insDS["City"] = data[cols[2]]
insDS["State/Province"] = data[cols[3]]
insDS["Country"] = data[cols[4]]
insDS = insDS.drop_duplicates()

# Prepping Teams CSV
teamDS = pd.DataFrame()
teamDS["Team Number"] = data[cols[1]]
teamDS["Advisor"] = data[cols[5]]
teamDS["Problem"] = data[cols[6]]
teamDS["Ranking"] = data[cols[7]]
teamDS["Institution ID"] = insID

# Writing to CSV Files
insDS.to_csv("Institutions.csv", index=False)
teamDS.to_csv("Teams.csv", index=False)