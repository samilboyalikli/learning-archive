FROM openjdk:8-jdk-alpine

RUN apk add --no-cache bash python3 py3-pip

COPY . .

# RUN tar -xvzf /opt/spark-modules/spark-3.2.1-bin-hadoop3.2.tgz

RUN ln -s /opt/spark-modules/spark-3.2.1-bin-hadoop3.2 /opt/spark 

# RUN mv /opt/spark-modules/spark-3.2.1-bin-hadoop3.2 /opt/spark-3.2.1-bin-hadoop3.2

RUN pip3 install pyspark

RUN pip3 install kafka-python

# RUN spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 main.py

ENV PATH="/opt/spark/bin:${PATH}"

ENTRYPOINT ["/entrypoint.sh"]
