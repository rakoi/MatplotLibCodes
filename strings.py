import xlrd,matplotlib.pyplot as plt
workbook=xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet=workbook.sheet_by_name('Table 9 ')


data=['counties','male','female','total']
countries=[]
male=[]
female=[]
total=[]
bins=[]

def sanitize(val):
    if val=='– ' or val=='–':
        return 0
    else:
        return val

for i in range(45,55):
    countries.append(sheet.row_values(i)[1])
    total.append(sanitize(sheet.row_values(i)[4]))
    female.append(sanitize(sheet.row_values(i)[6]))
    male.append(sanitize(sheet.row_values(i)[8]))

counter=0
for i in range(10):
    bins.append(counter)
    counter+=5

print(bins)
plt.xlabel('population')
plt.title('Child Labour')


plt.scatter(male,bins,label='male',marker='*',s=500)
plt.scatter(female,bins,marker='*',label='female',s=500)
#plt.hist(male,bins,histtype='bar')


plt.show()
