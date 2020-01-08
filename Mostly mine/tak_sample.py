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
# File: TAK_sample.py
# TAK Version: 2.0
# Author: David Lambert
#
# This file, TAK_sample.py, contains sample Jython code that
# calls TAK methods (I mean "methods" as used in object oriented terminology).
#
# A second file, nodeinfo.py, is called by TAK_sample.py.
# It contains parameters used by TAK_sample.py.
#
#########
#########UPDATE THIS!!!!
#########
# There are several TAK methods described in "TAK User Guide" that do not work:
#   1. add_certificate
#   2. delete_certificate
#   3. configure_system_time
#   4. modify_user
#   5. delete_sep
# Sample code for these five methods is included, but none of it is executed.
#
# Here are the instructions for using this sample code (yes, it works!).
#   1. Install TAK 1.0 as described in the "TAK User Guide".
#   2. Install Translattice software on three computers.  These sample scripts
#      will create a three-node cluster with these three computers.
#   3. Reserve a static IP address for use as the IP Address of a SEP.
#   4. Edit the parameters in nodeinfo.py to match the configuration of the
#      cluster to be created.
#   5. Execute "TAK TAK_sample.py" on the Windows Command line.
#
# Note that some methods may take awhile to finish executing.  These two can
# take several minutes to complete:
#   1. create_cluster
#   2. add_node
#
# I recommend reading the comments in this code.  They are designed to be
# educational, and they include some comments that did not make it into the
# "TAK User Guide".
#
#################################################################

print( "\n## Starting Execution of TAK_sample.py. ##\n" )

#################################################################

# Get TransLattice classes & functions for working with nodes.

OPERATION = "Importing ak.py"

print( "\n## %s started. ##\n" % OPERATION )
try:
  import ak
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

print( "\n## ak version: %s ##\n" % ak.VERSION )

#################################################################

# Get Python classes and functions.

OPERATION = "Importing sys"

print( "\n## %s started. ##\n" % OPERATION )
try:
  import sys
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Get the parameters describing the cluster we're building.

OPERATION = "Importing nodeinfo.py"

print( "\n## %s started. ##\n" % OPERATION )
try:
  from nodeinfo import *
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Connect to and get handle (object "kit") of a node.
# All operations on this cluster must reference "kit".
# Use "https". "Http" will fail.

OPERATION = "Connecting to host of Node 1"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit = ak.connect( "https://" + NODE1_IP )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Set log verbosity. The allowed values are:
#   0 = silent
#   1 = show only action results
#   2 = also show action plans
#   3 = also show debug messages (default)
#   4 = show everything
#
# Default verbosity is designed for normal running. Used only
# to debug under the direction of TransLattice tech support.

if DEBUG:
  OPERATION = "Setting verbosity level"

  print( "\n## %s started. ##\n" % OPERATION )
  try:
    kit.set_verbosity( VERBOSITY_LEVEL )
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Get log verbosity. See comments above for setting verbosity.
# This is a read-only operation, so kit.commit() not invoked.

OPERATION = "Getting verbosity level"

print( "\n## %s started. ##\n" % OPERATION )
try:
  verbosity = kit.get_verbosity()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## The verbosity is %s ##\n" % str(verbosity) )

#################################################################

# Create a cluster.

# When a cluster is created, behind the scenes:
#   The superuser (login "admin") is created, given password
#     SUPERUSER_PASSWORD and email address SUPERUSER_EMAIL.
#   Policy level 1, named "root", is created.
#   Policy domain CLUSTER_NAME is created for policy level 1.
#   The first node, NODE1_NAME, is created, given IP address
#     NODE1_IP, and assigned to policy domain CLUSTER_NAME.
#     All of its disks are automatically detected.
#   The SEP named SEP_NAME is created with IP address SEP_IP
#     and netmask SEP_NETMASK.
#   Policy level 2, named "nodes", is created without policy
#     domains.
#   Policy level 3, named "disks", is created without policy
#     domains.
#   Later, when another policy level is created, all policy
#     levels above it (including "nodes" and "disks") have 1
#     added to their level number.

OPERATION = "Creating Cluster"

print( "\n## %s started. ##\n" % OPERATION )
print( "\n## This may take several minutes to finish. ##\n" )

