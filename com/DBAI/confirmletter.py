import random
from com.DBAI import currency_list as cl

subjectlist = []
subjectlist.append("Confirmation of Funds certificate")
subjectlist.append("Bank Confirm Letter")

attachmentlist = []
attachmentlist.append('Confirm.Json')
attachmentlist.append('Confirmation.txt')
attachmentlist.append('Confirmation.json')
attachmentlist.append('confirmationstatement.msg')

bodyparam1 = []
bodyparam1.append('We the undersigned Bank confirm with full responsibility that the amount from the party is reserved on buyers requests for the purchase transaction of product (Bond value, Gold, Securities, Options)')
bodyparam1.append("PFA the Confirmation Letter")

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
    final_body = bp1 + "\nsee the following attachment \n" + attachment
    return final_body

def getrandomtext():
    final_text = getrandomsubject() + "\n" + generaterandombody()
    return final_text