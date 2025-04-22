# 🐳 Docker Practice Lab

Welcome to my Docker lab! This repo is where I practice Docker fundamentals, containerize apps, and explore real-world container workflows. It's part of my journey into cloud infrastructure and DevOps. 🚀

## 📁 Project Structure

```plaintext
docker-practice/
├── app/              # Application code (e.g., Python, Node.js, etc.)
├── Dockerfile        # Instructions for building the image
├── .dockerignore     # Files to exclude from the image build
├── requirements.txt  # Python dependencies (if using Python)
└── README.md         # You're here!
```

## 🧠 What I'm Practicing

- Writing clean, efficient Dockerfiles
- Building and running containers locally
- Using `.dockerignore` to optimize image builds
- Running containerized apps with `docker run`
- Experimenting with `docker-compose` (coming soon)
- Learning best practices for container workflows

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
