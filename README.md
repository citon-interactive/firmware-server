# firmware-server

This is the Citon firmware server repository. It contains the code and resources needed to build and deploy the firmware server for Citon devices. The server will likely be ran on a Raspberry Pi or similar device. and will serve firmware updates to Citon devices using OTA.

## File Structure

```
firmware-server
 ┣ deployment/
 ┣ docker/
 ┣ docs/
 ┣ scripts/
 ┣ src/
 ┣ tests/
 ┣ .env.example
 ┣ .gitignore
 ┣ Makefile
 ┣ README.md
 ┣ docker-compose.dev.yaml
 ┣ docker-compose.yml
 ┗ pyproject.toml
 ```

### Deployment
The `deployment` directory contains configuration files and scripts for deploying the firmware server.

### Docker
The `docker` directory contains Dockerfiles for building the firmware server image.

### Docs
The `docs` directory contains documentation related to the firmware server, including API documentation, architecture overview, and development guidelines.

### Scripts
The `scripts` directory contains utility scripts for setting up the development environment or other useful tools.

### Src
The `src` directory contains the main source code for the firmware server, organized into subdirectories for different modules and packages.

### Tests
The `tests` directory contains unit tests and mock servers for testing the firmware server functionality.

### .env.example
An example environment file that can be copied to `.env` and modified with actual configuration values.

### docker-compose.dev.yaml
A Docker Compose file for setting up a development environment with necessary services.

### docker-compose.yml
A Docker Compose file for deploying the firmware server and its dependencies.

### Makefile
A Makefile with common commands for building, testing, and running the firmware server.

### pyproject.toml
A configuration file for managing Python dependencies and project settings.

## Docs

The `docs` directory contains the following files:

- [API.md](./docs/API.md): Documentation for the firmware server API endpoints. It should be expanded with detailed descriptions of each endpoint, request/response formats, and examples.
- [ARCHITECTURE.md](./docs/ARCHITECTURE.md): An overview of the firmware server architecture, including diagrams and explanations of the main components and their interactions.
- [DEVELOPMENT.md](./docs/DEVELOPMENT.md): Guidelines for setting up a development environment, coding standards, and contribution guidelines.
- [CLIENT.md](./docs/CLIENT.md): Documentation for the MQTT communication between the firmware server and Citon devices, including message formats and topics.
- [DEPLOYMENT.md](./docs/DEPLOYMENT.md): Instructions for deploying the firmware server, including prerequisites, configuration steps, and troubleshooting tips.