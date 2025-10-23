# AWS-Cloud-Practitioner-Portfolio
AWS Serverless Contact Form

Introduction

This project is a fully serverless contact form built using Amazon Web Services (AWS). It allows users to send messages directly from a website  without needing a traditional backend server.

When someone fills in the form and clicks “Send”, their message travels through several AWS services that work together in a seamless, automated way. The message is processed securely in the cloud and then delivered straight to my email inbox.

I built this project to learn and demonstrate how AWS Lambda, API Gateway, and Simple Email Service (SES) can integrate to create a lightweight, event-driven application that’s cost-effective and easy to maintain.

What makes this project special is that it’s built entirely on serverless architecture, meaning there are no servers to manage, no infrastructure costs when idle, and it scales automatically based on user requests.






Tools and Technologies Used

Amazon Web Services (AWS)

AWS Lambda

Amazon SES (Simple Email Service)

API Gateway

CloudWatch (for logs)

IAM (for permissions)

Frontend Development: HTML, CSS, JavaScript

Code Editor: Visual Studio Code

Web Browser: Microsoft Edge








Project Overview

The goal of this project was to design a functional, visually appealing contact form that could send user messages directly to my email address using cloud technology.

Here’s a breakdown of how the system works:

Frontend (HTML, CSS, JavaScript)

The user interface is built with HTML and styled with CSS for a clean, modern look.

JavaScript handles the form submission process, sending user input (Name, Email, Message) to AWS via a REST API call.

AWS API Gateway

API Gateway serves as the entry point for all requests from the frontend.

It securely accepts the form data and triggers the Lambda function.

CORS (Cross-Origin Resource Sharing) is enabled so the web page can communicate with the AWS API.

AWS Lambda Function

The Lambda function is the “brain” of the system.

It receives the form data from API Gateway, processes it, and uses Amazon SES to send the email to my inbox.

The function is written in JavaScript (Node.js runtime).

Amazon Simple Email Service (SES)

SES is used to actually send the emails.

Since the account is in the sandbox environment, I verified my email (nomzamopreciousdhlamini@gmail.com) as both sender and receiver.

This ensures that messages are delivered securely and reliably.

Response to Frontend

After the message is sent, Lambda returns a success or failure response.

The webpage displays a message like “Message sent successfully!” or “Failed to send message. Please try again.”










Conclusion 
This entire project culminated in the successful implementation of a production-ready, highly efficient Serverless Contact Form API using foundational AWS services. The architecture adheres to modern best practices, demonstrating proficiency in integrating a client-side web form with an AWS backend powered by API Gateway, AWS Lambda, and Amazon SES. The API Gateway provides a public, scalable entry point, securely invoking the Python-based Lambda function which acts as the core business logic, safely parsing user input and orchestrating the email dispatch. Ultimately, the system achieved its primary goal: successfully receiving data from the frontend and sending an email notification, confirmed by the final HTTP 200 Success status in the API Gateway logs and the arrival of the test email.

The journey to completion served as a comprehensive, hands-on masterclass in AWS troubleshooting, with the most significant learning centered on IAM permissions and deployment synchronization. The persistent initial failure, indicated by the HTTP 500 status despite correct code, was resolved by correctly attaching the AmazonSESFullAccess policy to the Lambda execution role, proving that secure access control (IAM) is the most critical component in serverless integration. Furthermore, the need for explicit API Gateway re-deployment after Lambda configuration changes, as well as meticulous attention to CORS headers in the Lambda response, highlighted the subtle, non-code dependencies required for successful end-to-end communication between the browser and the cloud. This project is a strong validation of practical cloud skills, demonstrating not only deployment capability but also the essential ability to diagnose and resolve complex integration issues within the AWS ecosystem.
