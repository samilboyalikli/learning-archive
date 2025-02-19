#!/bin/bash

if [ "$SPARK_MODE" = "master" ]; then
  /opt/spark/bin/spark-class org.apache.spark.deploy.master.Master --host spark-master --port 7077 --webui-port 8080
else
  /opt/spark/bin/spark-class org.apache.spark.deploy.worker.Worker $SPARK_MASTER_URL
fi

tail -f /dev/null


#!/bin/bash
# 
# if [ "$SPARK_MODE" == "master" ]; then
#   /opt/spark/sbin/start-master.sh
# else
#   /opt/spark/sbin/start-worker.sh $SPARK_MASTER_URL
# fi
# 
# tail -f /dev/null