
## In the following file there are 3 ways to connect to the azure database. ##
## The way that I recommend is to use the token (code of line 72 and so on) ##
#### if you don't have a user with all the azure permissions. ################


'''
Connecting to database using username and password
'''

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'put_your_server_name_here' 
database = 'put_your_database_name_here' 
username = 'put_your_username_here' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Authentication=ActiveDirectoryInteractive;ENCRYPT=yes')
cursor = cnxn.cursor()



'''
Connecting to database using username and password, but using a different aproach to define the connection string
'''

import textwrap
import pyodbc

# Specify the driver
driver = '{ODBC Driver 18 for SQL Server}'

# Specify the Server Name and Database Name
server_name = 'put_your_server_name_here'
database_name = 'put_your_database_name_here'

# Create our server URL
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

# Define username & password
username = "put_your_username_here"
password = "put_your_password_here"

# Create the full connection string
connection_string = textwrap.dedent('''
    Driver={driver};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
'''.format(
    driver=driver,
    server=server,
    database=database_name,
    username=username,
    password=password
))

# Create a new PYODBC Connection Object.
cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

# Create a new Cursor object from the connection
crsr: pyodbc.Cursor = cnxn.cursor()

#Close the connection once we are done

'''
Connecting to database using a token
'''

import logging
import azure.functions as func
import os
import pyodbc
import struct

def db_connect():
    server = 'put_your_server_name_here' 
    database = 'put_your_database_name_here' 
    db_token = 'put_the_generated_token_here'
    #condition to check if the code is running locally or in the cloud
    if os.getenv("MSI_SECRET"):
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Authentication=ActiveDirectoryMsi')
    else:
        SQL_COPT_SS_ACCESS_TOKEN = 1256
        
        exptoken = b''
        for i in bytes(db_token, "UTF-8"):
            exptoken += bytes({i})
            exptoken += bytes(1)

        tokenstruct = struct.pack("=i", len(exptoken)) + exptoken
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database, attrs_before = { SQL_COPT_SS_ACCESS_TOKEN:tokenstruct })

    return cnxn.cursor()
