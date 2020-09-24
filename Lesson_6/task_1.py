import time


class TrafficLight:
    __color = {7: "Red", 2: "Yellow", 10: "Green"}

    def running(self):
        while True:
            for sec, switch in TrafficLight.__color.items():
                print(switch)
                time.sleep(sec)
            print(TrafficLight.__color.get(2))
            time.sleep(2)


street = TrafficLight()
street.running()


