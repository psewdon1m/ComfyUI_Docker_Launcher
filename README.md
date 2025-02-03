# Comfy UI Docker Launcher

## Overview
The **Comfy UI Docker Launcher** project is designed to simplify the process of running custom **Comfy UI** workflows via **Docker**. With this project, you can easily create isolated **Comfy UI** environments that include all your required versions of nodes, plugins, and libraries—without having to rebuild the original repository each time.

This solution also automates the installation of key dependencies such as **WSL, Ubuntu, and NVIDIA Toolkit**, making it ideal for users with a fresh system who may not have any prior experience with these tools.

## Features

### ✅ Isolated Docker Image Creation
- Creates an independent Docker image for each new instance, ensuring isolated and customizable environments.

### ✅ Automated Setup for Dependencies
- The installation process covers **WSL, Ubuntu, and NVIDIA Toolkit** (if applicable), making it easier for users on a clean system.

### ✅ Simplified Launch Process
- A launcher script and compiled executable streamline the process of starting and stopping the **Docker container**, logging output, and even opening your default web browser when the service is ready.

### ✅ User-Friendly Shortcuts
- Automatically generated shortcuts to commonly used directories (e.g., **models, output, workflows**) allow for quick access and management.

### ✅ Respect for Third-Party Licenses
- All intellectual property rights of third-party code, libraries, and plugins used in this project are fully respected. All license terms and conditions have been adhered to.

## Requirements
Before running the project, ensure that your system meets the following requirements:

- **Virtualization** must be enabled in your system BIOS settings
- **Operating System**: Windows (the project uses Windows-specific commands and libraries)
- **NVIDIA Drivers**: The latest version of **NVIDIA drivers** must be installed on the host machine
- **Docker**: Installed, configured, and logged in to Docker Desktop

## Installation

For correct operation, your system must have a working WSL with **NVIDIA Toolkit** installed. If you have already set up certain components (e.g., WSL, Ubuntu, or NVIDIA Toolkit), you may skip the corresponding steps and proceed to the next one.

### 📌 Clone the Repository
Open your terminal (or GitHub Desktop) and clone the repository:

```bash
git clone https://github.com/psewdon1m/ComfyUI_Docker_Launcher.git
cd ComfyUI_Docker_Launcher
```

### 📌 Install Required Components
The repository includes **automated scripts** to assist with the installation of all required dependencies, including:

1. **WSL (Windows Subsystem for Linux)**
2. **Ubuntu Linux distribution**
3. **NVIDIA Toolkit for GPU acceleration**

If these components are not installed, simply run the provided installation scripts located in the repository, and they will handle the setup process automatically.

### 📌 Install Required Components
The repository includes **automated scripts** to assist with the installation of all required dependencies, which **must be installed in the following order**:

1. **WSL (Windows Subsystem for Linux)**
2. **Ubuntu Linux distribution**
3. **NVIDIA Toolkit for GPU acceleration**

If these components are not installed, simply run the provided installation scripts located in the repository in the specified order, and they will handle the setup process automatically.

> ⚠ **Note:** During the installation process, **Docker may request user actions multiple times**. If prompted, make sure to select options like **"Restart with WSL integration"** or similar, depending on the exact request from Docker. These steps are crucial for proper setup and functionality.

### 📌 Configure the Project
The **main launcher script** will:
- Create a new directory with a timestamp.
- Copy the original **Comfy UI** repository (used as a template) into the new directory.
- Update the `docker-compose.yml` file with the correct paths and Docker image name.
- Build and tag the **Docker image**.
- Compile a **Python launcher script**
- Generate shortcuts for important folders (**models, output, workflows**).

### 📌 Launch the Application
Once the installation is complete, simply **run the generated executable** (e.g., `run_<timestamp>.exe`) to start the **Docker container** and launch **Comfy UI**. The executable will also:
- Open a command prompt displaying **Docker logs**
- Automatically open your **web browser** when the service is ready

## Usage

### ▶️ Starting the Service
- **Double-click** the generated executable to launch the Docker container.
- If the container is already running, the script will **stop it and restart as needed**.

**Note:** Each created **Comfy UI** project runs in its own isolated Docker environment, ensuring that different instances do not interfere with each other. All key elements remain independent, preventing conflicts between different setups.

### 🔗 Accessing the Application
- The application is accessible at **[http://127.0.0.1:8188](http://127.0.0.1:8188)**.
- Your **default browser** will open automatically once the service is up.

### 🛠️ Preinstalled Components

- ComfyUI Manager is preinstalled in this build, allowing easy management of nodes and extensions directly from the interface.

### 📂 Managing Files
- Shortcuts to the **models, output, and workflows** directories are created in the project folder for your convenience.
- These shortcuts can be **moved or copied** as needed.

### Related Projects

This project is based on and extends the functionality of the following repositories:

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - A powerful, modular UI framework for generative AI workflows

- [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) - A management tool for handling ComfyUI nodes and extensions

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
  - Verify that **prerequisites are installed**
  - Refer to the documentation for **Docker/WSL/NVIDIA Toolkit**

## License & Third-Party Rights
I do **not** claim any intellectual property rights over third-party **code, plugins, or libraries** used in this project. All rights and license terms from the original creators have been **fully respected and adhered to**.

## Contact

For questions, suggestions, or any other inquiries connect me via:

**Telegram:** [contact_psewdon1m](https://t.me/contact_psewdon1m)  

**Email:** [contact.psewdon1m@gmail.com](mailto:contact.psewdon1m@gmail.com)  

**GitHub:** [psewdon1m](https://github.com/psewdon1m)  
