import csv
import pandas as pd
colnames = ['first', 'last', 'char', 'password']
data = pd.read_csv(r'done\advent\passes.csv', names=colnames, sep=';')
df = pd.DataFrame(data)

# this is the function for the first part of the task


def countchars(x, y, f, l):
    a = x.count(y)
    if a >= f and a <= l:
        return True
    else:
        return False


df['a'] = df.apply(lambda row: countchars(
    row['password'], row['char'], row['first'], row['last']), axis=1)
print(df.a.value_counts())


# this is the function for the second part of the task
def position(password, char, first, last):
    indices = [i + 1 for i, x in enumerate(password) if x == char]
    a = first in indices
    b = last in indices
    if a ^ b:
        return True
    else:
        return False


df['b'] = df.apply(lambda row: position(
    row['password'], row['char'], row['first'], row['last']), axis=1)
print(df.b.value_counts())
