# Event Analytics Hub Ingest Service

This repository contains the Flask-based ingest service for the [Event Analytics Hub](https://blog.nick.shimokochi.com/post/building-an-event-analytics-hub-a-journey-in-software-development) project, which demonstrates a scalable, event-driven analytics platform. The ingest service accepts and validates incoming data, stores it in a database, and triggers downstream processing workflows.

---

## **Overview**

The ingest service plays a critical role in the **Event Analytics Hub** by:

- Providing a RESTful API for data ingestion.
- Validating incoming data against predefined schemas.
- Storing validated data in a PostgreSQL database.
- Publishing messages to AWS SNS/SQS to trigger downstream workflows.

This repository includes application code, configuration files, a GitHub Action for CI/CD, and Docker Compose for local testing and development.

---

## **Repository Structure**

### **1. Application Code**

#### Key Files and Directories:

- **`server/`**:
  Houses the main Flask RestX application and supporting modules.

### **2. Testing**

#### Key Files:

- **`tests/`**:
  Contains pytest cases to verify the functionality of the ingest service.

  - **`tests/conftest.py`**:
    Sets up test fixtures, including a test database.

  - **`tests/functionaltests/test_health.py`**:
    Verifies the health of the application.

  - **`tests/functionaltests/test_ingest.py`**:
    Tests the data ingestion functionality.

### **3. CI/CD Workflow**

#### Key File:

- **`.github/workflows/build-and-test.yml`**:
  Automates testing, building, and publishing Docker images.

  Key Steps:

  - **Build Container & Tests**: the `validate` job executes pytest cases to validate functionality.

  - **Push final artifact**: `push_to_registry` pushes our image to DockerHub upon successful merge to main

### **4. Local dev and testing**

#### Key Files:

- **`docker-compose.yaml`**:
  Defines the containerized environment for running the Flask application and PostgreSQL locally; note that a `.env` file must be present in your local repo, defining the test database password and image tag, e.g.

  ```
    POSTGRES_PASSWORD=sometestdbpassword
    IMAGE_TAG=local
  ```

  To run the tests, simply install Docker Compose and run `docker compose up`.

---

## **License**

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
