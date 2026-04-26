# Attendance-Management-API

A lightweight FastAPI-based backend system designed for attendance tracking and role-based user management.

## Tech Stack
- **Framework:** FastAPI
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Security:** Bcrypt (Password Hashing)
- **Validation:** Pydantic

## Features
- **User Management:** Create new users with role-based access.
- **Secure Auth:** Password hashing implemented using bcrypt.
- **Database Integration:** MySQL with SQLAlchemy for ORM.
- **Error Handling:** Proper status codes (201 for success, 400 for existing emails).

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/aishwaryasingh203/Attendance-Management-API
   cd Attendance-Management-API

2. Setup Virtual Environment:
    
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies:
    
    pip install -r requirements.txt

4. Environment Variables:

    Create a .env file in the root directory:
    DATABASE_URL=mysql+pymysql://root:password@localhost:3306/skillbridge_db

5. Run the Server:
    
    uvicorn src.main:app --reload


**Honest Assessment (Submission Status)**

**What is fully working:**

-User registration and login endpoints with JWT authentication.

-Password hashing using bcrypt for secure storage.

-Database connection with MySQL and SQLAlchemy.

-Input validation for user creation using Pydantic models.

**What is partially done / Pending:**

-Full test coverage for all edge cases is currently in progress.

-Bulk data management features are kept for future iterations to ensure core stability.

**What I found most challenging:**

-Setting up the MySQL integration and managing database integrity constraints while ensuring the authentication  flow remains secure.

**One thing I would do differently with more time:**

-I would implement asynchronous task processing for generating attendance reports to improve API response time and add comprehensive unit tests for all service layers.

API documentation and testing interface are available at: https://attendance-management-api-production.up.railway.app//docs
