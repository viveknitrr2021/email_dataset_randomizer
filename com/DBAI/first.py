import pandas
import confirmaffirm

df = pandas.read_csv("D:/pythonAutomation/com/resources/spam_ham_dataset.csv")

# for i in range(5):
#     print(df.iloc[i, 0])
#     df.iloc[i,1] = df.iloc[i,0].replace("hello")
#     print(df.iloc[i, 1])
#     print(df.iloc[i, 2])
#     print(100*"-")

var = 0
#
for index in df.index:
    var += 1
    print(df.loc[index,'label'])
    print(50*"&")
    print(df.loc[index,'text'])
    print(50*"&")
    print(df.loc[index,'label_num'])
    print(100*"-")
    if var == 5:
        break




# for index, row in df.iterrows():
#     df.at[index,'text'] = 'Hello'
#
# for index in df.index:
#     var += 1
#     print(df.loc[index,'label'])
#     print(df.loc[index,'text'])
#     print(df.loc[index,'label_num'])
#     print(100*"-")
#     if var == 5:
#         break

# df.to_csv('newfile.csv')

