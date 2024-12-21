# sshBrute

```
                  __    ____             __        
       __________/ /_  / __ )_______  __/ /____    
      / ___/ ___/ __ \/ __  / ___/ / / / __/ _ \   
     (__  |__  ) / / / /_/ / /  / /_/ / /_/  __/   
    /____/____/_/ /_/_____/_/   \__,_/\__/\___/    
                                                    
```

SSH Bruteforcer

## Installation

```
# Clone the project locally
git clone https://github.com/basedBaba/sshBrute

# Create a virtual environment and install the required packages
cd sshBrute
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Make the script executable
chmod +x sshbrute.py

./sshbrute.py -h
```

## Usage

### Help

```
usage: sshbrute.py [-h] [-p PORT] -w WORDLIST -u USERNAME target

SSH Bruteforcer

positional arguments:
  target                host to attack on e.g. 93.184.216.34

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  port to attack on, default:22
  -w WORDLIST, --wordlist WORDLIST
                        list of passwords to use
  -u USERNAME, --username USERNAME
                        username to use
```

### Example

```
./sshbrute 93.184.216.34 -u user -w rockyou.txt
```