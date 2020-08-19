import tkinter as tk
import pandas as pd


deviceList = pd.read_excel("D:\\검교정관리대장.xlsx")

colomnList = deviceList.columns.tolist()
colomnList_lbl = list()




root=tk.Tk()

# Frame 분할


upperFrame = tk.LabelFrame(root, text="upperFrame", padx=10, pady=10)
upperFrame.pack(padx=5, pady=5)
lowerFrame = tk.LabelFrame(root, text="lowerFrame", padx=10, pady=10)
lowerFrame.pack(padx=5, pady=5)


importFile_btn = tk.Button(upperFrame, text="Import").grid(row=0, column=0)
exportFile_btn = tk.Button(upperFrame, text='Export').grid(row=1, column=0)


for i in range (len(colomnList)):
    j = colomnList[i] + "_lbl"
    colomnList_lbl.append(j)
    tk.Label(lowerFrame, text=colomnList[i]).grid(row=0, column=i)

for i in range (len(colomnList)):
    for j in range(len(deviceList.index)):
        tk.Label(lowerFrame, text=deviceList.iloc[j,i]).grid(row=j+1, column=i)

root.mainloop()