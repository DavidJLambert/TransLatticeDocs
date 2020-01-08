#*******************************************************************************
#
#                             TRANSLATTICE, INC.
#                           AUTOMATION KIT SAMPLE CODE
#                         Copyright 2012, TransLattice, Inc.
#
#
#       The TransLattice AK contains a variety of materials, including but not
#       limited to, interface definitions, documentation, and sample code
#       regarding automating interfaces to one or more TransLattice products.
#       This sample code is intended to serve as a guide for writing programs
#       to interact with the TransLattice Software.
#
#       You may download and make a reasonable number of copies of the AK
#       contents for your use solely for the purpose of creating
#       software that communicates with TransLattice Software. You agree to
#       defend, indemnify and hold harmless TransLattice, and any of its
#       directors, officers, employees, affiliates or agents, from and against
#       any and all claims, losses, damages, liabilities and other expenses
#       arising from your modification and distribution of the sample code.
#
#
#       You may modify and create derivative works of the sample code and
#       distribute the modified sample code provided the above copyright notice
#       is included with the derivative work.
#
#       You may not represent that the programs you develop using the AK are
#       certified or otherwise endorsed by TransLattice. You may not use the
#       TransLattice name or any other trademarks or service marks of
#       TransLattice in connection with programs that you develop using the AK.
#
#       For complete terms and conditions, refer to the end user license
#       agreement which accompanies TransLattice products.
#
#       For questions or concerns, please contact info@translattice.com
#
#*******************************************************************************
#

##### DEFINE PARAMETERS #####

CLUSTER_NAME = "Bluster"
NETMASK      = "255.255.254.0"
GATEWAY      = "172.16.32.1"
DNS_SERVER   = "172.16.33.11"

SEP1_NAME     = "SEP_NUMBER1"
SEP1_IP       = "172.16.33.213"
SEP1_NETMASK  = NETMASK

SEP2_NAME     = "SEP_NUMBER2"
SEP2_IP       = "172.16.33.66"
SEP2_NETMASK  = NETMASK

APP1_NAME    = "App1"
APP1_DB_NAME = "app1db"

SUPERUSER_USERNAME = "admin"
SUPERUSER_PASSWORD = "hello"
SUPERUSER_EMAIL    = "dlambert@translattice.com"

USER1_LOGIN         = "pguser"
USER1_PASSWORD      = "pguser"
USER1_CLUSTER_WRITE = True
USER1_DB_CONNECT    = True
USER1_DB_WRITE      = True
USER1_FULL_NAME     = "pguser1"
USER1_EMAIL         = "name1@company.com"
USER1_SMS           = "name2@company.com"

# The IP addresses of the nodes to be created.
NODE1_IP     = "172.16.32.148"
NODE2_IP     = "172.16.32.238"
NODE3_IP     = "172.16.32.34"

# The names being given to these nodes.
NODE1_NAME   = "Node148"
NODE2_NAME   = "Node238"
NODE3_NAME   = "Node34"

# Nodes' hexadecimal serial numbers. Digits a-f must be lower case.
NODE1_SERIAL = "000367013cb5"
NODE2_SERIAL = "000367013cb6"
NODE3_SERIAL = "000367013cb7"

NODE1_STATIC_IP = False
NODE2_STATIC_IP = False
NODE3_STATIC_IP = False

# These two automatically set when cluster created
POLICY_LEVEL1         = "root"
POLICY_LEVEL1_DOMAIN1 = CLUSTER_NAME

# The names of the policy level and policy domains being created.
# Only alpha-numeric characters, hyphens, and spaces are allowed.
POLICY_LEVEL2         = "Level2"
POLICY_LEVEL2_DOMAIN1 = "Level2-Domain1"
POLICY_LEVEL2_DOMAIN2 = "Level2-Domain2"
DOMAIN1_DICT          = { POLICY_LEVEL1_DOMAIN1 : POLICY_LEVEL2_DOMAIN1 }

CERTIFICATE_FILE_NAME = "valid1.pem"
CERTIFICATE_NAME      = "SampleCertificate"

REMOTE_CONNECTIONS    = True

DEBUG           = False
VERBOSITY_LEVEL = 3
TIME_OUT        = 600

##### DONE DEFINING PARAMETERS ####
