#!/usr/bin/env python

import sys, ldap

# Set path name of file containing all CA certificates
# needed to validate server certificates
ldap.set_option(ldap.OPT_X_TLS_CACERTFILE,'/etc/openldap/cacerts/SNL_CA.pem')

# Create LDAPObject instance
l = ldap.initialize('ldaps://ldap.snl.salk.edu:636')
# Set LDAP protocol version used
l.protocol_version=ldap.VERSION3

# baseDN = "ou=Group,dc=snl,dc=salk,dc=edu"
baseDN = "dc=snl,dc=salk,dc=edu"
searchScope = ldap.SCOPE_SUBTREE

# searchFilter = "cn=cnl"
# searchFilter = "gidNumber=2016"
# searchFilter = "uidNumber=1175"
searchFilter = "uid=bryan"


ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
result_set = []

while 1:
   result_type, result_data = l.result(ldap_result_id, 0)
   if (result_data == []):
      print "No Results. \n"
      break
   # Or
   #if len(result_data) == 0:
   #   print "No Results."
   #   return
   else:
      ## here you don't have to append to a list
      ## you could do whatever you want with the individual entry
      ## The appending to list is just for illustration.
      #
      #if result_type == ldap.RES_SEARCH_ENTRY:
      #  result_set.append(result_data)
      #
      for i in range(len(result_data)):
         for entry in result_data[i]:
            name = entry[1]['cn'][0]
            email = entry[1]['mail'][0]
            phone = entry[1]['telephonenumber'][0]
            desc = entry[1]['description'][0]
            count = count + 1
            #print result_set
            print "%d.\nName: %s\nDescription: %s\nE-mail: %s\nPhone: %s\n" % (count, name, desc, email, phone)

# Close connection
l.unbind_s()