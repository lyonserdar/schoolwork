#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
I declare that the following source code was written solely by me. I understand that 
copying any source code, in whole or in part, constitutes cheating, and that I will 
receive a zero on this project if I am found in violation of this policy.
"""

# * Concurrent Programming

__class__ = "CS 1410"
__project__ = "Project 7 - Concurrent Programming"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "4/15/2021"
__divider__ = "------------------------------------------------------------------------"

# Import libraries
import os
import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

URL = "https://www.sciencekids.co.nz/images/pictures/flags680/"
COUNTRY_NAMES_FILE = "flags.txt"
FLAGS_FOLDER = "flags/"


class Timer:
    def __init__(self):
        self.start_time = 0
        self.finish_time = 0

    @property
    def elapsed_time(self):
        return self.finish_time - self.start_time

    def start(self):
        self.start_time = perf_counter()

    def finish(self):
        self.finish_time = perf_counter()


def download_image_and_save(country_name):
    img_bytes = requests.get(f"{URL}{country_name}.jpg").content
    with open(f"{FLAGS_FOLDER}{country_name}.jpg", "wb") as f:
        f.write(img_bytes)
    return len(img_bytes)


def download_sequentially(country_names):
    timer = Timer()
    byte_count = 0
    timer.start()
    for country_name in country_names:
        byte_count += download_image_and_save(country_name)
    timer.finish()
    time_elapsed = timer.elapsed_time
    return time_elapsed, byte_count


def download_using_threads(country_names):
    timer = Timer()
    byte_count = 0
    timer.start()
    with ThreadPoolExecutor() as executor:
        for flag_bytes in executor.map(download_image_and_save, country_names):
            byte_count += flag_bytes
    timer.finish()
    time_elapsed = timer.elapsed_time
    return time_elapsed, byte_count


def download_using_processes(country_names):
    timer = Timer()
    byte_count = 0
    timer.start()
    with ProcessPoolExecutor() as executor:
        for flag_bytes in executor.map(download_image_and_save, country_names):
            byte_count += flag_bytes
    timer.finish()
    time_elapsed = timer.elapsed_time
    return time_elapsed, byte_count


def print_results(time_elapsed, byte_count, title="Elapsed Time and Bytes"):
    print(title)
    print(__divider__)
    print(f"Elapsed time: {round(time_elapsed, 5)} seconds")
    print(f"Bytes downloaded: {byte_count:,} bytes")
    print(__divider__)


def main():
    print(__divider__)
    print(__project__)
    print(__divider__)
    country_names = []

    # Read country names from file
    with open(COUNTRY_NAMES_FILE, "r") as f:
        country_names = f.read().splitlines()

    # Create flags folder if does not exist
    if not os.path.exists(FLAGS_FOLDER):
        os.makedirs(FLAGS_FOLDER)

    print_results(*download_sequentially(country_names), title="Sequentially")
    print_results(*download_using_threads(country_names), title="Using Threads")
    print_results(*download_using_processes(country_names), title="Using Processes")


if __name__ == "__main__":
    main()
