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
   Create a standard queue
   Name: ProductOrdersQueue
   Update the code on step 1 to have this queue's URL

3. Deploy **submit-order** lambda function
   Create a test event with the following data
   

 
