# Greenhouse Gas Emissions

Backend API built with DRF (Django + Django Rest Framework) to manage annual greenhouse gas emissions data.  
Includes basic filtering, unit tests, and full Docker.

---

## How to Run Locally (Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/jpierre09/anthersis_greenhouse_gas_emissions.git
   cd greenhouse-emissions
   ```

2. Build and start containers:
   ```bash
   docker compose up --build
   ```

3. Once started, access the API at:  
   `http://localhost:8000/api/v1/emissions/`

---

## Environment Variables

The project requires a `.env` file at the root there is the .env.example included in the prohect

---

## Run Tests
To run the unit tests **inside the Docker container**, execute:

```bash
docker exec -it greenhouse_emissions_backend python manage.py test emissions_app
```

## API Endpoints

All endpoints support **GET** requests and return JSON data.

### Get all emissions
```http
GET /api/v1/emissions/
```



**Response:**
```json
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "emissions": 7.1,
      "emission_type": {
        "emission_code": "CO2",
        "description": "Carbon Dioxide"
      },
      "country": {
        "country_name": "Colombia",
        "country_code": "COL"
      },
      "activity": "Transportation",
      "year": 2021
    }
  ]
}
```

### Get emission by ID
```http
GET /api/v1/emissions/{id}/
```

---

## Deployment

To deploy the app:

1. Copy the `.env` file with variables.  
2. Run the project in detached mode:
   ```bash
   docker compose up --build -d
   ```

---

## Author

**Jean Pierre Londoño**  
jpierre09@gmail.com  
[GitHub](https://github.com/jpierre09)
