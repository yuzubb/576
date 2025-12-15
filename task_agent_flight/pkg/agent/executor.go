package agent

import (
	"sync"
	"time"
	"math/rand"
)

type FlightSearchRequest struct {
	UserID string
	Origin string
	Destination string
	Date string
}

type FlightResult struct {
	Source string
	Price float64
	FlightNumber string
}

func searchExternalAPI(apiName string, req FlightSearchRequest, ch chan FlightResult, wg *sync.WaitGroup) {
	defer wg.Done()
	
	time.Sleep(time.Duration(rand.Intn(500)) * time.Millisecond)
	
	ch <- FlightResult{
		Source: apiName,
		Price:  rand.Float64() * 1000,
		FlightNumber: "FN" + apiName + "123",
	}
}

func ExecuteFlightSearch(req FlightSearchRequest) []FlightResult {
	apis := []string{"API_A", "API_B", "API_C", "API_D"}
	results := make(chan FlightResult, len(apis))
	var wg sync.WaitGroup

	for _, api := range apis {
		wg.Add(1)
		go searchExternalAPI(api, req, results, &wg)
	}

	wg.Wait()
	
	close(results)
	
	finalResults := make([]FlightResult, 0)
	for res := range results {
		finalResults = append(finalResults, res)
	}
	
	return finalResults
}
