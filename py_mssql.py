import pymssql

conn = pymssql.connect(host='192.168.1.115',
                       user='CCLASMGR',
                       password='CCLASMGR',
                       database='',
                       charset='gbk')
cursor = conn.cursor()
