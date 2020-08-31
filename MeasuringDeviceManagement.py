import tkinter as tk
import pandas as pd
from tkinter import filedialog

# deviceList = pd.read_excel("D:\\검교정관리대장.xlsx")

# colomnList = deviceList.columns.tolist()
# colomnList_lbl = list()



# for i in range (len(deviceList.index)):
#     print(deviceInfo(i))

root=tk.Tk()




def importDB():
    global deviceList
    global columnList
    mainFrame1.filename = filedialog.askopenfilename(initialdir = '/', title = 'select file')
    deviceList = pd.read_excel(mainFrame1.filename)
    columnList = createColumnlist_list(deviceList)
    showColumnlist_lbl(columnList, mainFrame2)
    deviceTable = createDeviceTable_list()
    print(deviceTable[0][0])


def createColumnlist_list(deviceList):
    return deviceList.columns.tolist()

def showColumnlist_lbl(columnlist, frame):
    for i in range(len(columnlist)):
        tk.Label(frame, text=columnlist[i]).grid(row=0, column=i)




def createDeviceInfo_list(index_num):
    return deviceList.iloc[index_num].tolist()



def createDeviceTable_list():
    deviceTable = list()
    for i in range(len(deviceList.index)):
        device = createDeviceInfo_list(i)
        deviceTable.append(device)
    return deviceTable
    

    # for i in range(len(deviceInfo)):
    #     e = tk.Entry(frame)
    #     e.grid(row=index_num+1, column=i)
    #     e.insert(0, deviceInfo[i])


# def showDB():


# def exportDB():
#     for i in range(len(columnList)):
#         e = 









# Frame 분할
mainFrame1 = tk.LabelFrame(root, text="Main Menu", padx=10, pady=10)
mainFrame1.pack(padx=5, pady=5)
mainFrame2 = tk.LabelFrame(root, text="Device Records", padx=10, pady=10)
mainFrame2.pack(padx=5, pady=5)


importFile_btn = tk.Button(mainFrame1, text="Import DB", command=importDB)
importFile_btn.grid(row=0, column=0)
exportFile_btn = tk.Button(mainFrame1, text="Export DB")
exportFile_btn.grid(row=1, column=0)
deleteRecord_btn = tk.Button(mainFrame1, text="Delete Record")
deleteRecord_btn.grid(row=2,column=1)
createRecord_btn = tk.Button(mainFrame1, text="Create Record")
createRecord_btn.grid(row=2, column=2)
saveToDB_btn = tk.Button(mainFrame1, text="Save To DB")
saveToDB_btn.grid(row=2,column=0)

# for i in range (len(colomnList)):
#     j = colomnList[i] + "_lbl"
#     colomnList_lbl.append(j)
#     tk.Label(mainFrame2, text=colomnList[i]).grid(row=0, column=i)

# for i in range (len(colomnList)):
#     for j in range(len(deviceList.index)):
#         tk.Label(mainFrame2, text=deviceList.iloc[j,i]).grid(row=j+1, column=i)

root.mainloop()