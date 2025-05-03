# 🐳 Docker Practice Lab

Welcome to my Docker lab focused on AWS infrastructure automation. This project showcases my ability to containerize Python scripts using Docker and interact with AWS services securely and repeatably — a foundational skill for real-world DevOps workflows.🚀

## 💡 Why I Built This

I created this lab to deepen my hands-on experience with:

- Containerizing infrastructure tools using Docker
- Automating EC2 instance operations with Python (Boto3)
- Managing environment variables and credentials securely
- Preparing for CI/CD pipelines, Jenkins jobs, and Kubernetes workloads

My goal is to simulate real-world DevOps tasks and demonstrate the ability to build reliable, portable automation tools.






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
docker run \
  -v C:/Users/YourUsername/.aws:/root/.aws \
  -e AWS_PROFILE=YourAWSProfile \
  -e AWS_SDK_LOAD_CONFIG=1 \
  -e INSTANCE_IDS="i-xxxxxxxxxxxxxxxxx,i-yyyyyyyyyyyyyyyyy" \
  stop-instances```

## 🧪 Future Experiments

- Docker Compose (multi-container setup)
- Volumes and persistent data
- Networking between containers
- Custom base images for automation tooling
- Environment variables & `.env` files
- Pushing images to Docker Hub
- Integrating Docker into Jenkins pipelines
- Deploying containers to AWS (ECS or EC2)
