# 1. Create a Python script that removes all the elements of a list that are duplicates.
# Do the challenge in a single line of code using sets.
list=[1,5,4,8,8,9,4,7,2,8]
unique=[]
for item in list:
    if item not in unique:
        unique.append(item)
print(unique)
print(set(list))
alternative with set
print(set([1,5,4,8,8,9,4,7,2,8]))

# 2. Consider a list of words (strings). Write a Python script that generates a dictionary where
# the key is the word in the list and the value is its length.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}
my_list= ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
item_lenght= dict()
for item in my_list:
    item_lenght[item]=len(item)
print(item_lenght)

# 3 Considering the following dict, get a dict representation sorted by key.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# A dict representation means viewing or printing the dict.
d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
for k in sorted(d1.keys()):
    print(f'{k}----{d1[k]}')

# 4 Considering the following dict, get a dict representation sorted by value. d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
new_dict= sorted(d1.items(), key= lambda v: v[1])
print(new_dict)

# 5 Let's generalize the last challenge and sort a dictionary by any field of its values if
# the value is a composite type (list, tuple, etc).
# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]

employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
sorting=sorted(employees.items(), key=lambda s: s[1][1])
print(sorting)

# 6 Print a sorted view of the same dictionary by the third field of its values, in reverse order.

employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
new_order= sorted(employees.items(), key=lambda n:n[1][2], reverse= True)
print(new_order)

