package day9

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Height struct {
	Visited bool
	NumVal int
}

type Row struct {
	Values []Height
}

type HeightMap struct {
	Values []Row
}


func main() {
	f, err := os.Open("thermopylae.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {

		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

