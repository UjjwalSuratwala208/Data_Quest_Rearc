#Script to fecth file

# imoport necesarry libraries

import requests
from bs4 import BeautifulSoup


# reading the URL
url = 'https://download.bls.gov/pub/time.series/pr/'
print("URL",url)


# Requests URL and get response object
response = requests.get(url)
print(" \n Responses",response)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
print("parsed text \n", soup)

# Find all hyperlinks present on webpage
for links in soup.find_all('a'):

    fileurl = url+links.contents[0]
    print("file Url \n", fileurl)

    filename =links.contents[0]
    print("filename \n",  links.contents[0])

    r = requests.get(fileurl)
    with open('data/'+filename,'wb') as f:
        f.write(r.content)



# uploading the file using Boto3 into s3
# import necessary packages
import boto3
import os

# specify S3 service
client = boto3.client('s3')



#  uploading the file into s3 bucket
path = os.listdir('data/')

for file in path:
  #  print(file)
    full_path = "data/"+file
    with open(full_path, 'rb') as f:

        upload_file_bucket = 'dataquest-rearc'
        upload_file_key = 'part-1/  data/' + str(file)
        print(upload_file_bucket, upload_file_key, file)
        client.upload_fileobj(f, upload_file_bucket, upload_file_key)





