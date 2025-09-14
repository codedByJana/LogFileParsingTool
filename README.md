# Log Parsing Tool

## What's That?
A Python script that parses `.log` and `.txt` files in a given directory and exports the results into a CSV file.  
This makes it easier to investigate logs with tools like Excel or SIEMs.

## Features
- Parses all `.log` and `.txt` files in a directory.
- Extracts:
  - Timestamp
  - Log level (INFO, ERROR, WARNING, etc.)
  - Message
  - IP addresses
  - Status values
- Saves results into `parsed_logs.csv`.

## Usage

### Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### Run The Script 
`python logParsingTool.py <directory-path>`
#### Example 
`python logParsingTool.py "C:\Users\dell\logs"`

#### Example Log
`
06/12 14:23:45 INFO: User logged in from 192.168.1.1 status: success \n
06/12 14:25:10 ERROR: Connection failed from 10.0.0.5 status: failed
`
#### CSV Output
|timestamp	|ip	| status|
|--------|--------|--------|
|06/12 14:23:45 |	192.168.1.1 | success|
|06/12 14:25:10	| 10.0.0.5 | failed


#### Requirements
Python 3.x

##### Standard libraries: os, glob, re, csv, argparse

#### Future Work
 - Add more log format support
 - Add filtering options
 - Support JSON output
