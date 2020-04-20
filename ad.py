import sys
sys.path.append('libs/')
from pimods import *
import smbus

# Init smbus for module

bus = smbus.SMBus(1)

while True:
    ## Init AN0 on module
    bus.write_byte(0x48, 0)
    ## Read value of AN0 address
    value = bus.read_byte(0x48)
    print(value)
    time.sleep(1)

