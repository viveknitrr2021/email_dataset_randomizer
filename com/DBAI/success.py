import random
from com.DBAI import currency_list as cl

subjectlist = []
subjectlist.append("Account#1242 Settlement Successfull")
subjectlist.append("Account#1242 Settlement Completed")
subjectlist.append("Account#1242 Settlement Succeeded")
subjectlist.append("Account#1242 Settlement Cleared")

attachmentlist = []
attachmentlist.append('successstatement.Json')
attachmentlist.append('SuccessSettlement.txt')
attachmentlist.append('Success.json')
attachmentlist.append('Success statement.msg')

bodyparam1 = []
bodyparam1.append('Settlement is complete. Please find the confirmation')
bodyparam1.append("Settlement is done and parties have honored the amount")
bodyparam1.append("Settlement is Cleared and parties have honored the amount")

bodyparam2 = []
bodyparam2.append('Trade Success of ')
bodyparam2.append('Securities Loan success of Bonds worth ')
bodyparam2.append('Trade success of ')
bodyparam2.append('Trade completed of ')

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