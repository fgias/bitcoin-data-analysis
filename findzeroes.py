i_range = list(range(1, len(emadiff)))
zeroes=[]
direction=[]
for i in i_range:
    if (emadiff.reset_index().loc[i, 'close'] < 0 and emadiff.reset_index().loc[i-1, 'close'] > 0) or (emadiff.reset_index().loc[i, 'close'] > 0 and emadiff.reset_index().loc[i-1, 'close'] < 0): 
        zeroes.append(i)
        if (emadiff.reset_index().loc[i, 'close'] < 0 and emadiff.reset_index().loc[i-1, 'close'] > 0):
            direction.append('short')
        else:
            direction.append('long')


dates=[]       
for i in zeroes:
    dates.append(emadiff.reset_index().loc[i, 'ts'])

for j in range(len(dates)):
    print(dates[j])