try:
  if NODE1_STATIC_IP:
    kit.create_cluster(   CLUSTER_NAME,    NODE1_NAME,
      SUPERUSER_PASSWORD, SUPERUSER_EMAIL, NODE1_IP,
      NETMASK,            GATEWAY,         DNS_SERVER,
      SEP1_NAME,          SEP1_IP,         SEP1_NETMASK )
  else:
    kit.create_cluster(   CLUSTER_NAME,    NODE1_NAME,
      SUPERUSER_PASSWORD, SUPERUSER_EMAIL, None,
      None,               None,            None,
      SEP1_NAME,          SEP1_IP,         SEP1_NETMASK )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################


# Add Policy Level 2 and its first Domain.

# Creating a new policy level also creates its 1st policy
#   domain and adds 1 to the policy level numbers of all policy
#   levels above it.
# If this new policy level is the highest policy level below
#   the "nodes" policy level, all nodes automatically assigned
#   this policy level's new policy domain.
# Must name new policy domain & its parent policy domain in a
#   Dictionary object { PARENT_DOMAIN_NAME : NEW_DOMAIN_NAME }.

OPERATION = "Adding Policy Level 2 and its first Domain"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_level( POLICY_LEVEL2, 2, DOMAIN1_DICT )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add 2nd domain to Policy Level 2. When doing this, all
#   existing nodes remain in this level's 1st domain.

OPERATION = "Adding 2nd Domain to Policy Level 2"
print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_child_domain( POLICY_LEVEL1_DOMAIN1,
                        POLICY_LEVEL2_DOMAIN2 )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add 2nd node.

# When a node is added, its disks are automatically detected.

OPERATION = "Adding Node 2"

print( "\n## %s started. ##\n" % OPERATION )
print( "\n## This may take several minutes to finish. ##\n" )
try:
  if NODE2_STATIC_IP:
    kit.add_node(   POLICY_LEVEL2_DOMAIN1, NODE2_NAME,
      NODE2_SERIAL, NODE2_IP,              NODE2_IP,
      NETMASK,      GATEWAY,               DNS_SERVER,
      TIME_OUT )
  else:
    kit.add_node(   POLICY_LEVEL2_DOMAIN1, NODE2_NAME,
      NODE2_SERIAL, NODE2_IP,              None,
      None,         None,                  None,
      TIME_OUT )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################

# Add node number 3.

# When a node is added, its disks are automatically detected.

OPERATION = "Adding Node 3"

print( "\n## %s started. ##\n" % OPERATION )
print( "\n## This may take several minutes to finish. ##\n" )
try:
  if NODE3_STATIC_IP:
    kit.add_node(   POLICY_LEVEL2_DOMAIN1, NODE3_NAME,
      NODE3_SERIAL, NODE3_IP,              NODE3_IP,
      NETMASK,      GATEWAY,               DNS_SERVER,
      TIME_OUT )
  else:
    kit.add_node(   POLICY_LEVEL2_DOMAIN1, NODE3_NAME,
      NODE3_SERIAL, NODE3_IP,              None,
      None,         None,                  None,
      TIME_OUT )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Move Node from POLICY_LEVEL2_DOMAIN1 to POLICY_LEVEL2_DOMAIN2.

OPERATION = "Moving a Node to Another Domain"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.move_node( NODE3_NAME, POLICY_LEVEL2_DOMAIN2 )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

OPERATION = "Rename Node 3"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.rename_element( NODE3_NAME, NODE3_NAME )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

OPERATION = "Rename POLICY_LEVEL2_DOMAIN1"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.rename_element( POLICY_LEVEL2_DOMAIN1,
                      POLICY_LEVEL2_DOMAIN1 )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

OPERATION = "Rename Cluster"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.rename_element( CLUSTER_NAME, CLUSTER_NAME )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

OPERATION = "Add 2nd SEP"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_sep( SEP2_NAME, SEP2_IP, SEP2_NETMASK )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################

OPERATION = "Delete 2nd SEP"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.delete_sep( SEP2_NAME )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add a new user.
# Boolean arguments: USER2_ADMIN_CLUSTER, USER2_ADMIN_APP,
#   USER2_ADMIN_DB,  USER2_ADMIN_POLICY,  USER2_READ_ONLY.
# All other arguments are strings.
# Each user's full name must be unique.

