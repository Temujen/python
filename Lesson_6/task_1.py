import time


class TrafficLight:
    __color = {7: "Red", 2: "Yellow", 10: "Green"}

    def running(self):
        while True:
            for sec, switch in TrafficLight.__color.items():
                self.color_set(switch)
                time.sleep(sec)
            self.color_set('Yellow')
            time.sleep(2)

    def color_set(self, check):
        if check == 'Red':
            print("\033[31m {}".format(check))
        elif check == 'Yellow':
            print("\033[33m {}".format(check))
        elif check == 'Green':
            print("\033[32m {}".format(check))


street = TrafficLight()
street.running()
