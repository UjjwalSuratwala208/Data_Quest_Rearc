# Data_Quest_Rearc

This quest is a good way to get the idea and learn more about what skill set will be needed to build and design the Data pipeline architecture.  

PART-1 :
--------------
- This part is about the showing the Managing the data fom the different sources via utilizing the AWS S3 and 
implementing in python.

- US.Bureau of Labour Statistics  - time series dataset  was used for republishing and to store in s3.

- `Part-1.py` python script file to process  the data from website and upload the file got from website in S3 and also keep in sync with source when the data on the website is updated, deleted or added. 


- Steps for execution:-
-------------------------

1) Run the Script `Part-1.py` to extract the file form the link for bls.gov/pub.time series/pr link.
2) Upload the files we got from above mentioned the links into a local directory.
3) Upload all the files into s3 using Boto3.
 
- Command to execute PART-1: 
--------------------------------
- Command: `0 22 * * * .... python Part-1.py` 

CRON Expression: 
-- It wll run every 0 minute of hour 22. 
It will execute `Part-1.py` 


PART-2 :
--------------
- In this section, mainly  focusing on working with the API for sourcing the data and to store it in-house AWS S3.

- The Data USA API is used which has information related to the Population data. I have created the script Population_API.py to fecth the data.  


- Steps for execution:
----------------------

1) Run the `Population_API.py` to fetch the data from the API and stored the result in a JSON
2) Upload the JSON file in S3 - create new bucket in S3
3) Using AWS CLI to upload the JSON file in to the S3 bucket.


- Command to execute PART-2: 
--------------------------------

1) `AWS S3 sync Local to S3 bucket` – Copying/Uploading files
2) After the uploading, execute `aws s3 ls`  to see the list of uploaded files. 

- Command to execute PART-2: 
--------------------------------
- Command: `0 22 * * * .... python Population_API.py` 

CRON Expression: 
-- It wll run every 0 minute of hour 22. 
It will execute `Part-1.py` 


Note: For Both Part-1 and Part-2, This will be hosted on EC2 instance. 
