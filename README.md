# software_architecture_mvp_backend
## Description
This repository contains the backend for my MVP project in the Software Architecture course at PUC-Rio. It's built with Python and Flask, providing RESTful API endpoints for user authentication, store management, and product handling. The backend uses SQLAlchemy for database management and is containerized with Docker.

## Installation Instructions

Download tar file from https://drive.google.com/drive/folders/1BsSmDIBcSMG6hxnN9cuVQA3H3luvr_HX?usp=drive_link

### Docker Setup
1. Build and run the Docker container:
    ```sh
    docker build -t jrpreneur-backend .
    docker run -p 3000:3000 jrpreneur-backend
    ```

## Usage Instructions
1. Run the backend server.
2. Run the frontend server.
3. Open the browser and navigate to `http://localhost:3000`.
