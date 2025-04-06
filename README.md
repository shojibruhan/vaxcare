# VexCare
Your total vaccination soloution make by djago rest framework

# VaxCare API Documentation

## Introduction

VaxCare is a RESTful API built using Django REST Framework (DRF) for managing a vaccination campaign program. It provides endpoints for users (doctors and patients), bookings, campaigns, and reviews. JWT authentication is implemented using djoser, and API documentation is generated using drf-yasg (Swagger).

## Features

* **User Management:** Register and manage doctors and patients.
* **Booking Management:** Create, view, and manage vaccination bookings.
* **Campaign Management:** Create, view, and manage vaccination campaigns.
* **Review Management:** Submit and view reviews for campaigns.
* **JWT Authentication:** Secure API access using JSON Web Tokens (JWT).
* **Swagger Documentation:** Interactive API documentation for easy testing and exploration.

## Technologies Used

* **Django:** Python web framework.
* **Django REST Framework (DRF):** Toolkit for building Web APIs.
* **djoser:** REST implementation of Django authentication system.
* **drf-yasg:** Swagger/OpenAPI 2.0 and 3.0 spec generator for DRF.
* **JWT (JSON Web Tokens):** For authentication.

## Getting Started

### Prerequisites

* Python (3.7+)
* pip
* Virtual environment (recommended)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd VaxCare
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

### API Documentation

* Access the Swagger UI at `http://127.0.0.1:8000/swagger/` (or the appropriate address if you're using a different port or host).
* Access the ReDoc documentation at `http://127.0.0.1:8000/redoc/`.

## Environmental Variable
Create a `.env` file in the root directory and add the following:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=*
EMIL_HOST=your_email_host

```

### API Endpoints

#### Authentication

| Method | Endpoint              | Description              | Authentication |
| :----- | :-------------------- | :----------------------- | :------------- |
| POST   | `/auth/users/`        | Register a new user      | None           |
| POST   | `/auth/jwt/create/`   | Obtain a JWT token       | None           |
| POST   | `/auth/jwt/refresh/`  | Refresh a JWT token      | None           |

#### Users (Doctors & Patients)

| Method | Endpoint                    | Description                                  | Authentication |
| :----- | :-------------------------- | :------------------------------------------- | :------------- |
| GET    | `/users/`                   | List all users (admin only)                 | Admin Required |
| GET    | `/users/{id}/`               | Retrieve a specific user                     | User/Admin Required |
| PUT    | `/users/{id}/`               | Update a user                                | User/Admin Required |
| DELETE | `/users/{id}/`              | Delete a user (admin only)                   | Admin Required |
| POST   | `/doctors/`                 | Register a doctor (admin only)               | Admin Required |
| GET   | `/doctors/`                  | list all doctors. (admin/patient)            | optional       |
| GET   | `/doctors/{id}/`              | get specific doctor information. (admin/patient) | optional       |
| POST   | `/patients/`                | Register a patient (admin only)              | Admin Required |
| GET   | `/patients/`                 | list all patients. (admin/doctor)            | optional       |
| GET   | `/patients/{id}/`             | get specific patient information. (admin/doctor) | optional       |

#### Bookings

| Method | Endpoint             | Description                       | Authentication |
| :----- | :------------------- | :-------------------------------- | :------------- |
| POST   | `/bookings/`         | Create a new booking              | User Required  |
| GET    | `/bookings/`         | List all bookings (admin/doctor)  | Optional |
| GET    | `/bookings/{id}/`     | Retrieve a specific booking       | User/Admin/Doctor Required |
| PUT    | `/bookings/{id}/`     | Update a booking (admin/doctor)   | Admin/Doctor Required |
| DELETE | `/bookings/{id}/`    | Delete a booking (admin/doctor)   | Admin/Doctor Required |

#### Campaigns

| Method | Endpoint              | Description                      | Authentication |
| :----- | :-------------------- | :------------------------------- | :------------- |
| POST   | `/campaigns/`         | Create a new campaign (admin only) | Admin Required |
| GET    | `/campaigns/`         | List all campaigns               | Optional       |
| GET    | `/campaigns/{id}/`    | Retrieve a specific campaign     | Optional       |
| PUT    | `/campaigns/{id}/`    | Update a campaign (admin only)    | Admin Required |
| DELETE | `/campaigns/{id}/`   | Delete a campaign (admin only)   | Admin Required |

#### Reviews

| Method | Endpoint             | Description                   | Authentication |
| :----- | :------------------- | :---------------------------- | :------------- |
| POST   | `/reviews/`          | Create a new review           | User Required  |
| GET    | `/reviews/`          | List all reviews              | Optional       |
| GET    | `/reviews/{id}/`      | Retrieve a specific review    | Optional       |
| PUT    | `/reviews/{id}/`      | Update a review (user only)   | User Required |
| DELETE | `/reviews/{id}/`     | Delete a review (user only)   | User Required |

### Authentication

* All endpoints requiring authentication use JWT tokens.
* Include the `Authorization: Bearer <token>` header in your requests.

### Example Usage (using `curl`)

#### Obtaining a JWT token

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' [http://127.0.0.1:8000/auth/jwt/create/](http://127.0.0.1:8000/auth/jwt/create/)