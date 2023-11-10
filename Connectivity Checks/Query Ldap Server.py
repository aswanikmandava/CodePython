# Check connectivity to LDAP service on domain controller by querying itself
import ldap
import base64
import time

ldap_server = '10.152.107.115'
ldap_port = 389
ldap_timeout = 3 # seconds
bind_user = 'CN=svc-ScienceLogic,CN=CSC Services,DC=csc,DC=nycnet'
bind_pwd = base64.b64decode('RiFyczVCMTAwZCNTYw==')
baseDN = "DC=csc,DC=nycnet"
searchScope = ldap.SCOPE_SUBTREE
searchFilter = "sAMAccountName=svc-ScienceLogic"
retrieveAttributes = ['userPrincipalName','cn']
# Uncomment below line to retrieve all attributes
# retrieveAttributes = None

# start timer
start_time = time.time()
try:
    print("Initializing LDAP connection ...")
    l = ldap.initialize('ldap://' + ldap_server + ':' + str(ldap_port))
    # Turn off anonymous bind
    l.set_option(ldap.OPT_REFERRALS, 0)
    # Set initial connect timeout
    l.set_option(ldap.OPT_NETWORK_TIMEOUT, ldap_timeout)
    # Set Ldap operation timeout
    l.set_option(ldap.OPT_TIMEOUT, ldap_timeout)
    print("Binding to LDAP server: %s" %ldap_server)
    l.simple_bind_s(bind_user,bind_pwd)
    bind_time = time.time() - start_time
    print("Connection successful !!!")
    try:
        print("Performing a search using filter: %s" %searchFilter)
        result = l.search_s(baseDN, searchScope, searchFilter, retrieveAttributes)
        print("SEARCH RESULT:")
        print(result)
        print("Closing connection...")
        l.unbind_s()
        print("Closed connection !!!")
    except ldap.LDAPError, e:
        print("Error: %s" %e)

    # end timer
    end_time = time.time()
    res_time = (end_time - start_time)
    print("Response time: %.3f sec" %res_time)
except ldap.LDAPError, e:
    print("Connection Error: %s" %e)