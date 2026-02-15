# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will learn to build modern REST APIs using the FastAPI framework. You'll practice creating endpoints, handling HTTP methods, working with request/response models, and connecting to a database to build a fully functional backend application.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Create a new FastAPI project and set up the basic application structure with your first endpoint.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn web server using pip
- Create a basic FastAPI application instance
- Implement a root endpoint (`/`) that returns a welcome message
- Run the application locally and verify it works
- Access the automatic API documentation at `/docs`


### 🛠️ Task 2: Create CRUD Endpoints

#### Description
Build a complete set of Create, Read, Update, and Delete (CRUD) endpoints for managing a collection of items (e.g., tasks, books, or products).

#### Requirements
Completed program should:

- Create a POST endpoint to add new items to the collection
- Create a GET endpoint to retrieve all items
- Create a GET endpoint to retrieve a single item by ID
- Create a PUT endpoint to update an existing item
- Create a DELETE endpoint to remove an item
- Use appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Task 3: Implement Data Models

#### Description
Use Pydantic models to define the structure of your data and validate incoming requests.

#### Requirements
Completed program should:

- Define a Pydantic model for your item with at least 4 fields
- Include field validation (e.g., required fields, string length, value ranges)
- Create separate models for request and response data if needed
- Use type hints for all function parameters and return values
- Handle validation errors with appropriate error messages


### 🛠️ Task 4: Add Data Persistence

#### Description
Connect your API to a database or implement file-based storage to persist data between server restarts.

#### Requirements
Completed program should:

- Choose a storage method (SQLite, JSON file, or in-memory database)
- Store items persistently so data survives server restarts
- Implement proper error handling for database operations
- Ensure all CRUD operations work with the persistent storage
- Generate unique IDs for new items automatically
