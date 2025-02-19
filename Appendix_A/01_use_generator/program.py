import time

def NumberGenerator():
	i = 0
	while True:
		yield i
		i += 1
		time.sleep(1)
		

if __name__ == "__main__":

    gen = NumberGenerator()

    for i in gen:
        print(i)