# Comfy UI Docker Launcher

**Created by psewdon1m for the community!**

## Overview
The **Comfy UI Docker Launcher** project is designed to simplify the process of running custom **Comfy UI** workflows via **Docker**. With this project, you can easily create isolated **Comfy UI** environments that include all your required versions of nodes, plugins, and libraries—without having to rebuild the original repository each time.

This solution also automates the installation of key dependencies such as **Docker, WSL, Ubuntu, and NVIDIA Toolkit**, making it ideal for users with a fresh system who may not have any prior experience with these tools.

## Features

### ✅ Automated Docker Image Creation
- Creates an independent Docker image for each new instance, ensuring isolated and customizable environments.

### ✅ Automated Setup for Dependencies
- The installation process covers **Docker, WSL, Ubuntu, and NVIDIA Toolkit** (if applicable), making it easier for users on a clean system.

### ✅ Simplified Launch Process
- A launcher script and compiled executable streamline the process of starting and stopping the **Docker container**, logging output, and even opening your default web browser when the service is ready.

### ✅ User-Friendly Shortcuts
- Automatically generated shortcuts to commonly used directories (e.g., **models, output, workflows**) allow for quick access and management.

### ✅ Respect for Third-Party Licenses
- All intellectual property rights of third-party code, libraries, and plugins used in this project are fully respected. All license terms and conditions have been adhered to.

## Prerequisites
Before running the project, ensure that your system meets the following requirements:

- **Operating System**: Windows (the project uses Windows-specific commands and libraries)
- **Docker Desktop**: Installed and configured with **WSL2 integration**
- **WSL & Ubuntu**: The automated installation script will help set this up if not already installed
- **NVIDIA Toolkit**: *(Optional)* For users with **NVIDIA GPUs**; the installation script can install this as well
- **Internet Connection**: Required for downloading dependencies and Docker images

> **Note:** Even on a completely clean system (with no Python installed), the provided scripts are designed to guide you through the installation process.

## Installation

### 📌 Clone the Repository
Open your terminal (or GitHub Desktop) and clone the repository:

```bash
git clone https://github.com/your-username/comfy-ui-docker-launcher.git
cd comfy-ui-docker-launcher
```

### 📌 Run the Automated Installer
The project includes scripts to install and configure **Docker, WSL, Ubuntu, and the NVIDIA Toolkit** (if needed). Follow these steps:

#### 🚀 Docker Setup
1. Install **Docker Desktop** from [Docker's official website](https://www.docker.com/) and log in with your account.

#### 🚀 Automated WSL, Ubuntu, and NVIDIA Toolkit Setup
1. Run the provided installation scripts in the project directory.
2. These scripts will guide you through the setup process.
3. *(During the installation, Docker may prompt you to enable WSL integration—please follow those instructions.)*

### 📌 Configure the Project
The **main launcher script** will:
- Create a new directory with a timestamp.
- Copy the original **Comfy UI** repository (used as a template) into the new directory.
- Update the `docker-compose.yml` file with the correct paths and Docker image name.
- Build and tag the **Docker image**.
- Compile a **Python launcher script** into an executable with **PyInstaller**.
- Generate shortcuts for important folders (**models, output, workflows**).

### 📌 Launch the Application
Once the installation is complete, simply **run the generated executable** (e.g., `run_<timestamp>.exe`) to start the **Docker container** and launch **Comfy UI**. The executable will also:
- Open a command prompt displaying **Docker logs**
- Automatically open your **web browser** when the service is ready

## Usage

### ▶️ Starting the Service
- **Double-click** the generated executable to launch the Docker container.
- If the container is already running, the script will **stop it and restart as needed**.

### 🔗 Accessing the Application
- The application is accessible at **[http://127.0.0.1:8188](http://127.0.0.1:8188)**.
- Your **default browser** will open automatically once the service is up.

### 📂 Managing Files
- Shortcuts to the **models, output, and workflows** directories are created in the project folder for your convenience.
- These shortcuts can be **moved or copied** as needed.

## Troubleshooting & FAQ

### ❓ Docker Not Starting?
- Ensure **Docker Desktop** is running and that **WSL integration** is enabled.
- If you encounter errors, try **restarting Docker Desktop**.

### ❓ Permission Issues?
- Some commands may require **administrative privileges**.
- If you run into issues, try running the **terminal or scripts as an administrator**.

### ❓ Installation Errors?
- If an error occurs during the **automated installation process**, carefully **read the error message**.
- The error log often provides clues about what went wrong.
- You may need to:
  - Check your **internet connection**
  - Verify that **prerequisites are installed**
  - Refer to the documentation for **Docker/WSL/NVIDIA Toolkit**

### ❓ Need Further Assistance?
If you have any questions or issues that aren’t covered here, feel free to reach out through the **contact channels listed below**.

## License & Third-Party Rights
I do **not** claim any intellectual property rights over third-party **code, plugins, or libraries** used in this project. All rights and license terms from the original creators have been **fully respected and adhered to**.

## Contact
For questions, suggestions, or any other inquiries, you can reach me at:

📩 **Telegram:** [your Telegram handle]  
📸 **Instagram:** [your Instagram handle]  
🎨 **Behance:** [your Behance profile]  
🐙 **GitHub:** [your GitHub profile]  

---
**⭐ If you found this project helpful, consider giving it a star! ⭐**