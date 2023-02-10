# Databricks notebook source
# MAGIC %python
# MAGIC import pyspark
# MAGIC from pyspark.sql import SparkSession

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://appledata1@firststoragerennessh.blob.core.windows.net",
  mount_point = "/mnt/appledatamount",
  extra_configs = {"fs.azure.account.key.firststoragerennessh.blob.core.windows.net":"3J/TU63SoWmqyd6lE2ZeUj4FrfW9h7+yC6QpUd9hMrc+Ran/XFrfYSdRHeS3hCEiegrvpWl2UQAs+ASt1sad4g=="})

# COMMAND ----------

# MAGIC %sql
# MAGIC --dbutils.fs.unmount("/mnt/appledatamount")

# COMMAND ----------

df=spark.read.csv("/mnt/appledatamount/AppleStore.csv",inferSchema=True,header=True)
df.display()

# COMMAND ----------


