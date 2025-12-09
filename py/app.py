import time as t

def runCalculations(start):
	for i in range(int(1e9)):
		x = 2*i
		if i != 0 and i % int(1e7) == 0:
			 printTimePassed(start)

def printTimePassed(start):
	print("Time passed:", t.time() - start)

def main():
	print("Running Benchmark...please wait")
	start = t.time()
	runCalculations(start)
	printTimePassed(start)

if __name__ == "__main__": main()
