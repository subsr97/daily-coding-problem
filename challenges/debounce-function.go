/*
#105
Facebook

Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

*/

package main

import (
	"fmt"
	"time"
)

type fn func()

func foo() {
	fmt.Printf("%v: Hit the function.\n", time.Now().Local())
}

func Debouncer(function fn, timeout int) fn {
	lastAccessChannel := make(chan time.Time, 1)
	return func() {
		select {
		case lastAccessTime := <-lastAccessChannel:
			if time.Since(lastAccessTime) >= time.Duration(timeout)*time.Millisecond {
				go function()
				lastAccessChannel <- time.Now()
			} else {
				fmt.Printf("%v: Debounced.\n", time.Now().Local())
				lastAccessChannel <- lastAccessTime
			}
		default:
			go function()
			lastAccessChannel <- time.Now()
		}
	}
}

func main() {

	// No debounce
	for i := 0; i < 20; i++ {
		foo()
		time.Sleep(100 * time.Millisecond)
	}

	fmt.Println()
	debouncedFoo := Debouncer(foo, 300)

	// With debounce
	for i := 0; i < 20; i++ {
		debouncedFoo()
		time.Sleep(100 * time.Millisecond)
	}
}
