#!/usr/bin/python3

for x in range(10):
    for y in range(x + 1, 10):
        print(f"{x:01d}{y:01d}", end=", ")
print("/n")
