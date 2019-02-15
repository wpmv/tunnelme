#!/usr/bin/env python3


import time

def run():
    input("Password:")
    time.sleep(1)
    text = input("Enter a response to the grid challenge [J4] [G2] [J5] [B1] using a card with serial number 10115.")
    time.sleep(1)
    input("Password:")
    time.sleep(0.1)
    print("Complete! Answered with '{}'".format(text))

if __name__ == "__main__":
    run()
