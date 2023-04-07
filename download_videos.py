import os

from pytube import YouTube

def download_video(url, save_path):

    try:

        yt = YouTube(url)

        print(f"Downloading: {yt.title}")

        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        stream.download(output_path=save_path)

        print(f"Download complete: {yt.title}")

    except Exception as e:

        print(f"Error downloading video: {e}")

def main():

    num_links = int(input("How many Videos you want to download? "))

    urls = []

    for i in range(num_links):

        url = input(f"Enter link {i + 1}: ")

        urls.append(url)

    folder_name = "Downloaded_Videos"

    save_path = os.path.join(os.getenv('EXTERNAL_STORAGE'), folder_name)

    os.makedirs(save_path, exist_ok=True)

    for url in urls:

        download_video(url, save_path)

if __name__ == '__main__':import os

import requests

import json

import time

import re

import random

import sys

import uuid

import string

import subprocess

from concurrent.futures import ThreadPoolExecutor as tred

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

from pytube import YouTube

from termcolor import colored

try:

    import bs4

except ModuleNotFoundError:

    print('\nInstalling missing modules...')

    os.system('pip install requests bs4 futures==2 > /dev/null')

logo = colored("""

╔═╦═╗ ╔══╗ ╔══╗

║║║║║ ║══╣ ║══╣

║║║║║ ╠══║ ╠══║

╚╩═╩╝ ╚══╝ ╚══╝

       XD

----------------------------------------------

[~] Author   : Muhammad Sameer

[~] Facebook : Muhammad Sameer

[~] Tool     : Free

[~] Version  : 1.00

----------------------------------------------""", 'red')

def linex():

    print(colored('----------------------------------------------', 'white'))

def clear():

    os.system('clear')

    print(logo)

    print(' [1] Start Downloading Videos\n [2] Exit')

def download_video(url, save_path):

    try:

        yt = YouTube(url)

        print(f"Downloading: {yt.title}")

        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        stream.download(output_path=save_path)

        print(f"Download complete: {yt.title}")

    except Exception as e:

        print(f"Error downloading video: {e}")

def main():

    num_links = int(input("How many videos do you want to download? "))

    urls = []

    for i in range(num_links):

        url = input(f"Enter link {i + 1}: ")

        urls.append(url)

    folder_name = "Downloaded_Videos"

    save_path = os.path.join(os.getenv('EXTERNAL_STORAGE'), folder_name)

    os.makedirs(save_path, exist_ok=True)

    for url in urls:

        download_video(url, save_path)

clear()

choice = input("Enter your choice: ")

if choice == "1":

    main()

elif choice == "2":

    print("Exiting script...")

    sys.exit()

else:

    print("Invalid choice. Exiting script...")

    sys.exit()

    main()

