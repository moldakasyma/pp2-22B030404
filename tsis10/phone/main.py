import psycopg2, csv
from config import conn


config = psycopg2.connect(**conn) 
current = config.cursor()

#create table
create_table = '''
CREATE TABLE phonebook(
    name varchar(15),
    number varchar(15)
)
'''

#to upload inf
insert = '''
INSERT INTO phonebook VALUES (%s,%s);
'''
select = ''' 
SELECT * FROM phonebook; 
 
''' 
#to update information
update = '''
UPDATE phonebook SET number = %s WHERE name = %s;
'''
#to delete
delete = '''
DELETE FROM phonebook WHERE name = %s;
'''


print("Type '1' to create the table, '2' to insert data, '3' to update data, '4' to delete data")
num = int(input())

if num == 1:
    current.execute(create_table)
elif num == 2:
    name=input("Enter your name: ")
    Phone=input("Enter your number: ")    
    current.execute(insert, (name,Phone))
    
elif num == 3:
    phone=input("Enter your phone: ")
    name=input("Enter your name: ")
    current.execute(update,(phone,name))
    print("Successfully updated")
elif num == 4:
    name=input("Enter name: ")
    current.execute(delete,[name])
    print("successfully deleted")

with open('phone.csv','r') as f:
    reader = csv.reader(f,delimiter = ',')
    for row in reader:
        pass

current.execute(select)
# to recieve the data
v = current.fetchall() 
print(v) 

current.close() 
config.commit() 
config.close()
