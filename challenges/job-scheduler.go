/*
#10
Apple

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

*/

package main

import (
	"fmt"
	"time"
)

type fn func()

var threadCount = 0

func job() {
	id := threadCount
	fmt.Println(time.Now())
	fmt.Println("Started ", id)
	time.Sleep(time.Duration(10) * time.Second)
	fmt.Println("Stopped", id)
}

func scheduler(f fn, duration int64) {
	for {
		go f()
		time.Sleep(time.Duration(duration) * time.Millisecond)
		threadCount++
	}
}

func main() {
	scheduler(job, 5000)
}
