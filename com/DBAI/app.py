import pandas
import confirmaffirm
import failure
import success
import confirmletter

df = pandas.read_csv("D:/DBAI/email_dataset_randomizer/resources/spam_ham_dataset.csv")

print(confirmaffirm.getrandomtext())
print(100*"-")
print(failure.getrandomtext())
print(100*"-")
print(success.getrandomtext())
print(100*"-")
print(confirmletter.getrandomtext())

switchvar = 0

for index, row in df.iterrows():
    if(index%2 == 0):
        df.at[index,'text'] = confirmaffirm.getrandomtext()
        df.at[index,'label'] = "confirmaffirm"
    else:
        if(index%5 == 0):
            df.at[index,'text'] = confirmletter.getrandomtext()
            df.at[index,'label'] = "confirmletter"
        else:
            if(switchvar%2 == 0):
                df.at[index,'text'] = failure.getrandomtext()
                df.at[index,'label'] = "settlementFailure"
                switchvar += 1
            else:
                df.at[index,'text'] = success.getrandomtext()
                df.at[index,'label'] = "settlementSuccess"
                switchvar += 1

df.to_csv("D:/DBAI/email_dataset_randomizer/resources/newfile.csv")