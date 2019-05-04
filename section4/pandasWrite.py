import pandas as pd

df = pd.read_csv('csv_s2.csv', sep = ';', skiprows = [0], header = None, names = ['Name', 'Test1', 'Test2', 'Test3', 'Final', 'Grade'])
df['Average'] = df[['Test1', 'Test2', 'Test3', 'Final']].mean(axis = 1)

print(df)

df.to_csv('result_s2.csv', index = False)
