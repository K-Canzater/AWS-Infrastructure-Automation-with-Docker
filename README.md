# 🐳 Docker Practice Lab

Welcome to my Docker and AWS Automation lab! This repo is where I practice real-world DevOps workflows — including containerizing infrastructure scripts, managing AWS resources, and building repeatable automation tools using Docker and Python. 🚀

## 📁 Project Structure

```plaintext
docker-practice/
├── aws-tools/   
│   ├── stop-instances.py          # Python script to stop EC2 instances
│   ├── Dockerfile                 # Instructions for building the image
│   ├── requirements.txt           # Python dependencies (if using Python)
│   └── .dockerignore              # Files to exclude from the image build
├── README.md                      # You're here!

```

## 🧠 What I'm Practicing

- Writing clean, efficient Dockerfiles for AWS infrastructure automation
- Containerizing Python scripts that use Boto3 and the AWS CLI
- Using `.dockerignore` to reduce image size and improve build performance
- Reproducing real-world DevOps workflows with Docker (credentials, environment vars, etc.)
- Building a foundation for Docker use in CI/CD pipelines, Jenkins jobs, and Kubernetes clusters

## 🛠️ Tech Stack

- **Docker CLI**
- **Python** (for AWS automation scripts using Boto3)
- **AWS CLI & SDK (Boto3)**
- **VS Code**
- **Git & GitHub**

## 🚀 How to Run It

```bash
# Build the Docker image
docker build -t docker-practice-app .

# Run the container
docker run -p 8080:8080 docker-practice-app
```

## 🧪 Future Experiments

- Docker Compose (multi-container setup)
- Volumes and persistent data
- Networking between containers
- Custom base images for automation tooling
- Environment variables & `.env` files
- Pushing images to Docker Hub
- Integrating Docker into Jenkins pipelines
- Deploying containers to AWS (ECS or EC2)
