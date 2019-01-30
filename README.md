# UVDetection
Python program built for Raspberry Pi implementation that alerts the wearer of UV overexposure by measuring time exposed and current UV index

This program was created for a design project in my Health Solutions Design Projects Course that required the implementation of a sensor into a wearable device. The algorithm takes readings from the UV sensor and takes an average of all collected data points continuously. It then checks which UV index the average UV readings are in, and sets a countdown timer appropriately, that marks how long it is safe to stay in the sun. A buzzer buzzes once at five minutes before overexposure begins, and then constantly after the timer reaches zero.
