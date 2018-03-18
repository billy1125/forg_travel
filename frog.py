import time

class frog:

    def __init__(self, frog_name):
        self.frog_name = frog_name

        self.backpack = {}

    def go_to_travel(self, backpack):
        count = 0
        gift = []

        for i in range(0, len(backpack)):
            count += backpack[i]
            if count > 10 :
                gift.append('A')

        self.stopwatch(count)

        return gift

    def my_name(self):
        return self.frog_name

    def stopwatch(self, seconds):
        start = time.time()
        time.clock()    
        elapsed = 0
        while elapsed < seconds:
            elapsed = time.time() - start
            print("loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed))
            time.sleep(1)  

