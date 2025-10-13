# Catseye - A CAT tool & project management app in one
by Katie Hill 

<img width="1449" height="923" alt="Catseye_homepage" src="https://github.com/user-attachments/assets/d81b85f0-fda7-45d7-b45c-3d3f218ec65e" />

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


## Build

#### 1) User Authentication 

I implemented JWT authentication, manually extending the Access Token Lifetime in the project settings. I then created custom AuthSerializer and TokenSerializer classes to manage user authentication: 


<img width="635" height="375" alt="Catseye_TokenSerializer" src="https://github.com/user-attachments/assets/42839312-e03c-41fc-a537-da7c2e7366ba" />


Since the app is intended for business use, most of the routes require authentication. I applied Permission Classes to control access across the app, allowing unrestricted access to the homepage and signup routes only:

<img width="630" height="202" alt="Catseye_RESTFrameworkAuth" src="https://github.com/user-attachments/assets/0fe359e5-ee1a-4742-b6c9-c069d0b08971" />


#### 2) Data Models & Views

I created separate Django apps for each data entity and defined the models, including their relationships using Foreign Keys and related names: 

- users
- teams
- projects
- tasks
- source_texts
- translations
- termbases

<img width="1042" height="476" alt="Catseye_TaskModel" src="https://github.com/user-attachments/assets/246d5da4-1eb5-4b77-a71b-a1e112a65abb" />


For the API layer, I used Django REST Framework’s generic views wherever possible to speed up development and keep the codebase clean:


<img width="1040" height="337" alt="Catseye_GenericViews" src="https://github.com/user-attachments/assets/1d84a795-faae-45d0-8fce-b7a6dc0e4642" />


#### 3) Serializers

Given the multiple relationships between models, it was important to manage how the data was exposed through the API to avoid multiple API calls on the frontend. I designed nested and populated serializers for the projects and tasks (associated with teams, users, source texts, and translations):  

<img width="1043" height="192" alt="Catseye_NestedSerializers" src="https://github.com/user-attachments/assets/56b4b1a9-110f-4e0e-bd09-1a5b14541538" />

I also used select_related to combine queries into a single more complex query to boost performance when accessing related data in the database. 


#### 4) Nested Routes

Instead of creating standalone endpoints for the tasks, I structured them under the project routes since the tasks can only belong to one project: 

<img width="1044" height="226" alt="Catseye_NestedRoutes" src="https://github.com/user-attachments/assets/a3a1e97f-042a-4f5f-b99b-4b1b5ebbc2c1" />


I decided to keep the sources texts, translations, and termbases separate so that these could be accessed by multiple projects and tasks. Overall, this approach helped to make it clear how resources are accessed and kept the API design clean and intuitive. 


## Challenges


#### 1) Refresh Token 

When generating a new Token, the custom serializer settings were ignored and a standard token was generated without the user information in the payload.

The solution was to manually generate the Token with `TokenSerializer.get_token(serialized_user.instance)`:

<img width="629" height="305" alt="Catseye_RefreshTokenFix" src="https://github.com/user-attachments/assets/ed3769a7-88fd-4edc-9052-1bee9c877141" />


#### 2) User Profile Update

The user’s team was not returned correctly in the update profile response so I changed the OwnerSerializer and TokenSerializer to include the full team object (including the id and the name): 

<img width="1038" height="316" alt="Catseye_UserTeamSerializerFix" src="https://github.com/user-attachments/assets/c2a682e4-5f75-4ba2-bda3-7d13f610244a" />


#### 3) Task Statuses

To update the task statuses via the drag-and-drop functionality of the Kanban board, I modified the `TaskDetailView` to support partial updates. This means that the status field is updated on the backend without the need to include the other required fields in the request. 

Whenever a task is moved to a different column on the board (e.g. from “Review” to “Done”), its status is persisted in the database and remains consistent with the frontend state. 

<img width="1042" height="354" alt="Catseye_TaskDetailView" src="https://github.com/user-attachments/assets/7bb5fd50-730a-49a3-854b-e080aa22db23" />


## Wins

- Designed & implemented a clear URL structure with nested routes
- Developed reusable generic views and serializers to avoid duplicating code
- Used nested serializers to limit frontend API calls and the `select_related` method to optimise database queries
- Successfully implemented JWT authentication and strict access control with permission classes


## Key Learnings

- Gained a solid understanding of Django ORM by modelling multiple related entities and managing database interactions efficiently.
- Developed DRF serializers (including nested and custom serializers) to convert complex model instances into JSON responses.
- Implemented nested API routes and a combination of generic and custom views to create a clean, scalable, and maintainable API.


## Bugs

##### Sign up

The TokenSerializer includes the full user object which causes issues on the frontend when the new user payload exceeds the size limit for JWTs. A solution is currently being implemented to store only the user ID in the JWT and create a new endpoint (`CurrentUserView`). 


## Future Improvements

#### 1) AI Integration

I’m currently integrating the DeepL translation API to enable automated translation within the app. I looked into potential proxy options (e.g. using Netlify functions) but decided to use my Django REST API to handle translation requests for simplicity.

A new translation endpoint `/api/translation` and corresponding DRF Serializer and View will be implemented to allow users to submit texts for translation.The backend then sends the request to the third-party API and returns the output to the frontend. 

#### 2) Custom Error-Handling

When login fails, the generic error from `rest_framework_simplejwt` is currently displayed in the UI. Custom-error handling should be implemented on the backend with an additional `CustomTokenObtainSerializer` and a `LoginView(APIView)` to provide more information for the user. 

#### 3) Role-Based Permissions

Users are currently only able to access projects associated with their team. However, there is no restriction on who can create, edit and delete the team’s projects or any of the resources. More granular permissions may be more appropriate so that project owners and contributors have different access levels. 

#### 4) Search & Filtering

Advanced filtering and search options would allow users to access resources more quickly (e.g. search for a specific task, text or translation). 


#### 5) Multi-Tenancy Support

To allow different organisations to use the app, individual environments would need to be set up with separate schemas and databases (and a `tenant_id` on each model). 


#### 6)  Supported Languages

The language options for the source texts and translations are hardcoded in the Django data models. These could be extended or made available to edit on the frontend to allow more flexibility.  


#### 7) Text Analysis

The Lexical text editor has a wordcount (which is useful for marketing texts that have a character limit such as email subject lines, sponsored articles, and Facebook Ads, etc.). However, it would also be good to include additional text analysis features to allow users to evaluate translation quality and manage terminology.


