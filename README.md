# Student Management System – Docker & Kubernetes Deployment

A Flask-based Student Management System containerized using Docker and deployed on Kubernetes with two replicas and a NodePort Service.

## Project Overview

This project demonstrates the containerization and orchestration of a Python Flask web application using Docker and Kubernetes.

The application allows users to:
- Add student records.
- View student records.
- Delete student records.
- Access the application through a web browser.

The primary objective is to understand Docker image creation, container execution, Kubernetes Deployments, Pods, and Services.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | Web application framework |
| HTML | Frontend |
| Docker | Application containerization |
| Kubernetes | Container orchestration |
| YAML | Kubernetes configuration |
| Git & GitHub | Version control |

## Project Structure

```text
flask-app-docker-k8s/
│
├── app.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── k8s/
    ├── deployment.yaml
    └── service.yaml
```

## Application Features

1. Add Student – Enter student name, roll number, and course.
2. View Students – Display student records in a table.
3. Delete Student – Remove student records.

## Docker Implementation

### 1. Build Docker Image

```bash
docker build -t student-management-system:1.0 .
```

### 2. Run Docker Container

```bash
docker run -d --name student-management-app -p 8080:5000 student-management-system:1.0
```

### 3. Verify Running Container

```bash
docker ps
```

### 4. Access Application

```text
http://localhost:8080
```

## Kubernetes Implementation

The application is deployed on Kubernetes using a Deployment and NodePort Service.

### 1. Deploy Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
```

### 2. Create Kubernetes Service

```bash
kubectl apply -f k8s/service.yaml
```

### 3. Verify Deployment
