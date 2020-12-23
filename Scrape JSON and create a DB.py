import json
import urllib.request, urllib.parse, urllib.error
import sqlite3
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://raw.githubusercontent.com/PeterNotenboom/SwiftCodes/master/AllCountries/GH.json'

connection = urllib.request.urlopen(url)
data = connection.read().decode()
headers = dict(connection.getheaders())
js = json.loads(data)
# print(json.dumps(js))

# print('branch')
#print('User count:', len(info))

for item in js['list']:
    bank = item['bank']
    # print(bank)
    city=item['city']
    branch=item['branch']
    swift=item['swift_code']
    # print(swift)
   # print(item['city'])
   # print(item['branch'])
   # print(item['swift_code'])
   
#Creating the New Database
conn = sqlite3.connect('macedonia.sqlite')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS SWIFT')

# cur.execute('''
# CREATE TABLE SWIFT (bank TEXT, city TEXT, branch TEXT, swift_code TEXT)''')


    
for item in js['list']:  
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO SWIFT (bank, city, branch, swift_code)
                VALUES (?,?,?,?)''', (bank, city, branch, swift))
    
#     cur.execute('SELECT bank FROM SWIFT WHERE bank = ? ', (bank,))
# row = cur.fetchone()

        # if row is None:
        #     cur.execute('''INSERT INTO SWIFT (bank, city, branch, swift_code)
        #         VALUES (?,?,?,? ''', (bank, city, branch, swift))

conn.commit()

