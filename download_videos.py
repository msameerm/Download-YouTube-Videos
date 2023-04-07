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

if __name__ == '__main__':

    main()

