# docker-lab
Hands-on Docker practice: containerizing apps, building images, and exploring real-world container workflows.

# 🐳 Docker Practice Lab

Welcome to my Docker lab! This repo is where I practice Docker fundamentals, containerize apps, and experiment with real-world container workflows. It's part of my journey into cloud infrastructure and DevOps 🚀

---

## 📁 Project Structure

docker-practice/ ├── app/ # App code (e.g., Python, Node, etc.) ├── Dockerfile # Image build instructions ├── .dockerignore # Optional: files to exclude from image ├── requirements.txt # Python dependencies (if using Python) └── README.md # You're here!

---

## 🧠 What I'm Practicing

- Writing clean, efficient Dockerfiles
- Building and running containers locally
- Using `.dockerignore` to optimize image builds
- Running containerized apps with `docker run`
- Experimenting with `docker-compose` (coming soon)
- Learning best practices for container workflows

---

## 🛠️ Tech Stack

- **Docker CLI**
- **Python** (Flask for now, but may add other stacks)
- **VS Code**
- **Git & GitHub**

---

## 🚀 How to Run It

```bash
# Build the Docker image
docker build -t docker-practice-app .

# Run the container
docker run -p 8080:8080 docker-practice-app

🧪 Future Experiments
Docker Compose (multi-container setup)

Volumes and persistent data

Networking between containers

Custom base images

Environment variables & .env files

Pushing images to Docker Hub

Deploying containers to AWS (ECS or EC2)
