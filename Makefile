# This will compile the src/main.c file into a helloworld binary. This binary is the file we want!
compile:
	gcc src/main.c -o helloworld

run: compile
	./helloworld
