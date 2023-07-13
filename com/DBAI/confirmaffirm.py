import random
import currency_list as cl

subjectlist = []
subjectlist.append("MT 517")
subjectlist.append("MT 518")
subjectlist.append("MT 515")
subjectlist.append("MT 515(FUNDS)")
subjectlist.append("MT 516")
subjectlist.append("Confirmation Details")

attachmentlist = []
attachmentlist.append('Confirmation statement.json')
attachmentlist.append('statement.txt')
attachmentlist.append('Affirmation statement.json')
attachmentlist.append('Affirmation statement.msg')

bodyparam1 = []
bodyparam1.append('Trade Date')
bodyparam1.append('Settlement Date')
bodyparam1.append('Trade affirmation Summary Report')

bodyparam2 = []
bodyparam2.append('Trade Confirmation Affirmation of ')
bodyparam2.append('Client Confirmation of Purchase or Sale (FUNDS) amounted to ')
bodyparam2.append('Securities Loan Confirmation of Bonds worth ')
bodyparam2.append('Trade Confirmation Affirmation of ')
bodyparam2.append('Trade Affirmation Confirmation of ')

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
