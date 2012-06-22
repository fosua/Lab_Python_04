groceries = ['bananas', 'strawberries', 'apples', 'bread']
groceries.append('champagne')
for index in range (len(groceries)):
    print groceries[index]
print ''
groceries.remove('bread')
for index in groceries:
    print index
print ''
# c
food_aisle = {'bananas':'b', 'strawberries':'s', 'apples':'a', 'bread':'b'}
print food_aisle
print food_aisle['apples']
print ''
# answer to question 2a
# will use dictionaries because you need to pair every
#item and their price and when thier prices are changed you can change them

 # 2b
item_store = {'Apples':7.3, 'Bananas':5.5, 'Bread':1.0, 'Carrots':10.0, 'Champagne':20.90, 'Strawberries':32.6}
print item_store
item_store['Strawberries'] = 63.43
print item_store['Strawberries']
print ''
item_store['Chicken']= 6.5
print item_store
print ''
#3
#i will use  list because a list stores sequence of values
#b
in_stock = ['Apples', 'Bananas', 'Bread', 'Carrots', 'Champagne']
for names in in_stock:
    print names
print ''
#c tuples
always_in_stock = ('Apples', 'Bananas', 'Bread', 'Carrots', 'Champagne')
for names in always_in_stock:
    print names  
print ''
#d
print 'Come to shoprite! We always sell:'
for names in always_in_stock:
    print names
