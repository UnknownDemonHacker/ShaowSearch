# ShadowSearch

ShadowSearch is a powerful command-line tool for searching files on your system. It's designed to be fast, efficient, and easy to use.

## Features

- **Fast Search**: ShadowSearch uses Python's built-in `os` and `fnmatch` modules to quickly search for files.
- **Flexible Criteria**: You can search for files based on their name, extension, and last modified date.
- **Progress Bar**: ShadowSearch includes a progress bar that updates as the search progresses.
- **Color-Coded Output**: Search results are displayed in cyan, and other messages are displayed in green.
- **Logging**: ShadowSearch saves the search results to a structured JSON log file.

## Installation

1. Ensure that Python 3 is installed on your system.
2. Install the required Python modules with pip:

```bash
pip install tqdm termcolor
```

3. Download the ShadowSearch script and give it execute permissions:

```bash
chmod +x /path/to/your/script.py
```

4. Create a symbolic link to the script in a directory on your system's PATH:

```bash
sudo ln -s /path/to/your/script.py /usr/local/bin/search
```

## Usage

To run ShadowSearch, simply type `search` in the command line. The script will prompt you for the root directory, file name, file extension, and file date.

If you don't provide a root directory, the search will start from '/'. If you don't provide a file name or extension, the script will search for all files. If you don't provide a date, the script will not filter by date.

The search results will be displayed in the terminal and saved to a log file in the './logs' directory.

## Future Improvements

- **Multithreading**: Use multithreading to speed up the search.
- **More Search Criteria**: Add more search criteria, such as file size and permissions.
- **User-Friendly Interface**: Add a user-friendly command-line interface with the argparse module.

Please note that this is a basic version of the tool and there are many ways to optimize and add features to it. However, this script is a good start 
