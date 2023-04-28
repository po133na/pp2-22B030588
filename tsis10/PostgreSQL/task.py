import psycopg2
import csv

conn = psycopg2.connect(
    database="PhoneBook",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

with open('contacts.csv', newline='') as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in read:
        print(', '.join(row))

#with open('eggs.csv', 'w', newline='') as csvfile:
#    write = csv.writer(csvfile, delimiter=' ',
 #                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
  #  write.writerow(['Spam'] * 5 + ['Baked Beans'])
   # write.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

cursor = conn.cursor()

try:
    name = input("enter name: ")
    surname = input("enter surname: ")
    phone = input("enter phone number: ")

    cursor.execute("INSERT INTO PhoneBook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))

    cursor.execute("SELECT * FROM PhoneBook")
    print(cursor.fetchall())
    cursor.execute("UPDATE PhoneBook SET phone = '+555555' WHERE name = 'Polina';")

    cursor.execute("SELECT id, name FROM PhoneBook")
    print(cursor.fetchall())

    cursor.execute("DELETE FROM PhoneBook WHERE name = 'Polina'")

except psycopg2.DatabaseError:
    conn.rollback()
finally:
    conn.commit()
    cursor.close()
    conn.close()