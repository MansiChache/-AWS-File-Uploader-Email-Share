These are the files used in AWS Cloud Computing Miniproject: File Upload and Email Share
The given below is the process done
🧾PROJECT: File Uploader + Email Sharer (AWS Microservices)
🔧 Tech Stack:
Frontend: HTML + JavaScript (static form)

Backend: AWS Lambda (Python)

Storage: Amazon S3

Email: Amazon SES

API: Amazon API Gateway

🔁 Workflow Overview
User uploads a file + enters an email.

File is uploaded to S3.

Lambda function is triggered via API Gateway.

Lambda:

Uploads file to S3.

Creates pre-signed download link.

Sends email with download link via SES.

🚀 STEP-BY-STEP INSTRUCTIONS (Windows OS + AWS Free Tier)
🔹 Step 1: Create an S3 Bucket (To Store Files)
Log in to AWS Console.

Go to S3 → Create bucket

Bucket Name: my-file-share-bucket (unique name!)

Region: Keep as default (or your nearest)

Uncheck: “Block all public access”

Enable: Versioning (optional)

Leave rest as default → Create bucket

🔹 Step 2: Set Up Amazon SES (Email Service)
📌 Initial Setup (in sandbox mode):
Go to SES Console → Verified Identities

Click Create Identity

Type: Email Address

Enter: your own email (e.g., you@gmail.com)

Check your inbox and click the verification link

🔒 Note: SES sandbox mode only allows sending emails to and from verified addresses.

🔹 Step 3: Create the Lambda Function (Backend)
📁 On your local Windows machine:
Create a folder lambda-code

Inside that folder, create a file lambda_function.py with:

🧱 Install Dependencies
SES and S3 are available by default in Lambda, so no need to install anything extra unless you want to use custom libraries.

🔹 Step 4: Create Lambda Function on AWS
Go to Lambda → Create Function

Name: FileShareFunction

Runtime: Python 3.12

Permissions: Create a new role with basic Lambda permissions

Upload handler.py

Under "Code Source", paste your handler.py code

Set environment variables (optional)

Increase timeout to 1 minute

🔹 Step 5: Set Lambda Permissions
Go to IAM → Roles → FileShareFunction-role

Attach the following policies:

AmazonS3FullAccess

AmazonSESFullAccess

AWSLambdaBasicExecutionRole

🔹 Step 6: Create API Gateway
Go to API Gateway → Create API

Type: REST API

Name: FileShareAPI

Add a POST route: /upload

Integration: Your Lambda function

Enable CORS (very important for frontend)

Deploy to a stage: prod

✅ Note down the endpoint, e.g.
https://xyz123.execute-api.us-east-1.amazonaws.com/upload

🔹 Step 7: Create Frontend Form (HTML + JS)
Create a file index.html and put the code in index.html file in it

Replace YOUR_API_GATEWAY_URL with your real endpoint.

🔹 Step 8: Run & Test
Open index.html in your browser.

Choose a file and enter your verified SES email.

Hit “Upload & Send”

Check your inbox – you should receive a pre-signed download link!
