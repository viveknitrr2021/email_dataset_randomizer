import random
from com.DBAI import currency_list as cl

subjectlist = []
subjectlist.append("Account#1242 Insufficient Funds")
subjectlist.append("Account#1242 Insufficient Collateral")
subjectlist.append("Account#1242 Mandate Rejected")
subjectlist.append("Account#1242 Trade78780we Failed")

attachmentlist = []
attachmentlist.append('failurestatement.Json')
attachmentlist.append('Failedsettlement.txt')
attachmentlist.append('Failed.json')
attachmentlist.append('Failure statement.msg')

bodyparam1 = []
bodyparam1.append('Insufficient funds in account projected for upcoming trade')
bodyparam1.append("Insufficient collateral value as per today's MTM (Mark to Market ) Statement")
bodyparam1.append('Provided Mandate is rejected')
bodyparam1.append('Trade record is failed')

bodyparam2 = []
bodyparam2.append('Trade failure of ')
bodyparam2.append('Securities Loan Failed of Bonds worth ')
bodyparam2.append('Trade Failure of ')
bodyparam2.append('Trade failed of ')

list_cur = []
cur_list  = cl.currency_list
for row in cur_list:
    list_cur.append(row)

def getrandomattachment():
    end = len(attachmentlist)
    index = random.randint(0,end-1)
    return attachmentlist[index]

def getrandomsubject():
    end = len(subjectlist)
    index = random.randint(0,end-1)
    return subjectlist[index]

def getrandomcurrency():
    end = len(list_cur)
    index = random.randint(0,end-1)
    return list_cur[index]

def generaterandombody():
    cur = getrandomcurrency()
    attachment = getrandomattachment()
    amount = random.randrange(100,9999999999)
    bp1 = bodyparam1[random.randint(0, len(bodyparam1)-1)]
    bp2 = bodyparam2[random.randint(0, len(bodyparam2)-1)] + str(amount) + " "  + cur
    final_body = bp1 + "\n" + bp2 + "\nsee the following attachment \n" + attachment
    return final_body

def getrandomtext():
    final_text = getrandomsubject() + "\n" + generaterandombody()
    return final_text