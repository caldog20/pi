import wiringpi as wpi
wpi.wiringPiSetupGpio()
wpi.pinMode(21, 1)
wpi.digitalWrite(21,1)
