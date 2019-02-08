"""
Make a small square. Purpose is to teach myself to program the drone.
"""

# boilerplate to connect and takeoff
from pyparrot.Bebop import Bebop
import math

bebop = Bebop()

print("connecting")
success = bebop.connect(10)
print(success)

print("sleeping")
bebop.smart_sleep(5)

bebop.ask_for_state_update()

bebop.safe_takeoff(10)

# do it using move_relative()
# fly forward
bebop.move_relative(1, 0, 0, 0)

bebop.smart_sleep(2)

# fly right
bebop.move_relative(0, 1, 0, 0)

bebop.smart_sleep(2)

# fly backward
bebop.move_relative(-1, 0, 0, 0)

bebop.smart_sleep(2)

# fly left
bebop.move_relative(0, -1, 0, 0)

bebop.smart_sleep(2)

bebop.disconnect()


