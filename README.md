# 🐾 Pet Management API

A robust RESTful API for managing people and pets, built with Flask and SQLAlchemy, following Clean Architecture principles and best development practices.

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Design Patterns](#design-patterns)
- [Testing](#testing)
- [Error Handling](#error-handling)

## 🎯 About the Project

This project is a complete REST API that demonstrates the implementation of a well-defined layered architecture, separating responsibilities and facilitating maintenance and scalability. The system allows:

- ✅ Create and find people
- ✅ List and delete pets
- ✅ Relationship between people and their pets
- ✅ Data validation with Pydantic
- ✅ Robust error handling
- ✅ Unit and integration tests

## 🏗️ Architecture

The project follows a layered architecture inspired by Clean Architecture and MVC:

```
┌─────────────────────────────────────────┐
│          Routes (Flask)                 │
│  - person_routes.py                     │
│  - pets_routes.py                       │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│          Views Layer                    │
│  - person_creator_view.py               │
│  - person_finder_view.py                │
│  - pet_lister_view.py                   │
│  - pet_deleter_view.py                  │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│       Controllers Layer                 │
│  - PersonCreatorController              │
│  - PersonFinderController               │
│  - PetListerController                  │
│  - PetDeleterController                 │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│    Repositories Layer (Models)          │
│  - PeopleRepository                     │
│  - PetsRepository                       │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│       Database (SQLite)                 │
│  - people table                         │
│  - pets table                           │
└─────────────────────────────────────────┘
```

### Layers:

- **Routes**: Receives HTTP requests and delegates to Views
- **Views**: Validates data, calls Controllers and formats HTTP responses
- **Controllers**: Contains business logic
- **Repositories**: Abstracts database access
- **Models/Entities**: Defines table structure

## 🚀 Technologies Used

- **Python 3.x**
- **Flask** - Web framework
- **Flask-CORS** - CORS control
- **SQLAlchemy** - Database ORM
- **SQLite** - Database
- **Pydantic** - Data validation
- **Pytest** - Testing framework
- **mock-alchemy** - Mock for SQLAlchemy tests

## 📁 Project Structure

```
src/
├── main/
│   ├── routes/
│   │   ├── person_routes.py       # Person routes
│   │   └── pets_routes.py         # Pet routes
│   ├── composer/
│   │   ├── person_creator_composer.py
│   │   ├── person_finder_composer.py
│   │   ├── pet_deleter_composer.py
│   │   └── pets_lister_composer.py
│   └── server.py                  # Flask configuration
├── models/
│   └── sqlite/
│       ├── entities/
│       │   ├── people.py          # People model
│       │   └── pets.py            # Pets model
│       ├── repositories/
│       │   ├── people_repository.py
│       │   └── pets_repository.py
│       ├── interfaces/
│       │   ├── people_repository.py
│       │   └── pets_repository.py
│       └── settings/
│           ├── base.py
│           └── connection.py       # Connection manager
├── controllers/
│   ├── person_creator_controller.py
│   ├── person_finder_controller.py
│   ├── pet_deleter_controller.py
│   └── pet_lister_controller.py
├── views/
│   ├── person_creator_view.py
│   ├── person_finder_view.py
│   ├── pet_deleter_view.py
│   └── pet_lister_view.py
├── validators/
│   └── person_creator_validator.py
├── errors/
│   ├── error_handle.py
│   └── error_types/
│       ├── http_bad_request.py
│       ├── http_not_found.py
│       └── http_unprocessable_entity.py
└── views/
    └── http_types/
        ├── http_request.py
        └── http_response.py
```

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/pet-management-api.git
cd pet-management-api
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Initialize the database**
```bash
python init_db.py
```

5. **Run the application**
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## 📡 API Endpoints

### People

#### Create a Person
```http
POST /people
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "pet_id": 1
}
```

**Response (201 Created)**
```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {
      "first_name": "John",
      "last_name": "Doe",
      "age": 30,
      "pet_id": 1
    }
  }
}
```

#### Find a Person
```http
GET /people/{person_id}
```

**Response (200 OK)**
```json
{
  "data": {
    "type": "Person",
    "count": 1,
    "attributes": {
      "first_name": "John",
      "last_name": "Doe",
      "pet_name": "Rex",
      "pet_type": "dog"
    }
  }
}
```

### Pets

#### List All Pets
```http
GET /pets
```

**Response (200 OK)**
```json
{
  "data": {
    "type": "Pets",
    "count": 2,
    "attributes": [
      {
        "id": 1,
        "name": "Rex",
        "type": "dog"
      },
      {
        "id": 2,
        "name": "Whiskers",
        "type": "cat"
      }
    ]
  }
}
```

#### Delete a Pet
```http
DELETE /pets/{name}
```

**Response (204 No Content)**

### Error Responses

All errors follow a standard format:

**400 Bad Request**
```json
{
  "errors": [
    {
      "title": "Bad Request",
      "detail": "Invalid request parameters"
    }
  ]
}
```

**404 Not Found**
```json
{
  "errors": [
    {
      "title": "Not Found",
      "detail": "Person not found"
    }
  ]
}
```

**422 Unprocessable Entity**
```json
{
  "errors": [
    {
      "title": "Unprocessable Entity",
      "detail": "Validation error details"
    }
  ]
}
```

## 🎨 Design Patterns

### 1. Repository Pattern
Abstracts data access logic, making the code more testable and maintainable.

```python
class PeopleRepository(PeopleRepositoryInterface):
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        # Database access logic
```

### 2. Dependency Injection (Composer Pattern)
Uses composers to inject dependencies, facilitating testing and decoupling.

```python
def person_creator_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)
    return view
```

### 3. MVC (Model-View-Controller)
Clear separation between data (Model), presentation (View), and business logic (Controller).

### 4. Interface Segregation
Uses abstract interfaces to define contracts between layers.

```python
class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass
```

## 🧪 Testing

The project includes comprehensive unit and integration tests.

### Run all tests
```bash
pytest
```

### Run with coverage
```bash
pytest --cov=src tests/
```

### Run specific test file
```bash
pytest tests/test_pets_repository.py
```

### Test Structure

- **Unit Tests**: Mock database connections to test logic in isolation
- **Integration Tests**: Test actual database interactions (marked with `@pytest.mark.skip`)
- **Validation Tests**: Test data validation with Pydantic

Example of mocked test:
```python
def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()
    
    assert response[0].name == 'dog'
```

## 🛡️ Error Handling

The application has a centralized error handling system:

### Custom Exceptions
- `HttpBadRequestError` (400)
- `HttpNotFoundError` (404)
- `HttpUnprocessableEntityError` (422)

### Error Handler
```python
def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            status_code=error.status_code,
            body={'errors': [{'title': error.name, 'detail': error.message}]}
        )
    
    # Generic errors return 500
    return HttpResponse(
        status_code=500,
        body={'errors': [{'title': 'Internal Server Error', 'detail': str(error)}]}
    )
```

## 🔄 Data Validation

Uses Pydantic for robust data validation:

```python
class BodyData(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    age: int
    pet_id: int
```

## 🗃️ Database

### Schema

**people**
- id (BIGINT, PK, Auto Increment)
- first_name (VARCHAR(100), NOT NULL)
- last_name (VARCHAR(100), NOT NULL)
- age (BIGINT, NOT NULL)
- pet_id (BIGINT, FK → pets.id, NULLABLE)

**pets**
- id (BIGINT, PK, Auto Increment)
- name (VARCHAR(100), NOT NULL)
- type (VARCHAR(100), NOT NULL)

### Relationships
- A person can have one pet (1:1 optional)
- A pet can belong to multiple people (1:N)

## 🚀 Best Practices Implemented

- ✅ **Clean Architecture**: Clear separation of concerns
- ✅ **SOLID Principles**: Especially SRP, OCP, DIP
- ✅ **Type Hints**: Python typing for better code documentation
- ✅ **Error Handling**: Centralized and consistent
- ✅ **Data Validation**: Using Pydantic
- ✅ **Testing**: Unit and integration tests with mocks
- ✅ **Database Transactions**: Proper commit/rollback handling
- ✅ **Context Managers**: Safe resource management
- ✅ **Interface Segregation**: Abstract base classes defining contracts

## 📝 Requirements

```txt
Flask==2.3.0
Flask-CORS==4.0.0
SQLAlchemy==2.0.0
Pydantic==2.0.0
pytest==7.4.0
mock-alchemy==0.2.6
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**

- GitHub: [manoeldr](https://github.com/manoeldr)
- LinkedIn: [Manoel Antonio][(https://www.linkedin.com/in/manoel-antonio-dutra-rodrigues-98b390202/)]

## 🙏 Acknowledgments

- Clean Architecture principles by Robert C. Martin
- Flask documentation and community
- SQLAlchemy ORM
- Python community

---

⭐ If you found this project helpful, please consider giving it a star!
