# azure_connection
Code showing how to connect with a azure sql database from your local machine. Note that, since that was a project delevoped for another company, I couldn't use the convencional way of connecting to the database using the password and the username, so I had to use a acess token.

## Commands for implementing local and cloud functions

To be able to implement the functions we need, first of all, to have access to the database that is in the Azure. The code deployed checks where it is running: locally or in the cloud. So to make it possible to run the code in the cloud, it is necessary to follow the steps below:

[Download the following: Download Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)

In Powershell, run the following commands:

Azure CLI login: 
`az login`

Generate access token (1 hour):
```
az account get-access-token --
resource=https://database.windows.net/ --query accessToken
```
The access code must be added as the db_token variable in the code, allowing access for 1 hour.

The implemented code is already functional for running in the cloud, requiring no adjustments.


**Installation support documentation**

[Structuring functions from scratch](https://www.youtube.com/watch?v=_Xr_SxDeub4)

[Install pyodbc](https://learn.microsoft.com/pt-br/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16)

[Install pyodbc drive](https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)

[How to connect to Azure SQL?](https://techcommunity.microsoft.com/t5/apps-on-azure-blog/how-to-connect-azure-sql-database-from-python-function-app-using/ba-p/3035595)
