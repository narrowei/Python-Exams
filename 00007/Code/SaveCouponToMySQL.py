import mysql.connector
from mysql.connector import errorcode
import time
from datetime import date, datetime, timedelta
import uuid
'''
 this is a
 vary very
 long
 comment
'''

def create_Coupon(num):
  coupon_list = {}
  while len(coupon_list)<num:
    coupon_list[uuid.uuid4()] = 'coupon info'
  return coupon_list
#craete coupon table
def create_coupon_table(cursor):
  TABLES = {}
  TABLES['Coupon'] = (
    "CREATE TABLE `coupon` ("
    "  `coupon_no` varchar(50) NOT NULL,"
    "  `detail` varchar(50) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date DEFAULT NULL,"
    "  PRIMARY KEY (`coupon_no`)"
    ") ENGINE=InnoDB")
  for name, ddl in TABLES.iteritems():
    try:
      print("Creating table {}: ".format(name))
      cursor.execute(ddl)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
      else:
        print(err.msg)
    else:
      print("OK")
#insert
'''
 this is a
 vary very
 long
 comment
'''

def insert_coupons(coupons,cursor,cnx):
  tomorrow = datetime.now().date() + timedelta(days=1)
  now = datetime.now().date()
  for coupon_id in coupons:
    add_coupon = ("INSERT INTO coupon "
                  "(coupon_no, detail, from_date, to_date) "
                  "VALUES (%(coupon_no)s, %(detail)s, %(from_date)s, %(to_date)s)")
    data_salary = {
      'coupon_no': str(coupon_id),
      'detail': coupons[coupon_id],
      'from_date': now,
      'to_date': tomorrow,
    }
    cursor.execute(add_coupon, data_salary)
    cnx.commit()


config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}
#connect mysql
try:
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = cnx.cursor()
  create_coupon_table(cursor)
  coupons = create_Coupon(2000)
  insert_coupons(coupons, cursor, cnx)
  cursor.close()
  cnx.close()