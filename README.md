# **Simple-Serverless-Coffee-Ordering-Application-with-REST-APIs**
## **Project Description**
This is a simple serverless e-commerce application where uses can order coffee using a browser on the shop's website that is hosted on S3 using REST APIs. This project leverages AWS Lambda for serverless compute, API Gatteway for managing the REST APIs, S3 for static website hosting, SQS for decoupling and DynamoDB for storing order records. Users can interact with the application via a frontend or Postman to make order requests. </br>

Use Cases:
- Order Management: users can simply order what they need and it's going to be stored in the database. This can be useful for stock management at the end of the day or month.</br>
- Handling Traffic Spikes: Sometimes, hundreds or thousands of users can submit order at the same time and to ensure the system works correcctly, SQS acts as a buffer holding the messages until when the next lambda function can be able to process them. </br>

## **Project Architecture**:
![alt text](https://github.com/TROISTROIS/Simple-Serverless-Coffee-Ordering-Application-with-REST-APIs/blob/main/Coffee%20Shop.jpg "Architecture Diagram") </br>

## Getting Started
### **Prerequisites**
1. AWS account with necessary permissions.
2. Visual Studio Code or editor of your choice.
3. Draw.io for drawing the architecture diagram.

### **Steps to follow**
1. Create the first Lamda function.
   Name: submit-order </br>
   Runtime: Python 3.x </br>
   Execution role: AmazonSQSFullAccess </br>

2. Create SQS queue
   Create a standard queue </br>
   Name: ProductOrdersQueue </br>
   Update the code on step 1 to have this queue's URL </br>

3. Deploy **submit-order** lambda function
   Create a test event with the following data </br>
   `{"body": "{\"productName\": \"Test Product 3\", \"quantity\": 1}"}`

4. Head over to SQS and poll for messages, you should see a message on the queue.
5. Create the second lambda function
   Name: process-orders</br>
   Runtime: Python 3.x </br>
   Execution role: AmazonSQSFullAccess and AmazonDynamoDBFullAccess
6. Create a DynamoDB table
   Name: ProductOrders</br>
   Primary Key: orderId</br>
   Add table name to **process-orders** lambda function.
7. Configure SQS to trigger **process-orders** lambda function
8. Check the DynamoDB table to see if the first test event was processed. You should see 1 item on the table.
9. Test using the CLI/CloudShell with a file named input.json with the following content : </br>
    `{"body": "{\"productName\": \"Test Product 7\", \"quantity\": 3}"}`
10. Invoke the lambda function using this file above : </br>
    `aws lambda invoke --function-name lambda-function --payload fileb://input.json output.json`
11. Create the API
    Create a REST API in the API Gateway console and name it ProductOrdersAPI</br>
    Create a new resource */orders* and enable **CORS**</br>
    Create a **POST** method for the resource and integrate it with **submit-order** lambda function.</br>
    Enable lambda proxy integration</br>
    Deploy the API to **prod**
12. Update the **index.html** file with your APIs URL.
13. Create an S3 bucket and configure it for static website hosting.
    Enable public access using the following bucket policy: </br>

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
       }
     ]
   }
   ```
14. Test the Application by placing an order
    
   
   
   

 
