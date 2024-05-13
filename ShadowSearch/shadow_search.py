#!/usr/bin/env python3
import os
import fnmatch
import time
import json
import argparse
from datetime import datetime
from tqdm import tqdm
from termcolor import colored

class ShadowSearch:
    def __init__(self, log_dir='./logs'):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def search(self, root_dir='/', name=None, extension=None, date=None):
        matches = []
        for root, dirnames, filenames in tqdm(os.walk(root_dir), desc='Searching', unit='files'):
            for filename in filenames:
                if name and name not in filename:
                    continue
                if extension and not filename.endswith('.{}'.format(extension)):
                    continue
                if date:
                    file_date = datetime.fromtimestamp(os.path.getmtime(os.path.join(root, filename))).date()
                    if file_date != date:
                        continue
                matches.append(os.path.join(root, filename))
        return matches

    def log_search(self, matches):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        log_file = os.path.join(self.log_dir, 'search_{}.json'.format(timestamp))
        with open(log_file, 'w') as f:
            json.dump(matches, f, indent=4)
        print(colored("Search results saved to {}".format(log_file), 'green'))

    def run(self):
        root_dir = input('Enter the root directory to start the search (default: /): ') or '/'
        name = input('Enter the name of the file to search for (optional): ')
        extension = input('Enter the extension of the file to search for (optional): ')
        date_str = input('Enter the date of the file to search for (format: YYYY-MM-DD, optional): ')
        date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None

        start_time = time.time()
        matches = self.search(root_dir, name, extension, date)
        self.log_search(matches)
        end_time = time.time()
        print(colored("Found {} matches in {} seconds".format(len(matches), end_time - start_time), 'green'))
        for match in matches:
            print(colored(match, 'cyan'))

if __name__ == "__main__":
    ss = ShadowSearch()
    ss.run()
