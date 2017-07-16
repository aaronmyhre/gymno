import time, random, datetime, json # Standard
from kafka import KafkaProducer
from Falcon_SDK import FalconSDK  as FDK

# Params
topic = "test4"
server='localhost:9092'

# Kafka
producer = KafkaProducer(bootstrap_servers=server,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8')
                         )
# Query
queryParams = {'identifier_type': 'assets',
                'identifiers':'bitcoin',
                'categories': 'mp',
                'time_filter': 'd1',
                }

while True:
    # Get stories from Falcon
    stories = fdk.stories(queryParams)

    for s in stories.stories:
        print(s)

    # Send to producer
    #producer.send(topic, order)

    # Sleep
    #time.sleep(10)

    # debug
    Break()
