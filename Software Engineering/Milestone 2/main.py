#!/usr/bin/env python
"""
Project: Milestone 2 - UVSim
Group Members:  Ali Aydogdu
                Triston Yocom
                Bryson May
                John Revill
Course: CS 2450-X01
Date Created: 7/9/2021
Date Last Modified: 7/9/2021
"""


from uvsim import UVSim


def main():
    """
    Main
    Author: Ali Aydogdu
    """
    uvsim = UVSim()
    uvsim.initialize()
    uvsim.program()
    uvsim.execute()
    uvsim.memdump()


if __name__ == "__main__":
    main()
