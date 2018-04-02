import requests

# Call this method to download file which will return a response object
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code #checking status code if the res succeed
#200 if the resquest suceeded, then the webpage will be store as a string as res.text
print(len(res.text))

# print(res.text[:500])

res.raise_for_status() # This will raise an exception if there was an error downloading the file


playFile = open('RnJ.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
