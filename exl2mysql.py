# -*- coding:utf-8 -*-

import xlrd
import MySQLdb

book = xlrd.open_workbook("/Users/yangzefeng/Downloads/净水品牌目录.xls")
sheet = book.sheet_by_name("Sheet1")

database = MySQLdb.connect(host="localhost",user="root",passwd="",db="rrs")

cursor = database.cursor()

query = "insert into brands (name, parent_id, description) values (%s, %s, %s)"

for r in range (1, sheet.nrows):
	name = sheet.cell(r,1).value
	parent_id = None
	description = ""

	values =  (name,parent_id,description)

	cursor.execute(query,values)

cursor.close()

database.commit()

database.close()

print ""
print "Done"
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
#print "imported " %s " columns and " %s " rows into mysql", columns, rows