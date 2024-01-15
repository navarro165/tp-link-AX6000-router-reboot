# TP-Link AX6000 Router Reboot

## Introduction

This project provides a simple solution for remotely rebooting a TP-Link AX6000 router using Selenium and Docker. The project includes a `Dockerfile`, `docker-compose.yml`, and a Python script for rebooting the router.

## Prerequisites

Before using this project, ensure that you have Docker and Docker Compose installed on your machine.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/navarro165/tp-link-AX6000-router-reboot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd tp-link-AX6000-router-reboot
    ```

3. Open the `Dockerfile` and set the following environment variables with your router's information:

    ```Dockerfile
    ENV ROUTER_REBOOT_IP=your-routers-ip
    ENV ROUTER_REBOOT_USERNAME=your-username
    ENV ROUTER_REBOOT_PASSWORD=your-password
    ```

4. Save the changes to the `Dockerfile`.

5. Run the following commands to build and start the Docker containers:

    ```bash
    chmod +x reboot.sh
    ./reboot.sh
    ```

## Important Note

**Make sure to add the required environment variables (`ROUTER_REBOOT_IP`, `ROUTER_REBOOT_USERNAME`, and `ROUTER_REBOOT_PASSWORD`) to the `Dockerfile` before running the containers. Failure to do so will result in errors during execution.**

## References

- SeleniumHQ Docker Selenium - Quick Start
- Docker Python Official Image

Feel free to contribute to and enhance this project. Happy rebooting!
