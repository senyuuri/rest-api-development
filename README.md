# rest-api-development

CS5331 Assignment 1 Project Reference Repository

## [Temporary] Development Environemnt Setup
1. Create a virtualenv and install necessary packages
```
> virtualenv -p python3.5 pyenv
> source pyenv/bin/activate
> pip install -r requirements.txt
```

2. Setup django
```
> python manage.py migrate
> python manage.py createsuperuser
```

3. Run local server
```
> python manage.py runserver
```

## Instructions


## Grading

The implementation will be graded in an automated fashion on an Ubuntu 16.04
virtual machine by building the docker container found in your repository and
running it. The grading script will interact with your API.

The following ports are expected to be accessible:

1. 80, on which static HTML content, including the front-end, is served.
2. 8080, on which the API is exposed.

To verify this, please run the following commands:

```
sudo ./run.sh
```

On a different window:

```
curl http://localhost:80
curl http://localhost:8080
```

If a response is received, you're good to go.

**Please replace the details below with information relevant to your team.**

## Screenshots

Please replace the example screenshots with screenshots of your completed
project. Feel free to include more than one.

![Sample Screenshot](./img/samplescreenshot.png)

## Administration and Evaluation

Please fill out this section with details relevant to your team.

### Team Members

1. Member 1 Name
2. Member 2 Name
3. Member 3 Name
4. Member 4 Name

### Short Answer Questions

#### Question 1: Briefly describe the web technology stack used in your implementation.

Answer: Please replace this sentence with your answer.

#### Question 2: Are there any security considerations your team thought about?

Answer: Please replace this sentence with your answer.

#### Question 3: Are there any improvements you would make to the API specification to improve the security of the web application?

Answer: Please replace this sentence with your answer.

#### Question 4: Are there any additional features you would like to highlight?

Answer: Please replace this sentence with your answer.

#### Question 5: Is your web application vulnerable? If yes, how and why? If not, what measures did you take to secure it?

Answer: Please replace this sentence with your answer.

#### Feedback: Is there any other feedback you would like to give?

Answer: Please replace this sentence with your answer.

### Declaration

#### Please declare your individual contributions to the assignment:

1. Member 1 Name
    - Integrated feature x into component y
    - Implemented z
2. Member 2 Name
    - Wrote the front-end code
3. Member 3 Name
    - Designed the database schema
4. Member 4 Name
    - Implemented x

