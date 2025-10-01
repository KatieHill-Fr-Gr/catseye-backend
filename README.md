# Catseye - A CAT tool & project management app in one
by Katie Hill 


*Screenshot of homepage*


## Tech stack

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/react/react-original-wordmark.svg"
  alt=“React” width="40" height="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg"
  alt=“Python” width="40" height="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg"
  alt=“Django” width="40" height="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/djangorest/djangorest-original-wordmark.svg"
  alt=“DjangoRESTFramework” width="40" height="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-plain-wordmark.svg"
alt=“PostgreSQL” width="40" height="40" />

## Timeframe

- **Duration** 7 days
- **Team** This was a solo project
- **Skills** Backend development in Python Django, RESTful API design & implementation with Django REST Framework, PostgreSQL database management (Neon)



## About

Catseye is a translation and project management app intended for business users who create and manage multilingual content. In my previous roles as a translator and copywriter, I used many CAT (Computer Assisted Translation) and workflow management tools that had clunky and outdated UIs. I wanted to design and build an agile and streamlined app that combined these functionalities in a simple and intuitive way, while also fostering collaboration between teams.

This was my final project on the General Assembly Software Engineering Bootcamp. Our brief was to develop a full-stack application using a Python Django API and PostgreSQL for data management. These technologies are ideal for data-heavy apps like translation tools, which rely on structured data and complex relationships. Combining this with workflow management (projects and tasks) made this a challenging build. However, I managed to deliver a Minimum Viable Product (MVP) by the deadline and have since continued to fix bugs and work on additional features.

The API is live at this link: https://catseye-ai-1d2038dfccf2.herokuapp.com/admin/login/?next=/admin/

## Installation

For the backend, clone this repository and install the following packages: 


```bash
pipenv install django
pipenv install django-environ
pipenv install djangorestframework
```

**Database**

```bash
pipenv install psycopg2-binary
```

**Frontend**

```bash
pipenv install django-cors-headers
```

**Optional Formatting**
```bash
pipenv install autopep8
```

## Planning 

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/trello/trello-plain-wordmark.svg" 
	alt="Trello" width="80" height="60" />

This project required multiple interconnected datasets so I started by planning these relationships before defining the endpoints (including nested routes for the project tasks): 

#### 1) Relationships


<img width="1083" height="798" alt="Catseye_ERD" src="https://github.com/user-attachments/assets/befe3140-fda4-4623-bc81-fabe32ef7fd6" />


#### 2) Routing

<img width="763" height="647" alt="Catseye_RoutingChart" src="https://github.com/user-attachments/assets/95cd8550-cb2f-497c-a838-3da5d5ae719d" />

<img width="786" height="656" alt="Catseye_RoutingChart1" src="https://github.com/user-attachments/assets/1943ece1-d45c-4d0d-9b86-7423db4f3c2c" />

<img width="858" height="714" alt="Catseye_RoutingChart2" src="https://github.com/user-attachments/assets/3218b424-ab5a-411b-b270-d4f4bb7e10fb" />

Finally, I created a Trello board to plan and manage my tasks throughout the week and keep all the reference materials in one place.


## Build





## Challenges


#### 1) Refresh Token 

When generating a fresh token, the specific settings included in the serializer were ignored and a standard token was generated instead (without the user information). 

The solution was to manually generate the token with `TokenSerializer.get_token(serialized_user.instance)` to include the user in the payload:


<img width="629" height="305" alt="Catseye_RefreshTokenFix" src="https://github.com/user-attachments/assets/ed3769a7-88fd-4edc-9052-1bee9c877141" />


#### 2) User Profile Update

The user’s team was not returned correctly in the update profile response so I changed the OwnerSerializer and TokenSerializer to include the full team object (including the id and name): 


<img width="632" height="293" alt="Catseye_UserTeamSerializerFix" src="https://github.com/user-attachments/assets/1ff7f7e6-6065-4dab-87e5-97275343cb55" />




