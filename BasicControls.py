from djitellopy import tello
from time import sleep

# connecting to tello drone
hello = tello.Tello()
hello.connect()
print(hello.get_battery())

# the done goes forward and lands itself
hello.takeoff()
hello.send_rc_control(0, 50, 0, 0)
sleep(5)
hello.send_rc_control(0, 0, 0, 30)
sleep(5)
hello.send_rc_control(0, 0, 0, 0)
hello.land()
