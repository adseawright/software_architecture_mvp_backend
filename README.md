# JrPreneur Backend API
## About
The JrPreneur Backend API is the main service of the JrPreneur application, designed to facilitate various operations such as user registration, product management, store operations, and order handling. This service is built using Flask, with a SQLlite database for data persistence.

## Endpoints
### User Registration
This endpoint is used for registering new users in the system.

Route: /register
HTTP Method: POST
username: String - The username for the new user.
email: String - The email address of the new user.
password: String - The password for the new user.

### User Login
This endpoint handles user authentication by verifying email and password.

Route: /login
HTTP Method: POST
Authentication: Required for subsequent requests after login.
email: String - The registered email address of the user.
password: String - The password of the user.

### Profile Management
This endpoint allows the retrieval and updating of a user’s profile, including store information.

Route: /profile
HTTP Method: GET, PUT
Authentication: JWT token required.
Authorization: User must be the owner of the profile to make updates.

Operations:
GET: Retrieve profile and associated store details.
PUT: Update user profile and store details.

### Product Management
Endpoints to handle CRUD operations for products within a store.

Route: /products
HTTP Method: POST, GET, PUT, DELETE
Authentication: JWT token required.
Authorization: User must be the owner of the store to manage products.

Operations:
POST: Create a new product in the store.
GET: Retrieve a list of products in the store.
PUT: Update an existing product.
DELETE: Remove a product from the store.

### Order Management
Endpoints to handle the placing and management of orders.

Route: /order
HTTP Method: POST, GET
Authentication: JWT token required.
Authorization: User must be authenticated to place or view orders.
Operations:
POST: Place a new order.
GET: Retrieve the status and details of an existing order.

### Technical Description
The JrPreneur Backend API is implemented as a Flask-based web service, utilizing SQLlite to persist data.

### Technologies:
Backend Framework: Flask
Database: SQLlite
Authentication: JWT for secure user sessions

### Dependencies:
Flask
SQLAlchemy
Flask-Migrate
Flask-CORS
Flask-JWT-Extended

## Docker
The application is containerized using Docker. Below are the instructions to build and run the service.

Dockerfile: The Dockerfile is located at the root of the backend directory.

Docker Compose: Utilize Docker Compose to set up the backend service alongside its dependencies.
