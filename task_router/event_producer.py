import time
import json
from kafka import KafkaProducer

PRODUCER = KafkaProducer(bootstrap_servers=['kafka-broker:9092'], 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def route_task_to_agent(user_id: str, instruction: str):
    # action_type = LLM_Intention_Classifier.classify(instruction) 
    action_type = "FLIGHT_SEARCH" 

    event = {
        "user_id": user_id,
        "instruction": instruction,
        "action_type": action_type,
        "timestamp": time.time()
    }
    
    PRODUCER.send(f"task_queue_{action_type.lower()}", event)
    
    return {"status": "processing"}
