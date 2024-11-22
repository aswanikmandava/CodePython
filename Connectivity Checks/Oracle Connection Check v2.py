import cx_Oracle

# Init
ORA_USER = 'sciencelogic_usr'
ORA_PWD = 'sc13nc3l0gicM0n'
ORA_HOST = 'dshr-prd-db.nycnet'
ORA_PORT = '1536'
ORA_SERVICE = 'dshrprd.nycnet'

dsn_tns = cx_Oracle.makedsn(ORA_HOST,ORA_PORT,service_name = ORA_SERVICE)

try:
    con = cx_Oracle.connect(ORA_USER, ORA_PWD,dsn_tns)
    print("Oracle Version: %s" %con.version)
    con.close()
except Exception as err:
    print(dsn_tns)
    print("Exception occurred: %s" %err)