# 7 The keys are the country codes and the values are the country names.
# Print a sorted view of the dictionary, by the key (country code).
COUNTRY = {
"MX":"MEXICO",
"RW":"RWANDA",
"BI":"BURUNDI",
"PR":"PUERTO RICO",
"GM":"GAMBIA",
"SR":"SURINAME",
"KG":"KYRGYZSTAN",
"GA":"GABON",
"CK":"COOK ISLANDS",
"VN":"VIET NAM",
"UZ":"UZBEKISTAN",
"BG":"BULGARIA",
"JP":"JAPAN",
"KP":"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
"PL":"POLAND",
"BB":"BARBADOS",
"CF":"CENTRAL AFRICAN REPUBLIC",
"GI":"GIBRALTAR",
"AE":"UNITED ARAB EMIRATES",
"MY":"MALAYSIA",
"KI":"KIRIBATI",
"RU":"RUSSIAN FEDERATION",
"MQ":"MARTINIQUE",
"SB":"SOLOMON ISLANDS",
"TL":"TIMOR-LESTE",
"VI":"VIRGIN ISLANDS, U.S.",
"FR":"FRANCE",
"ZA":"SOUTH AFRICA",
"NE":"NIGER",
"IE":"IRELAND",
"MG":"MADAGASCAR",
"TC":"TURKS AND CAICOS ISLANDS",
"BW":"BOTSWANA",
"KY":"CAYMAN ISLANDS",
"JO":"JORDAN",
"MR":"MAURITANIA",
"NI":"NICARAGUA",
"KM":"COMOROS",
"FK":"FALKLAND ISLANDS (MALVINAS)",
"SH":"SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
"PF":"FRENCH POLYNESIA",
"DK":"DENMARK",
"PT":"PORTUGAL",
"NR":"NAURU",
"DM":"DOMINICA",
"GH":"GHANA",
"GP":"GUADELOUPE",
"CU":"CUBA",
"GR":"GREECE",
"AS":"AMERICAN SAMOA",
"AI":"ANGUILLA",
"LS":"LESOTHO",
"TJ":"TAJIKISTAN",
"AW":"ARUBA",
"GY":"GUYANA",
"LC":"SAINT LUCIA",
"GG":"GUERNSEY",
"TG":"TOGO",
"OM":"OMAN",
"NL":"NETHERLANDS",
"MT":"MALTA",
"MD":"MOLDOVA, REPUBLIC OF",
"EC":"ECUADOR",
"FM":"MICRONESIA, FEDERATED STATES OF",
"CA":"CANADA",
"TT":"TRINIDAD AND TOBAGO",
"CN":"CHINA",
"CM":"CAMEROON",
"BD":"BANGLADESH",
"LK":"SRI LANKA",
"CO":"COLOMBIA",
"LT":"LITHUANIA",
"DJ":"DJIBOUTI",
"CX":"CHRISTMAS ISLAND",
"TF":"FRENCH SOUTHERN TERRITORIES",
"TM":"TURKMENISTAN",
"SC":"SEYCHELLES",
"MK":"MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
"TH":"THAILAND",
"LA":"LAO PEOPLE'S DEMOCRATIC REPUBLIC",
"BE":"BELGIUM",
"UY":"URUGUAY",
"MV":"MALDIVES",
"SZ":"SWAZILAND",
"MN":"MONGOLIA",
"PK":"PAKISTAN",
"BZ":"BELIZE",
"AT":"AUSTRIA",
"WF":"WALLIS AND FUTUNA",
"GD":"GRENADA",
"RO":"ROMANIA",
"SJ":"SVALBARD AND JAN MAYEN",
"CV":"CAPE VERDE",
"UG":"UGANDA",
"CR":"COSTA RICA",
"HM":"HEARD ISLAND AND MCDONALD ISLANDS",
"TN":"TUNISIA",
"MC":"MONACO",
"MP":"NORTHERN MARIANA ISLANDS",
"SN":"SENEGAL",
"PW":"PALAU",
"VC":"SAINT VINCENT AND THE GRENADINES",
"ST":"SAO TOME AND PRINCIPE",
"DO":"DOMINICAN REPUBLIC",
"EG":"EGYPT",
"TZ":"TANZANIA, UNITED REPUBLIC OF",
"SV":"EL SALVADOR",
"TR":"TURKEY",
"SG":"SINGAPORE",
"UM":"UNITED STATES MINOR OUTLYING ISLANDS",
"KR":"KOREA, REPUBLIC OF",
"PG":"PAPUA NEW GUINEA",
"GQ":"EQUATORIAL GUINEA",
"US":"UNITED STATES",
"BF":"BURKINA FASO",
"AM":"ARMENIA",
"TD":"CHAD",
"NP":"NEPAL",
"IT":"ITALY",
"IO":"BRITISH INDIAN OCEAN TERRITORY",
"ZW ":"ZIMBABWE",
"HU":"HUNGARY",
"BR":"BRAZIL",
"IN":"INDIA",
"PH":"PHILIPPINES",
"TW":"TAIWAN, PROVINCE OF CHINA",
"AO":"ANGOLA",
"MH":"MARSHALL ISLANDS",
"NO":"NORWAY",
"JE":"JERSEY",
"VU":"VANUATU",
"EE":"ESTONIA",
"AF":"AFGHANISTAN",
"AX":"ALAND ISLANDS",
"GN":"GUINEA",
"FO":"FAROE ISLANDS",
"SE":"SWEDEN",
"SL":"SIERRA LEONE",
"LB":"LEBANON",
"MO":"MACAO",
"IR":"IRAN, ISLAMIC REPUBLIC OF",
"CG":"CONGO",
"SM":"SAN MARINO",
"NA":"NAMIBIA",
"CI":"COTE D'IVOIRE",
"GL":"GREENLAND",
"VE":"VENEZUELA, BOLIVARIAN REPUBLIC OF",
"VG":"VIRGIN ISLANDS, BRITISH",
"BH":"BAHRAIN",
"ZM":"ZAMBIA",
"HR":"CROATIA",
"MZ":"MOZAMBIQUE",
"KW":"KUWAIT",
"MA":"MOROCCO",
"DZ":"ALGERIA",
"AQ":"ANTARCTICA",
"AU":"AUSTRALIA",
"PN":"PITCAIRN",
"QA":"QATAR",
"AL":"ALBANIA",
"BN":"BRUNEI DARUSSALAM",
"NZ":"NEW ZEALAND",
"SA":"SAUDI ARABIA",
"RE":"REUNION",
"HK":"HONG KONG",
"CD":"CONGO, THE DEMOCRATIC REPUBLIC OF THE",
"MW":"MALAWI",
"CZ":"CZECH REPUBLIC",
"DE":"GERMANY",
"AD":"ANDORRA",
"LU":"LUXEMBOURG",
"CY":"CYPRUS",
"TO":"TONGA",
"FJ":"FIJI",
"GT":"GUATEMALA",
"LV":"LATVIA",
"ES":"SPAIN",
"SI":"SLOVENIA",
"IM":"ISLE OF MAN",
"BS":"BAHAMAS",
"RS":"SERBIA",
"WS":"SAMOA",
"NC":"NEW CALEDONIA",
"SY":"SYRIAN ARAB REPUBLIC",
"MS":"MONTSERRAT",
"GB":"UNITED KINGDOM",
"PM":"SAINT PIERRE AND MIQUELON",
"CL":"CHILE",
"MF":"SAINT MARTIN",
"SO":"SOMALIA",
"BJ":"BENIN",
"YE":"YEMEN",
"TV":"TUVALU",
"GE":"GEORGIA",
"BM":"BERMUDA",
"GS":"SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
"AN":"NETHERLANDS ANTILLES",
"BY":"BELARUS",
"FI":"FINLAND",
"BV":"BOUVET ISLAND",
"LR":"LIBERIA",
"KH":"CAMBODIA",
"LY":"LIBYAN ARAB JAMAHIRIYA",
"MU":"MAURITIUS",
"GU":"GUAM",
"ER":"ERITREA",
"LI":"LIECHTENSTEIN",
"SD":"SUDAN",
"PA":"PANAMA",
"IL":"ISRAEL",
"EH":"WESTERN SAHARA",
"KE":"KENYA",
"CC":"COCOS (KEELING) ISLANDS",
"IS":"ICELAND",
"GF":"FRENCH GUIANA",
"MM":"MYANMAR",
"HT":"HAITI",
"NF":"NORFOLK ISLAND",
"ML":"MALI",
"PY":"PARAGUAY",
"KZ":"KAZAKHSTAN",
"CH":"SWITZERLAND",
"BA":"BOSNIA AND HERZEGOVINA",
"BO":"BOLIVIA, PLURINATIONAL STATE OF",
"UA":"UKRAINE",
"BL":"SAINT BARTHELEMY",
"AZ":"AZERBAIJAN",
"BT":"BHUTAN",
"VA":"HOLY SEE (VATICAN CITY STATE)",
"PE":"PERU",
"AR":"ARGENTINA",
"TK":"TOKELAU",
"AG":"ANTIGUA AND BARBUDA",
"KN":"SAINT KITTS AND NEVIS",
"PS":"PALESTINIAN TERRITORY, OCCUPIED",
"ID":"INDONESIA",
"GW":"GUINEA-BISSAU",
"HN":"HONDURAS",
"NG":"NIGERIA",
"IQ":"IRAQ",
"JM":"JAMAICA",
"NU":"NIUE",
"ET":"ETHIOPIA",
"ME":"MONTENEGRO",
"SK":"SLOVAKIA",
"YT":"MAYOTTE"
}
for k in sorted(COUNTRY.keys()):
    print(f'{k}:{COUNTRY[k]}')

