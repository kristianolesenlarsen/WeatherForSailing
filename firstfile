import pandas as pd

df = pd.DataFrame({'0': [0, 3, 2],
                   '1': [2, 0, 3],
                   '2': [3, 2, 1]})



def cell_search(data):
    zeroes = []
    for i in range(0,3):                        #col
        for j in range(0,3):                    #row
            if data[str(j)][i] == 0:
                zeroes.append([int(j),i])       #col, row
                print(zeroes)
    return zeroes


def get_row(r,data):
    row = data.iloc[r]
    return row


def get_col(c,data):
    col = data[str(c)]
    return col

def easysolver(data):
    z = cell_search(data)
    for i in z:
        r = z[1]
        c = z[0]

        row = get_row(r = r, data = data)
        col = get_col(c = c, data = data)

        df_copy = pd.DataFrame(df.copy)

        if row.count(0) == 1:
            value = sum([1,2,3]) - sum(row)
            df_copy.set_value(r,c,value)
        elif col.count(0) == 1:
            value = sum([1,2,3]) - sum(col)
            df_copy.set_value(r,c,value)
    return df_copy


print(easysolver(df))