OPERATION = "Add a new User"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_user(          USER2_LOGIN,     USER2_PASSWORD,
    USER2_ADMIN_CLUSTER, USER2_ADMIN_APP, USER2_ADMIN_DB,
    USER2_ADMIN_POLICY,  USER2_READ_ONLY, USER2_FULL_NAME,
    USER2_EMAIL,         USER2_SMS )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add another new user.

OPERATION = "Add a new User"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_user(          USER3_LOGIN,     USER3_PASSWORD,
    USER3_ADMIN_CLUSTER, USER3_ADMIN_APP, USER3_ADMIN_DB,
    USER3_ADMIN_POLICY,  USER3_READ_ONLY, USER3_FULL_NAME,
    USER3_EMAIL,         USER3_SMS )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Modify a User.

# The first argument is the user's full name, which is a unique
#   identifier, and can not be changed.  The other arguments
#   are the other arguments of add_user, in the same order.  If
#   an argument is not changing, set it to None.

OPERATION = "Modifying a User"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.modify_user(  USER3_FULL_NAME,     USER3_LOGIN,
    USER3_PASSWORD, USER3_ADMIN_CLUSTER, USER3_ADMIN_APP,
    USER3_ADMIN_DB, USER3_ADMIN_POLICY,  USER3_READ_ONLY,
    USER3_EMAIL,    USER3_SMS )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Delete a user.

OPERATION = "Delete a User"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.delete_user( USER3_LOGIN )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################

# Configure System Time

# Argument 1: name of node to make change on,
#             or None for the cluster default
# Argument 2: Use NTPD?     True = On, False = Off,
#             None to use the cluster default
# Argument 3: Use NTPDATE?  True = On, False = Off,
#             None to use the cluster default
# Argument 4: If argument 3 = True, string[4] list of up to 4
#             servers for NTPDATE, otherwise None

  OPERATION = "Configuring System Time"

  print( "\n## %s started. ##\n" % OPERATION )
  try:
    kit.configure_system_time( NODE3_NAME,  Use_NTPD,
                               Use_NTPDATE, NTPDATE_SERVERS )
    kit.commit()
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add Application.

# Uploading an application through "add_application" is
#   currently unsupported.
# Can still use this method to create an application with no
#   code and an empty database.
#
# Here, the application database name must be specified. This
#   is different from the Administrative Interface, where the
#   database name is optional, and if the database name field
#   is left blank, the database name is set to
#   "appdb<application ID>".
# Database names must contain only lower-case letters, digits,
#   spaces, and underscores.

OPERATION = "Adding an Application to the Cluster"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_application( APP1_NAME, APP1_DB_NAME, APP1_FILES )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Enable or Disable Remote Connections to the Cluster"

# The argument is boolean.

OPERATION = "Enable or Disable Remote Connections to Cluster"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.configure_remote_connections( REMOTE_CONNECTIONS_ENABLED )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add Certificate to a Node

# A certificate name must be unique accross all nodes.

OPERATION = "Add Certificate To a Node"

FILE_OBJ      = open( CERT_FILE_NAME,"r",-1)
CERT_CONTENTS = FILE_OBJ.read(-1)

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_certificate( NODE2_NAME,   NODE2_NAME + CERT_NAME,
                       CERT_CONTENTS )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Add Certificate to another Node

OPERATION = "Add Certificate To a Node"

FILE_OBJ      = open( CERT_FILE_NAME,"r",-1)
CERT_CONTENTS = FILE_OBJ.read(-1)

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_certificate( NODE3_NAME,   NODE3_NAME + CERT_NAME,
                       CERT_CONTENTS )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

#  Delete Certificate from a node.

OPERATION = "Delete Certificate"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.delete_certificate( NODE3_NAME + CERT_NAME )
  kit.commit()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################

OPERATION = "Add policy template"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_policy_template( POLICY_TEMPLATE_NAME )
  kit.commit_policy()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################

OPERATION = "Adding locating policy"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_locating_policy( POLICY_TEMPLATE_NAME, "=", 2, POLICY_LEVEL2_DOMAIN2 )
  kit.commit_policy()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################

OPERATION = "Adding redundancy policy"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.add_redundancy_policy( POLICY_TEMPLATE_NAME, "disks", 3 )
  kit.commit_policy()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################
########
######## NEW
########
######## NEED TO DEFINE POLICY_OBJECTS

