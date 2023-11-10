import cx_Oracle

# Init
ORA_USER = 'sciencelogic_usr'
ORA_PWD = 'sc13nc3l0gicM0n'
ORA_HOST = 'dshr-prd-db.nycnet'
ORA_PORT = '1536'
ORA_SERVICE = 'dshrprd.nycnet'

try:
    con = cx_Oracle.connect("%s/%s@%s:%s/%s" %(ORA_USER, ORA_PWD, ORA_HOST, ORA_PORT, ORA_SERVICE))
    print("Oracle Version: %s" %con.version)
    con.close()
except Exception, err:
    print("Exception occurred: %s" %err)


