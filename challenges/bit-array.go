/*
#137
Amazon

A bit array is a space efficient array that holds a value of 1 or 0 at each index.
	- init(size): initialize the array with size
	- set(i, val): updates index at i with val where val is either 1 or 0
	- get(i): gets the value at index i

Solution reference: https://web.archive.org/web/20181015104504/http://www.mathcs.emory.edu/~cheung/Courses/255/Syllabus/1-C-intro/bit-array.html
*/
package main

import (
	"errors"
	"fmt"
	"math"
)

var (
	indexError = errors.New("Error: Index out of range.")
)

type BitArray struct {
	array []int32
	size  uint
}

func (bitArray *BitArray) init(neededSize uint) {
	implementationSize := int(math.Ceil(float64(neededSize) / 32.0))
	bitArray.array = make([]int32, implementationSize)
	bitArray.size = neededSize

	for index := 0; index < implementationSize; index++ {
		bitArray.array[index] = 0
	}
}

func (bitArray *BitArray) set(i, val uint) error {
	implementationIndex := uint(i / 32)
	if i >= bitArray.size {
		return indexError
	}

	var temp int32 = 1
	if val == 1 {
		temp = (temp << (i % 32))
		bitArray.array[implementationIndex] |= temp
	} else {
		temp = ^(temp << (i % 32))
		bitArray.array[implementationIndex] &= temp
	}

	return nil
}

func (bitArray BitArray) get(i uint) (int32, error) {
	implementationIndex := uint(i / 32)
	if i >= bitArray.size {
		return 0, indexError
	}

	var temp int32 = 1
	if bitArray.array[implementationIndex]&(temp<<i%32) != 0 {
		return 1, nil
	} else {
		return 0, nil
	}
}

func (bitArray *BitArray) print() {
	for _, val := range bitArray.array {
		op := fmt.Sprintf("%b", val)

		for len(op) != 32 {
			op = "0" + op
		}

		fmt.Print(op, " ")
	}
	fmt.Println()
}

func main() {
	var bitArray1 BitArray
	bitArray1.init(10)
	// 00000000000000000000000000000000

	bitArray1.set(0, 1)
	bitArray1.print()
	// 00000000000000000000000000000001

	bitArray1.set(1, 1)
	bitArray1.print()
	// 00000000000000000000000000000011

	bitArray1.set(2, 1)
	bitArray1.print()
	// 00000000000000000000000000000111

	bitArray1.set(1, 0)
	bitArray1.print()
	// 00000000000000000000000000000101

	if err := bitArray1.set(10, 1); err != nil {
		fmt.Println(err.Error())
	}
	// Error: Index out of range.

	var bitArray2 BitArray
	bitArray2.init(35)
	// 00000000000000000000000000000000 00000000000000000000000000000000

	if err := bitArray2.set(10, 1); err != nil {
		fmt.Println(err.Error())
	}
	bitArray2.print()
	// 00000000000000000000010000000000 00000000000000000000000000000000

	bitArray2.set(33, 1)
	bitArray2.print()
	// 00000000000000000000010000000000 00000000000000000000000000000010

	if err := bitArray2.set(35, 1); err != nil {
		fmt.Println(err.Error())
	}
	// Error: Index out of range.
}
