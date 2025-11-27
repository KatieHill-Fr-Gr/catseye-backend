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


```
class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'profile_img': user.profile_img,
            'job_title': user.job_title,
            'team': {
                'id': user.team.id if user.team else None,
                'name': user.team.name if user.team else None,
            }
        }
        return token
```

Since the app is intended for business use, most of the routes require authentication. I applied Permission Classes to control access across the app, allowing unrestricted access to the homepage and signup routes only:

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

#### 2) Data Models & Views

I created separate Django apps for each data entity and defined the models, including their relationships using Foreign Keys and related names: 

- users
- teams
- projects
- tasks
- source_texts
- translations
- termbases

```
class Task(models.Model):

    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('review', 'Under Review'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    deadline = models.DateField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='in_progress')

    parent_project = models.ForeignKey(to='projects.Project', on_delete=models.SET_NULL, null=True, blank=True, related_name='project_tasks')
    assigned_to = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    source_text = models.ForeignKey(to='source_texts.Source', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    translation = models.ForeignKey(to='translations.Translation', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
```

For the API layer, I used Django REST Framework’s generic views wherever possible to speed up development and keep the codebase clean:


```
class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.select_related('team', 'owner').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedProjectSerializer
        return ProjectSerializer 

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.select_related('team', 'owner').all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedProjectSerializer 
        return ProjectSerializer
```

#### 3) Serializers

Given the multiple relationships between models, it was important to manage how the data was exposed through the API to avoid multiple API calls on the frontend. I designed nested and populated serializers for the projects and tasks (associated with teams, users, source texts, and translations):  

```
class PopulatedProjectSerializer(ProjectSerializer):
    owner = OwnerSerializer()
    team = TeamSerializer()

    class Meta(ProjectSerializer.Meta):
        fields = ['id', 'name', 'brief', 'deadline', 'images', 'status', 'owner', 'team']
```

I also used select_related to combine queries into a single more complex query to boost performance when accessing related data in the database. 


#### 4) Nested Routes

Instead of creating standalone endpoints for the tasks, I structured them under the project routes since the tasks can only belong to one project: 

```
urlpatterns = [
    path('', ProjectListView.as_view()),
    path('<int:pk>/', ProjectDetailView.as_view()),
    path('<int:pk>/tasks/', TaskListView.as_view()),
    path('<int:pk>/tasks/<int:task_pk>/', TaskDetailView.as_view()),
    path('<int:pk>/team-users/', ProjectTeamUsersView.as_view()),
    path('user-team-projects/', UserTeamProjectsView.as_view()),
    path('user-tasks/', UserTasksView.as_view()), 
]
```

I decided to keep the sources texts, translations, and termbases separate so that these could be accessed by multiple projects and tasks. Overall, this approach helped to make it clear how resources are accessed and kept the API design clean and intuitive. 


## Challenges


#### 1) Refresh Token 

When generating a new Token, the custom serializer settings were ignored and a standard token was generated without the user information in the payload.

The solution was to manually generate the Token with `TokenSerializer.get_token(serialized_user.instance)`:

```
class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialized_user = AuthSerializer(data=request.data)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        print(serialized_user.data)

        refresh = TokenSerializer.get_token(serialized_user.instance)

        return Response({
             'access': str(refresh.access_token)
            }, 201)
```

#### 2) User Profile Update

The user’s team was not returned correctly in the update profile response so I changed the OwnerSerializer and TokenSerializer to include the full team object (including the id and the name): 

```
class OwnerSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), required=False, allow_null=True)
    team_info = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'job_title', 'profile_img', 'team', 'team_info']

    def get_team_info(self, obj):
        if obj.team:
            return {
                'id': obj.team.id,
                'name': obj.team.name
            }
        return None
```

#### 3) Task Statuses

To update the task statuses via the drag-and-drop functionality of the Kanban board, I modified the `TaskDetailView` to support partial updates. This means that the status field is updated on the backend without the need to include the other required fields in the request. 

Whenever a task is moved to a different column on the board (e.g. from “Review” to “Done”), its status is persisted in the database and remains consistent with the frontend state. 

```
class TaskDetailView(RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PopulatedTaskSerializer
        return TaskSerializer 

    lookup_field = 'pk'
    lookup_url_kwarg = 'task_pk'

    def get_queryset(self):
        project_pk = self.kwargs['pk']
        get_object_or_404(Project, pk=project_pk) 
        return Task.objects.filter(parent_project_id=project_pk)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
```

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

To do this, I added helper functions to connect to the DeepL client and store it in a variable (the "lazy-singleton" pattern to avoid making multiple calls to the API). A new translations endpoint `/auto-translate` and corresponding View have also been implemented to allow users to submit texts for translation. The source texts are converted from JSON objects to strings so that they can be processed by the translation API. The response is then returned as JSON again — preserving the original format for reinjection into the Lexcial editor on the frontend:

```
class AutoTranslateView(APIView):
    def post(self, request):
        source_id = request.data.get('source_id')
        target_lang = request.data.get('target_lang')

        if not source_id or not target_lang:
            return Response(
                {'error': 'Missing text or target-lang'},
                 status=400
            )
        
        source_obj = get_object_or_404(Source, id=source_id)

        try: 
            translated_json = translate_lexical_json(source_obj.body, target_lang)
            
            return Response({
                'translated_text': translated_json,
                'original': source_obj.body
            })
        except json.JSONDecodeError:
            return Response(
                {'error': 'Invalid JSON format'},
                status=400
            )
```
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