OPERATION = "Applying policy template to application "

if True:
  print( "\n## %s started. ##\n" % OPERATION )
  try:
    kit.apply_application_policy( APP1_NAME, POLICY_TEMPLATE_NAME, POLICY_OBJECTS )
    kit.commit_policy()
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

# Output: "Connected? True"

OPERATION = "Determining If TAK Can Connect to Cluster"

# Returns Boolean value
print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.IsConnected()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## Connected? %s ##\n" % str(result) )

#################################################################

# Get the current URI used for webui connection.
# Output: "Base URI: https://12.34.56.71", for example.

OPERATION = "Get Cluster's Base URI"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetBaseUri()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## BaseUIR: %s ##\n" % str(result) )

#################################################################

# Output: "Cluster Root Name: Bluster" in this example.

OPERATION = "Get Cluster Root Name"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetClusterRootName()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## Cluster Root Name: %s ##\n" % str(result) )

#################################################################

# Return number of levels in cluster topology.
# Output: "Number of levels: 3" in this example.  Actually,
#   in this example, there is a hidden 4th level for disks.

OPERATION = "Counting Number of Levels in Cluster"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.CountLevels()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## Number of levels: %s ##\n" % str(result) )

#################################################################

# Argument = level number minus one. Note extra level of disks.
# Output, in this example:
#   "Name level 1: {u'uiAttrib': {}, u'name': u'root'}"
#   "Name level 2: {u'uiAttrib': {}, u'name': u'Policy Level 2'}"
#   "Name level 3: {u'uiAttrib': {}, u'name': u'nodes'}"
#   "Name level 4: {u'uiAttrib': {}, u'name': u'disks'}"
#   "Name level 5: None"

OPERATION = "Getting the Level Name For a Given Level Number"

print( "\n## %s started. ##\n" % OPERATION )

for LEVEL in range(0,5):
  try:
    result = kit.GetLevelName( LEVEL )
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )
  print( "\n## Name level %d: %s ##\n" % (LEVEL+1, result) )

#################################################################

# Return level number of given level name; None if not found.
# Output in this example ("disks" level is hidden):
#   "Level Number: 0"
#   "Level Number: 1"
#   "Level Number: 2"
#   "Level Number: 3"
#   "Level Number: None"

OPERATION = "Getting Level Number Given Level Name"

print( "\n## %s started. ##\n" % OPERATION )
for LEVEL in [ POLICY_LEVEL1, POLICY_LEVEL2, 'nodes', 'disks', 'invalid']:
  try:
    result = kit.GetLevelId( LEVEL )
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )
  print( "\n## Level Number: %s ##\n" % str(result) )

#################################################################

# Argument is level number minus one, output is a Unicode list.
# Output for this example:
#   "Level 1: [u'Bluster']"
#   "Level 2: [u'Policy Level 2-Domain 2', u'Policy Level 2-Domain 1]"
#   "Level 3: []"
#   "Level 4: []"

OPERATION = "Get the Cluster Elements At a Topology Level"

print( "\n## %s started. ##\n" % OPERATION )
for LEVEL in range(0,4):
  try:
    result = kit.GetElementsAtLevel( LEVEL )
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )
  print( "\n## Level %d: %s ##\n" % (LEVEL+1, result) )

#################################################################

# Return list of all login names as list of Unicode strings.
# Output: "Cluster Login Names: [u'pguser', u'admin']" in this example.

OPERATION = "Get List of All User Login Names"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetAllUsers()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## Cluster Login Names: %s ##\n" % str(result) )

#################################################################

# Fetch all Users and each of their properties.

OPERATION = "Fetch List of Users"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.FetchUserlist()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## Users on this cluster: %s ##\n" % str(result) )

