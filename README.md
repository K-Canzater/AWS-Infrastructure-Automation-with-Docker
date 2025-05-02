# 🐳 Docker Practice Lab

Welcome to my Docker and AWS Automation lab! This repo is where I practice real-world DevOps workflows — including containerizing infrastructure scripts, managing AWS resources, and building repeatable automation tools using Docker and Python. 🚀

## 📁 Project Structure

```plaintext
aws-tools/
├── stop-instances.py              # Python script to stop EC2 instances
├── Dockerfile                     # Instructions for building the image
├── .dockerignore                  # Files to exclude from the image build
├── requirements.txt               # Python dependencies (if using Python)

README.md                      # You're here!
```

## 🧠 What I'm Practicing

- Writing clean, efficient Dockerfiles for infrastructure tools
- Building and running containerized Python scripts that interact with AWS
- Using `.dockerignore` to reduce image size
- Exploring real-world DevOps workflows using Docker and the AWS CLI/SDK
- Preparing for Docker use in CI/CD, Jenkins, and Kubernetes environments

## 🛠️ Tech Stack

- **Docker CLI**
- **Python** (Flask for now, but may add other stacks)
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
- Custom base images
- Environment variables & `.env` files
- Pushing images to Docker Hub
- Deploying containers to AWS (ECS or EC2)
