
Provinciehoofdsteden = {
'Noord_Holland' : 'Amsterdam',
'Zuid_Holland' : 'Den_Haag',
'Utrecht' : 'Utrecht',
}



print(type(Provinciehoofdsteden))



Provinciehoofdsteden = {
'Noord_Holland' : 'Amsterdam',
'Zuid_Holland' : 'Den_Haag',
'Utrecht' : 'Utrecht',
}


for key, value in Provinciehoofdsteden.items():
    print(key, ':',value)

Provinciehoofdsteden = {
'Noord_Holland' : 'Amsterdam',
'Zuid_Holland' : 'Den_Haag',
'Utrecht' : 'Utrecht',
}

Provinciehoofdsteden['Zeeland'] = 'Middelburg'
Provinciehoofdsteden['Drenthe'] = 'Assen'
Provinciehoofdsteden['Overijssel'] = 'Zwolle'

for key, value in Provinciehoofdsteden.items():
    print(key, ':',value)




    Provinciehoofdsteden[1] = input('type haarlem')