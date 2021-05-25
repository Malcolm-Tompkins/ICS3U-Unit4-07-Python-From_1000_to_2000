#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 25, 2021
# Shows all numbers in between 1000 and 2000


def main():
    loop_counter = 1000
    while loop_counter < 2000:
        loop_counter = loop_counter + 1
        mod = loop_counter % 5
        print("{} ".format(loop_counter), end="")
        if mod == 0:
            print("\n")


if __name__ == "__main__":
    main()
