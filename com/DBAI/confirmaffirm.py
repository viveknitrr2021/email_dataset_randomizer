import random

currency_list = {
    'ALL': 'Albania Lek',
    'AFN': 'Afghanistan Afghani',
    'ARS': 'Argentina Peso',
    'AWG': 'Aruba Guilder',
    'AUD': 'Australia Dollar',
    'AZN': 'Azerbaijan New Manat',
    'BSD': 'Bahamas Dollar',
    'BBD': 'Barbados Dollar',
    'BDT': 'Bangladeshi taka',
    'BYR': 'Belarus Ruble',
    'BZD': 'Belize Dollar',
    'BMD': 'Bermuda Dollar',
    'BOB': 'Bolivia Boliviano',
    'BAM': 'Bosnia and Herzegovina Convertible Marka',
    'BWP': 'Botswana Pula',
    'BGN': 'Bulgaria Lev',
    'BRL': 'Brazil Real',
    'BND': 'Brunei Darussalam Dollar',
    'KHR': 'Cambodia Riel',
    'CAD': 'Canada Dollar',
    'KYD': 'Cayman Islands Dollar',
    'CLP': 'Chile Peso',
    'CNY': 'China Yuan Renminbi',
    'COP': 'Colombia Peso',
    'CRC': 'Costa Rica Colon',
    'HRK': 'Croatia Kuna',
    'CUP': 'Cuba Peso',
    'CZK': 'Czech Republic Koruna',
    'DKK': 'Denmark Krone',
    'DOP': 'Dominican Republic Peso',
    'XCD': 'East Caribbean Dollar',
    'EGP': 'Egypt Pound',
    'SVC': 'El Salvador Colon',
    'EEK': 'Estonia Kroon',
    'EUR': 'Euro Member Countries',
    'FKP': 'Falkland Islands (Malvinas) Pound',
    'FJD': 'Fiji Dollar',
    'GHC': 'Ghana Cedis',
    'GIP': 'Gibraltar Pound',
    'GTQ': 'Guatemala Quetzal',
    'GGP': 'Guernsey Pound',
    'GYD': 'Guyana Dollar',
    'HNL': 'Honduras Lempira',
    'HKD': 'Hong Kong Dollar',
    'HUF': 'Hungary Forint',
    'ISK': 'Iceland Krona',
    'INR': 'India Rupee',
    'IDR': 'Indonesia Rupiah',
    'IRR': 'Iran Rial',
    'IMP': 'Isle of Man Pound',
    'ILS': 'Israel Shekel',
    'JMD': 'Jamaica Dollar',
    'JPY': 'Japan Yen',
    'JEP': 'Jersey Pound',
    'KZT': 'Kazakhstan Tenge',
    'KPW': 'Korea (North) Won',
    'KRW': 'Korea (South) Won',
    'KGS': 'Kyrgyzstan Som',
    'LAK': 'Laos Kip',
    'LVL': 'Latvia Lat',
    'LBP': 'Lebanon Pound',
    'LRD': 'Liberia Dollar',
    'LTL': 'Lithuania Litas',
    'MKD': 'Macedonia Denar',
    'MYR': 'Malaysia Ringgit',
    'MUR': 'Mauritius Rupee',
    'MXN': 'Mexico Peso',
    'MNT': 'Mongolia Tughrik',
    'MZN': 'Mozambique Metical',
    'NAD': 'Namibia Dollar',
    'NPR': 'Nepal Rupee',
    'ANG': 'Netherlands Antilles Guilder',
    'NZD': 'New Zealand Dollar',
    'NIO': 'Nicaragua Cordoba',
    'NGN': 'Nigeria Naira',
    'NOK': 'Norway Krone',
    'OMR': 'Oman Rial',
    'PKR': 'Pakistan Rupee',
    'PAB': 'Panama Balboa',
    'PYG': 'Paraguay Guarani',
    'PEN': 'Peru Nuevo Sol',
    'PHP': 'Philippines Peso',
    'PLN': 'Poland Zloty',
    'QAR': 'Qatar Riyal',
    'RON': 'Romania New Leu',
    'RUB': 'Russia Ruble',
    'SHP': 'Saint Helena Pound',
    'SAR': 'Saudi Arabia Riyal',
    'RSD': 'Serbia Dinar',
    'SCR': 'Seychelles Rupee',
    'SGD': 'Singapore Dollar',
    'SBD': 'Solomon Islands Dollar',
    'SOS': 'Somalia Shilling',
    'ZAR': 'South Africa Rand',
    'LKR': 'Sri Lanka Rupee',
    'SEK': 'Sweden Krona',
    'CHF': 'Switzerland Franc',
    'SRD': 'Suriname Dollar',
    'SYP': 'Syria Pound',
    'TWD': 'Taiwan New Dollar',
    'THB': 'Thailand Baht',
    'TTD': 'Trinidad and Tobago Dollar',
    'TRY': 'Turkey Lira',
    'TRL': 'Turkey Lira',
    'TVD': 'Tuvalu Dollar',
    'UAH': 'Ukraine Hryvna',
    'GBP': 'United Kingdom Pound',
    'USD': 'United States Dollar',
    'UYU': 'Uruguay Peso',
    'UZS': 'Uzbekistan Som',
    'VEF': 'Venezuela Bolivar',
    'VND': 'Viet Nam Dong',
    'YER': 'Yemen Rial',
    'ZWD': 'Zimbabwe Dollar'
}


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
for row in currency_list:
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
