import sqlite3

conn = sqlite3.connect('c:\python27\VisibleAlpha_Assignment\TestDB.db')
print "Opened database successfully";

conn.execute('select * from employee')
print "data fetched";
conn.close()
