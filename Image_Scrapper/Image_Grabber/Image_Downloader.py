import requests
import shutil
import os
from multiprocessing import Pool
import warnings
warnings.filterwarnings('ignore')

base_dir = r'C:\Users\SONY\Desktop\Celebs'
dedup_dir = r'C:\Users\SONY\Desktop\Celebs\Dedup_urls'


def image_download(dedup_urls_file):
    actress_name = (dedup_urls_file.split("\\")[-1]).split("_")[1]
    print("Processing {} with pid {}".format(actress_name, os.getpid()))
    actress_dir = os.path.join(base_dir, actress_name)
    os.makedirs(actress_dir, exist_ok=True)
    counter = 0

    with open(dedup_urls_file, 'r') as reader:
        for url in reader:
            counter += 1
            try:
                r = requests.get(url.strip(), stream=True, verify=False, timeout=7)
                with open(os.path.join(actress_dir, str(counter)+".jpg"), 'wb') as writer:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, writer)
            except: #I know too broad exception but be it.
                pass

if __name__ == "__main__":
    dedup_urls_files = [os.path.join(dedup_dir, dedup_file) for dedup_file in os.listdir(dedup_dir)]
    pool = Pool(3)
    pool.map(image_download, dedup_urls_files)
    pool.close()
    pool.join()
