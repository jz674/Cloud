import random
import threading 

class Foo: #how to initialize to 0?
    def __init__(self, i):
        self.i = i 

    def bump(x):
        self.i = self.i + x

bar = Foo(0)
lock = threading.Lock()

def main():
    for i in range(16):
        program(i)

if if __name__ == "__main__":
    main()

def program(t):
    count = 0
    while count < t: #how to spawn t threads?
        #make a thread
        count += 1
        t1 = threading.Thread(target=target) 
        t1.start()
        t1.join()
    print("The final value of bar is"+ bar.i)
    

def target():
    step = random.randint(0,1000)
    for i in range(1000000):
        lock.acquire()
        bar.bump(step)
        lock.release()
# # Now add an argument to your main procedure that will be an integer value, t. Your main
# # procedure will spawn t threads that each will do the following:
# # 1. Create an integer variable (not an object) step to hold a 64 bit integer, and initialize it
# # to a random value in the range 0..1000. Each thread will pick its own random value.
# # Use a method that yields “uniformly random” values (you won’t need to code this
# # yourself). Hint: is the random number generator thread-safe? How can you find out?


# # 2. Loop 1 million times, calling bump on the shared bar variable, passing the random step.
# # Hint: Don’t forget that bump requires an object as its argument: you will need to box
# # the random number. We need bump to be thread-safe: Is a lock required? If you could
# # answer this in multiple ways, does the choice you make impact speed?
# # When all threads have terminated, print “The final value of bar is xxxxx.” (print the value in
# # decimal format)


# Now, using the Linux time command, run your program for t ranging from 1 to 16, on a nonvirtualized machine. VMs introduce significant overheads. First, run your program on a single
# core. Then run it on 4 cores. To do this, you need to learn about the Linux taskset command.
# Plot two graphs: one showing how performance varies as a function of t for a single core, and
# the second (with the identical y axis scale!) showing how performance varies with 4 cores.