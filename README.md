# InstaFinder
Scrape & filter Instagram username and full name of account's follower, recursively.
## Description

Instafinder scrape all username and full name of public account based on follower of follower of follower of follower...\
InstaFinder use and change proxies automatically to prevent being refused requests.\
You can then filter username and full_name with your keywords

## Getting Started

### Installation
1. [Download](https://www.python.org/downloads/) and install Python >= 3.8
2. Clone the repo
   ```sh
   git clone https://github.com/Electro007/InstaFinder.git
   ```
3. Install the [dependencies](requirements.txt)
   ```sh
   pip install -r requirements.txt
   ```

### Configuration
1. Change bot info in [configuration.py](configuration.py)
   ```py
   ACCOUNT_USERNAME = "YOUR_IG_USERNAME"
   ACCOUNT_PASSWORD = "YOUR_IG_PASSWORD"
   FIRST_ACCOUNT_USERNAME = "ACCOUNT_USERNAME_TO_CHECK"
   ```
2. Enter your keyword in [keywords.txt](keywords.txt)
   ```
   john
   doe
   lorem
   ipsum
   jo
   rem
   ```


## Usage

1. Parse data
   ```sh
   py parse.py
   ```

2. Filter data
   ```sh
   py filter.py
   ```
## Results
### Location
Raw data is located in 
```
~/data/raw_data.json
```
Filtered data is located in 
```
~/data/filtered_data.json
```
### Format
Both data files is stored in the following format :
```json
{
"username":"full_name",
"username":"full_name",
"username":"full_name",
"username":"full_name",
}
```
