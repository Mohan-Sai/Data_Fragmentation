import cx_Oracle
import pymysql
cx_Oracle.init_oracle_client(lib_dir=r"D:\Downloads\instantclient-basic-nt-19.9.0.0.0dbru\instantclient_19_9")



dsn = cx_Oracle.makedsn("localhost", 1521, service_name="XE")
conn = cx_Oracle.connect("SYS","admin", dsn, cx_Oracle.SYSDBA, encoding="UTF-8")
print(conn)

# Open MYSQL connection
mySqlCon = pymysql.connect(host='148.66.138.171',user='devgamingstaan',password='@Hani8655',database='GamingStaan')

print(mySqlCon)

