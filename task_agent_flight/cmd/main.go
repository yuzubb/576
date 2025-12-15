package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"github.com/confluentinc/confluent-kafka-go/kafka"
	"github.com/ukc/task_agent_flight/pkg/agent"
	"encoding/json"
)

func main() {
	topic := os.Getenv("KAFKA_TOPIC")
	if topic == "" {
		topic = "task_queue_flight_search"
	}

	consumer, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": "kafka-broker:9092", 
		"group.id":          "flight-agents-group",
		"auto.offset.reset": "earliest",
	})

	if err != nil {
		panic(err)
	}

	err = consumer.SubscribeTopics([]string{topic}, nil)
	if err != nil {
		panic(err)
	}

	sigchan := make(chan os.Signal, 1)
	signal.Notify(sigchan, syscall.SIGINT, syscall.SIGTERM)

	run := true
	for run == true {
		select {
		case sig := <-sigchan:
			fmt.Printf("Caught signal %v: terminating\n", sig)
			run = false
		default:
			msg, err := consumer.ReadMessage(time.Second)
			if err == nil {
				var req agent.FlightSearchRequest
				json.Unmarshal(msg.Value, &req)
				
				fmt.Printf("Received Task: %v\n", req.UserID)
				results := agent.ExecuteFlightSearch(req)
				fmt.Printf("Task Completed. Results count: %d\n", len(results))
				
			} else if !err.(kafka.Error).IsTimeout() {
				fmt.Printf("Consumer error: %v (%v)\n", err, msg)
			}
		}
	}

	consumer.Close()
}