# 8 Find the country which has the longest name.
# Use list comprehension if possible.
COUNTRY = {
"MX":"MEXICO",
"RW":"RWANDA",
"BI":"BURUNDI",
"PR":"PUERTO RICO",
"GM":"GAMBIA",
"SR":"SURINAME",
"KG":"KYRGYZSTAN",
"GA":"GABON",
"CK":"COOK ISLANDS",
"VN":"VIET NAM",
"UZ":"UZBEKISTAN",
"BG":"BULGARIA",
"JP":"JAPAN",
"KP":"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
"PL":"POLAND",
"BB":"BARBADOS",
"CF":"CENTRAL AFRICAN REPUBLIC",
"GI":"GIBRALTAR",
"AE":"UNITED ARAB EMIRATES",
"MY":"MALAYSIA",
"KI":"KIRIBATI",
"RU":"RUSSIAN FEDERATION",
"MQ":"MARTINIQUE",
"SB":"SOLOMON ISLANDS",
"TL":"TIMOR-LESTE",
"VI":"VIRGIN ISLANDS, U.S.",
"FR":"FRANCE",
"ZA":"SOUTH AFRICA",
"NE":"NIGER",
"IE":"IRELAND",
"MG":"MADAGASCAR",
"TC":"TURKS AND CAICOS ISLANDS",
"BW":"BOTSWANA",
"KY":"CAYMAN ISLANDS",
"JO":"JORDAN",
"MR":"MAURITANIA",
"NI":"NICARAGUA",
"KM":"COMOROS",
"FK":"FALKLAND ISLANDS (MALVINAS)",
"SH":"SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
"PF":"FRENCH POLYNESIA",
"DK":"DENMARK",
"PT":"PORTUGAL",
"NR":"NAURU",
"DM":"DOMINICA",
"GH":"GHANA",
"GP":"GUADELOUPE",
"CU":"CUBA",
"GR":"GREECE",
"AS":"AMERICAN SAMOA",
"AI":"ANGUILLA",
"LS":"LESOTHO",
"TJ":"TAJIKISTAN",
"AW":"ARUBA",
"GY":"GUYANA",
"LC":"SAINT LUCIA",
"GG":"GUERNSEY",
"TG":"TOGO",
"OM":"OMAN",
"NL":"NETHERLANDS",
"MT":"MALTA",
"MD":"MOLDOVA, REPUBLIC OF",
"EC":"ECUADOR",
"FM":"MICRONESIA, FEDERATED STATES OF",
"CA":"CANADA",
"TT":"TRINIDAD AND TOBAGO",
"CN":"CHINA",
"CM":"CAMEROON",
"BD":"BANGLADESH",
"LK":"SRI LANKA",
"CO":"COLOMBIA",
"LT":"LITHUANIA",
"DJ":"DJIBOUTI",
"CX":"CHRISTMAS ISLAND",
"TF":"FRENCH SOUTHERN TERRITORIES",
"TM":"TURKMENISTAN",
"SC":"SEYCHELLES",
"MK":"MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
"TH":"THAILAND",
"LA":"LAO PEOPLE'S DEMOCRATIC REPUBLIC",
"BE":"BELGIUM",
"UY":"URUGUAY",
"MV":"MALDIVES",
"SZ":"SWAZILAND",
"MN":"MONGOLIA",
"PK":"PAKISTAN",
"BZ":"BELIZE",
"AT":"AUSTRIA",
"WF":"WALLIS AND FUTUNA",
"GD":"GRENADA",
"RO":"ROMANIA",
"SJ":"SVALBARD AND JAN MAYEN",
"CV":"CAPE VERDE",
"UG":"UGANDA",
"CR":"COSTA RICA",
"HM":"HEARD ISLAND AND MCDONALD ISLANDS",
"TN":"TUNISIA",
"MC":"MONACO",
"MP":"NORTHERN MARIANA ISLANDS",
"SN":"SENEGAL",
"PW":"PALAU",
"VC":"SAINT VINCENT AND THE GRENADINES",
"ST":"SAO TOME AND PRINCIPE",
"DO":"DOMINICAN REPUBLIC",
"EG":"EGYPT",
"TZ":"TANZANIA, UNITED REPUBLIC OF",
"SV":"EL SALVADOR",
"TR":"TURKEY",
"SG":"SINGAPORE",
"UM":"UNITED STATES MINOR OUTLYING ISLANDS",
"KR":"KOREA, REPUBLIC OF",
"PG":"PAPUA NEW GUINEA",
"GQ":"EQUATORIAL GUINEA",
"US":"UNITED STATES",
"BF":"BURKINA FASO",
"AM":"ARMENIA",
"TD":"CHAD",
"NP":"NEPAL",
"IT":"ITALY",
"IO":"BRITISH INDIAN OCEAN TERRITORY",
"ZW ":"ZIMBABWE",
"HU":"HUNGARY",
"BR":"BRAZIL",
"IN":"INDIA",
"PH":"PHILIPPINES",
"TW":"TAIWAN, PROVINCE OF CHINA",
"AO":"ANGOLA",
"MH":"MARSHALL ISLANDS",
"NO":"NORWAY",
"JE":"JERSEY",
"VU":"VANUATU",
"EE":"ESTONIA",
"AF":"AFGHANISTAN",
"AX":"ALAND ISLANDS",
"GN":"GUINEA",
"FO":"FAROE ISLANDS",
"SE":"SWEDEN",
"SL":"SIERRA LEONE",
"LB":"LEBANON",
"MO":"MACAO",
"IR":"IRAN, ISLAMIC REPUBLIC OF",
"CG":"CONGO",
"SM":"SAN MARINO",
"NA":"NAMIBIA",
"CI":"COTE D'IVOIRE",
"GL":"GREENLAND",
"VE":"VENEZUELA, BOLIVARIAN REPUBLIC OF",
"VG":"VIRGIN ISLANDS, BRITISH",
"BH":"BAHRAIN",
"ZM":"ZAMBIA",
"HR":"CROATIA",
"MZ":"MOZAMBIQUE",
"KW":"KUWAIT",
"MA":"MOROCCO",
"DZ":"ALGERIA",
"AQ":"ANTARCTICA",
"AU":"AUSTRALIA",
"PN":"PITCAIRN",
"QA":"QATAR",
"AL":"ALBANIA",
"BN":"BRUNEI DARUSSALAM",
"NZ":"NEW ZEALAND",
"SA":"SAUDI ARABIA",
"RE":"REUNION",
"HK":"HONG KONG",
"CD":"CONGO, THE DEMOCRATIC REPUBLIC OF THE",
"MW":"MALAWI",
"CZ":"CZECH REPUBLIC",
"DE":"GERMANY",
"AD":"ANDORRA",
"LU":"LUXEMBOURG",
"CY":"CYPRUS",
"TO":"TONGA",
"FJ":"FIJI",
"GT":"GUATEMALA",
"LV":"LATVIA",
"ES":"SPAIN",
"SI":"SLOVENIA",
"IM":"ISLE OF MAN",
"BS":"BAHAMAS",
"RS":"SERBIA",
"WS":"SAMOA",
"NC":"NEW CALEDONIA",
"SY":"SYRIAN ARAB REPUBLIC",
"MS":"MONTSERRAT",
"GB":"UNITED KINGDOM",
"PM":"SAINT PIERRE AND MIQUELON",
"CL":"CHILE",
"MF":"SAINT MARTIN",
"SO":"SOMALIA",
"BJ":"BENIN",
"YE":"YEMEN",
"TV":"TUVALU",
"GE":"GEORGIA",
"BM":"BERMUDA",
"GS":"SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
"AN":"NETHERLANDS ANTILLES",
"BY":"BELARUS",
"FI":"FINLAND",
"BV":"BOUVET ISLAND",
"LR":"LIBERIA",
"KH":"CAMBODIA",
"LY":"LIBYAN ARAB JAMAHIRIYA",
"MU":"MAURITIUS",
"GU":"GUAM",
"ER":"ERITREA",
"LI":"LIECHTENSTEIN",
"SD":"SUDAN",
"PA":"PANAMA",
"IL":"ISRAEL",
"EH":"WESTERN SAHARA",
"KE":"KENYA",
"CC":"COCOS (KEELING) ISLANDS",
"IS":"ICELAND",
"GF":"FRENCH GUIANA",
"MM":"MYANMAR",
"HT":"HAITI",
"NF":"NORFOLK ISLAND",
"ML":"MALI",
"PY":"PARAGUAY",
"KZ":"KAZAKHSTAN",
"CH":"SWITZERLAND",
"BA":"BOSNIA AND HERZEGOVINA",
"BO":"BOLIVIA, PLURINATIONAL STATE OF",
"UA":"UKRAINE",
"BL":"SAINT BARTHELEMY",
"AZ":"AZERBAIJAN",
"BT":"BHUTAN",
"VA":"HOLY SEE (VATICAN CITY STATE)",
"PE":"PERU",
"AR":"ARGENTINA",
"TK":"TOKELAU",
"AG":"ANTIGUA AND BARBUDA",
"KN":"SAINT KITTS AND NEVIS",
"PS":"PALESTINIAN TERRITORY, OCCUPIED",
"ID":"INDONESIA",
"GW":"GUINEA-BISSAU",
"HN":"HONDURAS",
"NG":"NIGERIA",
"IQ":"IRAQ",
"JM":"JAMAICA",
"NU":"NIUE",
"ET":"ETHIOPIA",
"ME":"MONTENEGRO",
"SK":"SLOVAKIA",
"YT":"MAYOTTE"
}
lenght= [len(v) for v in COUNTRY.values()]
# print(lenght)
m= max(lenght)
# print(m)

