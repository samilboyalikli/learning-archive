from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, count

print("[MAIN] Starting spark session...")
try:
    spark = SparkSession.builder.appName("KafkaSparkStreaming").config("spark.sql.session.timeZone", "UTC").getOrCreate()
    print("[MAIN] Started spark session.")
except Exception as e:
    print(f"[MAIN] Occurred an Error: {e}")

print("[MAIN] Start reading kafka stream...")
try:
    kafka_df = spark.readStream.format("kafka") \
                .option("kafka.bootstrap.servers", "kafka:9092") \
                .option("subscribe", "raw_topic") \
                .option("startingOffsets", "latest") \
                .load()
    print("[MAIN] Started reading kafka stream.")
except Exception as e:
    print(f"An Error Occurred: {e}")

print("[MAIN] Parsing kafka dataframe...")
try: 
    parsed_df = kafka_df.selectExpr("CAST(value as STRING) as message", "timestamp")
    print("[MAIN] Parsed kafka dataframe.")
except Exception as e:
    print(f"An Error Occurred: {e}")

print("[MAIN] Counting kafka dataframe...")
try: 
    aggregated_df = parsed_df.groupBy(window(col("timestamp"), "10 seconds")).agg(count("*").alias("message_count"))
    print("[MAIN] Counted kafka dataframe.")
except Exception as e: print(f"An Error Occurred: {e}")

print("[MAIN] Query starting...")
try:
    query = aggregated_df.selectExpr("to_json(struct(*)) as value").writeStream.format("Kafka") \
                    .option("kafka.bootstrap.servers", "kafka:9092") \
                    .option("topic", "result_topic") \
                    .option("checkpointLocation", "/tmp/spark-checkpoints") \
                    .outputMode("update") \
                    .start()
    query.awaitTermination()
    print("[MAIN] Query started.")
except Exception as e:
    print(f"An Error Occurred: {e}")


# print("[MAIN] Query starting...")
# try:
#     query = aggregated_df.writeStream.outputMode("update") \
#             .format("console") \
#             .option("truncate", "false") \
#             .start()
#     query.awaitTermination()
#     print("[MAIN] Query started.")
# except Exception as e:
#     print(f"An Error Occurred: {e}")