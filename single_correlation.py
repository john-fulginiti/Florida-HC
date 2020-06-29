import pandas as pd
#from decimal import Decimal
book = pd.read_csv(r'C:\Users\John Fulginiti\Documents\FLORIDA HC\leoncountywkbk.csv' )

#l is the number of useful columns  starting at 0
l = int(len(book.columns)-1)

#removing Geo ID column
col_list = []
for col in book.columns:
    if col not in ['GEO_ID']:
        col_list.append(col)

#creating dictionary so that inputs can be numbers instead of words
#col_dict maps 0-l to the column titles of book
#print(col_list)
col_dict = {}
i = 0
for item in col_list:
    col_dict[i] = locals()['item']  #locals() grabs the current value of 'item'.  this line maps a new entry in col_d with key 'i' to item value
    i += 1
i = int(i)
print(col_dict)

var1 = int(input('Enter first variable: '))
var2 = int(input('Enter second variable: '))



for k in range(l):  #range does not include the last number, so this only runs 27 times instead of 28
    if var1 == k:
        var1 = col_dict[k]
    elif var2 == k:
        var2 = col_dict[k]

print('Correlation between ' + var1 + ' and ' + var2 + ': ')

r = book[var1].corr(book[var2])
print(r)