## Here's the output for this example, with carriage returns,
##   indenting, spaces, and comments added to make it easier to read.
## This output is in Unicode format, so all strings are enclosed
##   in single-quotes and preceded by "u".
## This is two Python Dictionary (abbreviation: Dict) objects
##   enclosed inside a third, outer, Dictionary object.
#
#{ 8533:                          # Start outer Dict object
#  { u'role': 15,                 # Start 1st inner Dict object
#    u'userId': 8533,
#    u'smsEmail': u'name2@company.com',
#    u'smsNotifications': u'000000',
#    u'login': u'pguser',
#    u'emailNotifications':u'000000',
#    u'password': u'39c71989ada5f22d7865885eadc5dc46ccc0d1799819',
#    u'name': u'pguser1',
#    u'email': u'name1@company.com'
#  },                             # End 1st inner Dict object
#  1000:
#  { u'role': 15, # Start 2nd inner Dict object
#    u'userId': 1000,
#    u'login': u'admin',
#    u'password': u'7110e25b46fa1d8eaa0c11f44e02e5c0936a19ad0976',
#    u'name': u'Default Administrator',
#    u'email': u'default_admin@company.com'
#  }                              # End 2nd inner Dict object
#} # End outer Dict object
#
## Each Dict object is a comma-deliminated list of key:value
##   pairs. For the inner objects, the key describes the data
##   type of the value. For the outer object, the key is a
##   unique user id, while the value is a Dict object describing
##   all of the characteristics of that user.
#
#################################################################

# Get user id associated with user login.
# Output "User ID: 8533", for example.

OPERATION = "Getting User's ID Given User's Login Name"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetUidOfLogin( USER1_LOGIN )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print(" \n## User ID: %s ##\n" % str(result) )

USER_ID = result

#################################################################

# Get user id associated with user's full name (first match).
# Output "User ID: 8533", for example.

OPERATION = "Getting User's ID Given User's Full Name"
print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetUidOfFullname( USER1_FULL_NAME )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## User ID: %s ##\n" % str(result) )

#################################################################

# Get user's login name given their user id.
# Output "User's Login: pguser", in this example.

if True:
  OPERATION = "Getting User's Login Name Given User's ID"

  print( "\n## %s started. ##\n" % OPERATION )
  try:
    result = kit.GetLoginOfId( USER_ID )
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )
  print( "\n## User's Login: %s ##\n" % str(result) )

#################################################################

OPERATION = "Getting User's Full Name Given User's ID"

# Get user's full name given their user id.
# Output "User's Full Name: pguser1", in this example.

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetFullnameOfId( USER_ID )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## User's Full Name: %s ##\n" % str(result) )

#################################################################

# Return full name of user given login; None if not found.
# Output "User's Full Name: pguser1" in this example.

OPERATION = "Getting User's Full Name From Their Login Name"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetFullnameOfLogin( USER1_LOGIN )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## User's Full Name: %s ##\n" % str(result) )

#################################################################

# Return login name give user's full name; None if not found.
# Output "User's Login: pguser" in this example.

OPERATION = "Getting User's Login Name Given User's Full Name"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetLoginOfFullname( USER1_FULL_NAME )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\n## User's Login: %s ##\n" % str(result) )

##################################################################

# Return list of all node names in cluster topology, in
#   Unicode format.
# Output "List of all nodes: [u"Node71",u"Node72",u"Node73"]",
#   for example.

OPERATION = "Getting list of Nodes"

print( "\n## %s started. ##\n" % OPERATION )
try:
  result = kit.GetAllNodes()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )
print( "\nList of all nodes:\n%s\n" % str(result) )

##################################################################
###########
########### NEW
###########

OPERATION = "Printing Alerts"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.PrintAllAlerts( sys.stdout )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )


##################################################################
###########
########### NEW
###########

OPERATION = "List Policy Templates"

print( "\n## %s started. ##\n" % OPERATION )
try:
  kit.list_policy_templates()
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################
###########
########### NEW
########### NOT IMPLEMENTED

OPERATION = "Get policies for app"

if True:
  print( "\n## %s started. ##\n" % OPERATION )
  try:
    kit.get_app_policy( APP1_NAME )
  except ak.PyAkException, e:
    print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
    raise
  print( "\n## %s succeeded. ##\n" % OPERATION )

##################################################################
###########
########### NEW
########### name 'DbConfig' is not defined

OPERATION = "Get db config keys"

print( "\n## %s started. ##\n" % OPERATION )
try:
  dbConfig = DbConfig(kit)
  for elem in dbConfig.keys:
    print( elem )
except ak.PyAkException, e:
  print( "\n## %s failed: %s ##\n" % ( OPERATION, e ) )
  raise
print( "\n## %s succeeded. ##\n" % OPERATION )

#################################################################

print( "\n## Ending Execution of TAK_sample.py. ##\n" )

#################################################################
