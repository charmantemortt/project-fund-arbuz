# Arbuz Backend 

This project is a backend for a children's aid fund. It includes APIs for managing news, projects, and donation forms. The project runs via Docker and provides API documentation via Swagger.

# Projects:

CRUD projects.

Each project contains a name, description and image.

# Donation form:

Ability to specify the donation amount, payment type (one-time or monthly), username, comment and link status.

Support for creating donations via API.

# News:

CRUD news.

Each news contains a name, description and creation date.

# Installation and launch:
1. Clone this repository
    ```bush
    Copy 
   https://github.com/charmantemortt/project-fund-arbuz
   
2. Build & launch containers: \
   `docker compose up --build`
3. For stop:\
`docker compose down`

# Swagger UI
API documentation is available via Swagger UI at: \
`http://localhost:8000/swagger/`

# Check Project, News:
Copy: \
`GET /api/projects/`
\
`GET /api/news/`

# Create new project, news, form:
Copy: \
`POST /api/projects/` 
\
`POST /api/news/`
\
`POST /api/forms/`

# Body request:
```bush
{
  "name": "Name",
  "description": "Description",
  "image": "image URL"
}

{
  "name": "name",
  "description": "description"
}

{
  "sum": 100.0,
  "pay_status": "one-time",
  "user_name": "name",
  "comment": "text",
  "link_status": "yes",
  "link_field": "https://example.com"
}
```

# Project Structure
## Models:

- `Project`: Foundation projects.

- `Forms`: Donation form.

- `News`: Foundation news.

## ViewSets:

- `ProjectViewSet`: Project management.

- `FormsViewSet`: Donation form management.

- `NewsViewSet`: News management.

## Swagger:

API documentation is available via `drf-yasg`.
