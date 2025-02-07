To run kafka connect with specific configurations

1. run docker-compose-2.yaml to start docker containers if you want vanilla apache kafka image used 
This vanila image uses custom entry point for the apache/kafka image to start kafka connect with the required configurations
2. run docker-compose.yaml to start docker containers if you want to use confluent image
3. run the following commands to create a connector with the required configurations

```shell
curl http://localhost:8083
{"version":"3.7.0","commit":"2ae524ed625438c5","kafka_cluster_id":"Some(5L6g3nShT-eMCtK--X86sw)"}%

curl -X POST -H "Content-Type: application/json" --data @s3-sink-config.json http://localhost:8083/connectors
{"name":"s3-sink-connector","config":{"connector.class":"io.confluent.connect.s3.S3SinkConnector","behavior.on.null.values":"IGNORE","topics.dir":"eventbus_logs","partition.field.format.path":"true","tasks.max":"3","s3.part.size":"5242880","timezone":"UTC","locale":"US","value.converter.schemas.enable":"false","format.class":"io.confluent.connect.s3.format.json.JsonFormat","key.converter":"org.apache.kafka.connect.storage.StringConverter","value.converter":"org.apache.kafka.connect.json.JsonConverter","errors.log.enable":"true","s3.bucket.name":"turo-vendors-dropbox","partition.duration.ms":"86400000","file.delim":".","topics":"test-topic","partition.field.name":"eventName","value.converter.region":"us-east-1","s3.compression.type":"gzip","aws.region":"us-east-1","partitioner.class":"com.canelmas.kafka.connect.FieldAndTimeBasedPartitioner","errors.tolerance":"all","storage.class":"io.confluent.connect.s3.storage.S3Storage","path.format":"'year'=YYYY/'month'=MM/'day'=dd","aws.access.key.id":"test","aws.secret.access.key":"test","store.url":"http://localstack:4566","s3.region":"us-east-1","flush.size":"50000","rotate.interval.ms":"300000","rotate.schedule.interval.ms":"-1","timestamp.extractor":"RecordField","timestamp.field":"payloadTimestamp","log4j.logger.org.apache.kafka.connect.runtime":"DEBUG","log4j.logger.io.confluent.connect.s3":"DEBUG","log4j.logger.com.amazonaws":"DEBUG","name":"s3-sink-connector"},"tasks":[],"type":"sink"}%
```

The second command creates the s3 sink connector with the necessary configuration based on the config file s3-sink-config.json
