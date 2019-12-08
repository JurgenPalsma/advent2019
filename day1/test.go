package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var fuel int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		fuel = fuel + ((num / 3) - 2)
	}

	fmt.Println(fuel)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
