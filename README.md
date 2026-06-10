# ☁️ Cloud File Storage System

## Live Demo

**Deployed Application**

https://cloudstorage-app.onrender.com

---

# Project Overview

Cloud File Storage System is a cloud-based web application that enables users to securely upload, manage, and share files using Amazon S3. The application uses Google OAuth 2.0 for authentication and is deployed on Render for public access.

The project demonstrates cloud storage integration, secure authentication, and cloud deployment in a practical environment.

---

# Problem Statement

Traditional local storage systems limit accessibility and file sharing capabilities. This project provides a cloud-based solution that allows authenticated users to upload, download, share, and manage files securely from anywhere.

---

# Objectives

* Build a cloud-based file storage application.
* Implement secure user authentication.
* Store files using AWS S3.
* Allow users to upload, download, delete, and share files.
* Deploy the application on a cloud platform.

---

# Features

## Authentication

* Google OAuth 2.0 Login
* Secure User Authentication
* Session Management
* Logout Functionality

## File Management

* Upload Files
* View Uploaded Files
* Download Files
* Delete Files
* Generate Shareable Links

## Cloud Features

* AWS S3 Integration
* Bucket Versioning Enabled
* Secure IAM Access

## Deployment

* Hosted on Render
* Publicly Accessible

---

# Technology Stack

## Frontend

* HTML5
* CSS3

## Backend

* Python
* Flask

## Cloud Services

* Amazon S3
* Google OAuth 2.0
* Render

## Libraries Used

* Flask
* Boto3
* Authlib
* Gunicorn

---

# System Architecture

User

↓

Google OAuth Authentication

↓

Flask Application

↓

AWS S3 Storage

↓

File Management Operations

---

# Project Workflow

## User Authentication

1. User opens the application.
2. User clicks Login with Google.
3. Google verifies the user.
4. User is redirected to the dashboard.

## File Upload

1. User selects a file.
2. Flask receives the file.
3. File is uploaded to AWS S3.
4. Dashboard is updated.

## File Download

1. User clicks Download.
2. Flask generates a pre-signed URL.
3. File is downloaded securely.

## File Sharing

1. User clicks Share.
2. A temporary shareable link is generated.
3. User can share the file.

## File Deletion

1. User clicks Delete.
2. File is removed from AWS S3.
3. Dashboard refreshes automatically.

---

# Project Structure

```text
CloudFileStorage
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
│
└── templates
    ├── login.html
    └── index.html
```

---

# AWS Services Used

## Amazon S3

Purpose:

* File Storage
* File Retrieval
* File Sharing
* Versioning

## IAM

Purpose:

* Secure Access Control
* Programmatic Access

---

# Google OAuth 2.0

Used For:

* User Authentication
* Secure Login
* Identity Verification

Benefits:

* No Password Storage
* Reliable Authentication
* Industry Standard Security

---

# Deployment

The application is deployed using Render.

## Deployment Steps

1. Push source code to GitHub.
2. Connect repository to Render.
3. Configure environment variables.
4. Deploy using Gunicorn.
5. Configure Google OAuth redirect URLs.

---

# Environment Variables

```env
AWS_ACCESS_KEY=YOUR_AWS_ACCESS_KEY
AWS_SECRET_KEY=YOUR_AWS_SECRET_KEY

BUCKET_NAME=YOUR_BUCKET_NAME
REGION=ap-south-1

GOOGLE_CLIENT_ID=YOUR_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_CLIENT_SECRET

SECRET_KEY=YOUR_SECRET_KEY
```

---

# Installation and Setup

## Clone Repository

```bash
git clone <repository-url>
cd CloudFileStorage
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

## Open Browser

```text
http://127.0.0.1:5000
```

---

# Application Screenshots

## Login Page

<img width="1907" height="1028" alt="image" src="https://github.com/user-attachments/assets/9b02c589-65cc-4d4c-85ee-a0053ae2ff99" />


---

## Dashboard

<img width="1907" height="1022" alt="image" src="https://github.com/user-attachments/assets/1b711fe2-44a5-41d8-9428-b035dd679861" />



---

## Upload File

<img width="1907" height="1026" alt="image" src="https://github.com/user-attachments/assets/4670fa4e-7a16-40f4-afdf-846200b597ae" />




---

# Link Generated

<img width="1582" height="462" alt="image" src="https://github.com/user-attachments/assets/96ade0c6-bea3-4f94-be70-72e33fba7b77" />



# Learning Outcomes

Through this project, the following concepts were explored:
+++++++
* Cloud Computing Fundamentals
* AWS S3 Integration
* IAM Access Management
* OAuth Authentication
* Flask Web Development
* Cloud Deployment
* Environment Variables
* Secure File Handling

---

# Future Enhancements

* User-specific folders
* File Search Functionality
* File Preview Support
* Storage Usage Analytics
* Multi-file Upload
* Database Integration
* Role-Based Access Control
* Email Notifications

---

# Conclusion

The Cloud File Storage System demonstrates the integration of cloud technologies with web application development. The project provides secure authentication, cloud-based file management, and public deployment while maintaining simplicity and scalability.

It serves as a practical implementation of cloud computing concepts and modern application deployment.
