# Databricks notebook source
jdbcHostname = "rennesshserverforpoc1.database.windows.net"  
jdbcDatabase = "employeedatabase"  
jdbcPort = "1433"  
username = "rennessh"  
password = "Devi1203@"  
jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2}".format(jdbcHostname, jdbcPort, jdbcDatabase)  
connectionProperties = {  
  "user" : username,  
  "password" : password,  
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"  
}  
pushdown_query = "(Select * from [SalesLT].[Customer] where CustomerID = 2) CustomerID"    
df = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=connectionProperties)  
display(df) 



# COMMAND ----------


