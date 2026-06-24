# Local Setup and Deployment Guide (Fedora Linux)

This guide provides step-by-step instructions to install Docker, clone this repository, and orchestrate the multi-container architecture for the Uber Price Prediction system.

---

## Prerequisites: Install Docker on Fedora

If you do not have Docker installed on your Fedora engine, execute the following system commands.

### 1. Remove conflicting packages
Fedora comes with alternative container tools by default. Remove them to prevent system conflicts:
```bash
sudo dnf remove docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-selinux \
                docker-engine-selinux \
                docker-engine
```

### 2. Set up the official Docker repository
```bash
sudo dnf -y install dnf-plugins-core
sudo dnf-plugins-core config-manager --add-repo [https://download.docker.com/linux/fedora/docker-ce.repo](https://download.docker.com/linux/fedora/docker-ce.repo)
```

### 3. Install Docker Engine and Buildx
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 4. Manage Docker as a non-root user
To avoid using sudo for every Docker command, add your user profile to the docker group:
```bash
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
```
Crucial: Log out of your desktop session and log back in (or `run newgrp docker`) for these permissions to take effect.

## Cloning and Launching the Application

1. Clone the Repository
Open your terminal and clone the source code:
```bash
git clone [https://github.com/Calvin-Gacheru/Uber-Price-Prediction.git](https://github.com/Calvin-Gacheru/Uber-Price-Prediction.git)
cd Uber-Price-Prediction
```

2. Microservices Orchestration via Docker Compose
Docker Compose will automatically parse the layout profiles, pull down the secure lightweight base Python footprints, implement the Astral UV package resolutions, and mount the private container network mesh.

Run this command from the root directory containing your docker-compose.yml file:

```bash
docker compose up --build
```

3. Accessing the Live Applications
Once the terminal logs stabilize and show active servers, the endpoints are live:

- Interactive Frontend Interface: Open your web browser and go to http://localhost:8501 to view the graphical ride estimation dashboard.
- Production REST API Gateway: Access http://localhost:8000 to interact with the raw backend.
- Interactive Swagger Documentation: Go to http://localhost:8000/docs to read structural payload schemas and run explicit endpoint test configurations.

##  Troubleshooting and Maintenance
- Port Collision Errors
If the application crashes with an error stating Port is already allocated, a background service is blocking port 8000 or 8501. Clear all active networks by running:

```bash
docker rm -f $(docker ps -aq)
docker compose up
```
- Stopping the Services
To safely tear down the active container structures without destroying build images, run:

```bash
docker compose down
```