#!/bin/bash

clear

mkdir output/

g++ -Wall -o src/string-generator/RandomString src/string-generator/RandomString.cpp
g++ -Wall -o src/$1/$1 src/$1/$1.cpp

if [ "$?" == 0 ]; then
	for i in 1000 5000 10000 50000 100000 500000
	do
		for j in 100 500 1000
		do
			./src/string-generator/RandomString $i $j
			./src/$1/$1 "src/random_string.in" $i $j > src/trash
			echo $i-$j finished
		done
	done
fi

rm -r src/random_string.in src/trash src/string-generator/RandomString src/$1/$1 src/$1/$1.exe
