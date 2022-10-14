#Script for fecthing files from URL

# import libraries

import requests
from bs4 import BeautifulSoup
import os
import boto3

upload_file_bucket = 'dataquest-rearc'
# reading the URL
url = 'https://download.bls.gov/pub/time.series/pr/'

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
for links in soup.find_all('a'):
    fileurl = url+links.contents[0]
    # print("file Url \n", fileurl)

    fileurl.split('/')[-1]
    filename =links.contents[0]


    if not '[To Parent Directory]' == str(filename) or not '[To Parent Directory]' in fileurl or not fileurl.split('/')[-1]=='[To Parent Directory]':
        r = requests.get(fileurl)
        if 'Current' in filename or 'AllData' in filename:
            filename+='.csv'
            print('Fileurl:', fileurl, 'Filename', filename)
        with open('data/'+filename,'wb') as f:
            f.write(r.content)

# uploading the file using Boto3 into s3

# specify S3 service
client = boto3.client('s3')

#  uploading the file into s3 bucket
path = os.listdir('data/')

def isModified(bucket, key, fname):
    s3 = boto3.resource('s3')
    try:
        obj = s3.Object(bucket, key)
        return int(obj.content_length) != int(os.path.getsize(fname)) # if file size is diff or file not found =, then upload into s3
    except Exception as e:
        print('Key not present')
        return True
for file in path:
  #  print(file)
    full_path = "data/"+file
    with open(full_path, 'rb') as f:


        upload_file_key = 'part-1/data/' + str(file)

        # check if file changed
        if isModified(upload_file_bucket,upload_file_key,full_path):
            print(upload_file_bucket, upload_file_key, file)
            client.upload_fileobj(f, upload_file_bucket, upload_file_key)


# compare and delete data from s3 for file deleted from website
local=os.listdir('data/')
s3_list=client.list_objects_v2(Bucket=upload_file_bucket,Prefix='part-1/data/')
s3_list=[obj['Key'].split('/')[-1] for obj in s3_list['Contents']]
print('local_list',local)
print('s3_list',s3_list)
res = set(local)-set(s3_list)
# Deletes the file from s3 that is removed from source
for file in list(res):
    response = client.delete_object(
        Bucket=upload_file_bucket,
        Key='part-1/data/'+file
    )

# delete data from local
for file in os.listdir("data/"):
    file='data/'+file
    if os.path.exists(file):
        os.remove(file)
    else:
        print("The file does not exist")