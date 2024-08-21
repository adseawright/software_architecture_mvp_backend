# JrPreneur Backend API

## About
The JrPreneur Backend API is the core service of the JrPreneur application. It handles key operations such as user registration, product management, store operations, and order processing. The service is built using Flask and persists data using SQLite.

## Endpoints

### User Registration
This endpoint is used to register new users in the system.

- **Route**: `/register`
- **HTTP Method**: `POST`
- **Payload**:
  - `username` (String): The username for the new user.
  - `email` (String): The email address of the new user.
  - `password` (String): The password for the new user.
- **Response**:
  - Returns a JWT token and the user's unique ID upon successful registration.

### User Login
This endpoint handles user authentication by verifying email and password.

- **Route**: `/login`
- **HTTP Method**: `POST`
- **Payload**:
  - `email` (String): The registered email address of the user.
  - `password` (String): The password of the user.
- **Response**:
  - Returns a JWT token and the user's unique ID upon successful login.

### Profile Management
This endpoint allows the retrieval and updating of a user’s profile, including store information.

- **Route**: `/profile`
- **HTTP Methods**: `GET`, `PUT`
- **Authentication**: JWT token required.
- **Operations**:
  - `GET`: Retrieve profile and associated store details.
  - `PUT`: Update user profile and store details.

### Product Management
Endpoints to handle CRUD operations for products within a store.

- **Route**: `/products`
- **HTTP Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Authentication**: JWT token required.
- **Operations**:
  - `POST`: Create a new product in the store.
  - `GET`: Retrieve a list of products in the store.
  - `PUT`: Update an existing product.
  - `DELETE`: Remove a product from the store.

### Store Management
Endpoints to handle the creation, retrieval, updating, and deletion of stores.

- **Route**: `/stores`
- **HTTP Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Authentication**: JWT token required.
- **Operations**:
  - `POST`: Create a new store.
  - `GET`: Retrieve a list of stores owned by the user.
  - `PUT`: Update the details of an existing store.
  - `DELETE`: Remove a store.

### Order Management
Endpoints to handle the placing and management of orders, integrated with PayPal for payment processing.

- **Route**: `/order`
- **HTTP Methods**: `POST`, `GET`
- **Authentication**: JWT token required.
- **Operations**:
  - `POST`: Place a new order.
  - **PayPal Integration**: The order placement interacts with the PayPal API to create payment orders and handle the payment process.
  - `GET`: Retrieve the status and details of an existing order.

## PayPal Integration
The `order.py` module integrates with the PayPal API to handle secure payment processing:

- **PayPalClient Class**:
  - Manages the retrieval of an access token from PayPal using the client credentials.
  - Ensures tokens are refreshed when they expire.
  - Handles the creation of payment orders and captures payments.

- **Environment Variables**:
  - `PAYPAL_CLIENT_ID`: Your PayPal client ID.
  - `PAYPAL_CLIENT_SECRET`: Your PayPal client secret.
  
  Ensure these are set in your `.env` file.

- **Endpoints**:
  - The PayPal API is utilized within the `/order` endpoint to create and manage payment orders.

## Technical Description
The JrPreneur Backend API is implemented as a Flask-based web service with an SQLite database for data persistence.

### Technologies
- **Backend Framework**: Flask
- **Database**: SQLite
- **Authentication**: JWT for secure user sessions
- **External API**: PayPal API for payment processing

### Dependencies
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-CORS
- Flask-JWT-Extended
- Requests (for PayPal API integration)

## Docker
The application is containerized using Docker. Below are the instructions to build and run the service.

- **Dockerfile**: The Dockerfile is located at the root of the backend directory.
- **Docker Compose**: Utilize Docker Compose to set up the backend service alongside its dependencies.