lc= [c for c in COUNTRY.values() if len(c)==m]
print(lc)

# 9
# Consider the following two Python Lists that save information about company sales for the last 6 years:
years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]
new_list= list(zip(years, sales))
print(new_list)

# 10
# Create a new dictionary that has the keys, the years, and the values, the sales.
new_dict= dict(zip(years, sales))
print(new_dict)

# 11
# Consider the dictionary from the previous challenge.
# Create a new dictionary called profit that stores the profit of the company, if the profit margin is 25% of the sales.
# Use dictionary comprehension if possible.
profit= {k*0.25 for k in new_dict.values()}
# print(profit)
profit_dict= dict(zip(years, profit))
print(profit_dict)

# 12 Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].
# Create a set that contains the elements of the 2 lists in pairs.
# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}

names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]
new_set= set(zip(names,phones))
print(new_set)

# 13 Consider the two Python lists.
# Write a Python Script to make a new list whose elements are the intersection of the two given lists.
# This means all elements of L1 that also belong to L2, but no other elements.

l1=[1,2,3,4,4,5,3,5,6,6]
l2=[1,2,3,5,6,8,4]
inter= list(set(l1).intersection(set(l2)))
print(inter)
 # 14 Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".
# If the email is not valid the script should display why it's not valid.
# We consider a valid email address if:
# it has at least 6 characters but no more than 16.
# it contains both . and @
# it does not contain any of the following characters:'[]{}()$*'

not_permitted= '[]{}()$*'
permitted='.@'
while True:
    email = input('enter your email:')
    if len(email)<6 or len(email)>16:
        print('invalid email')
    elif not set(email).isdisjoint(set(not_permitted)):
        print('invalid symbol')
    elif set(email)& set(permitted)!= set(permitted):
        print('A character is missing, either . or @')
    else:
        print('Valid email')


