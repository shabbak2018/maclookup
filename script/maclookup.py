import sys
import requests
program_name = sys.argv[0]
arguments = sys.argv[1]
url = "https://macaddress.io/" + arguments
result = requests.get(url);
print(result)
