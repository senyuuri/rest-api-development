# rest-api-development

CS5331 Assignment 1 Project Reference Repository

## Instruction
Make sure you have docker-compose installed. To start the container, simply run:
```
./run.sh
```


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

## Screenshots

Please replace the example screenshots with screenshots of your completed
project. Feel free to include more than one.

![Sample Screenshot](./img/samplescreenshot.png)

## Administration and Evaluation

### Team Members

1. Cao Wei
2. Pan Long
3. Zhan Yuli
4. Zhou Chuyu

### Short Answer Questions

#### Question 1: Briefly describe the web technology stack used in your implementation.

Our implementation uses [django REST framework](http://www.django-rest-framework.org/) and postgreSQL. For front-end, we use bootstrap and jQuery.

#### Question 2: Are there any security considerations your team thought about?

Http: serve web content using http may expose sensitive user information and make users susceptible to man-in-the-middle attacks. However, given the requirement of the API, we will not use https for this assignment.

SQL injection: we access the database only through Django's object-relational mapper(ORM) so as to ensure all queries are properly sanitized. No `raw()` SQL used.

Clickjacking:  we include `django.middleware.clickjacking.XFrameOptionsMiddleware` to prevent clickjacking.

#### Question 3: Are there any improvements you would make to the API specification to improve the security of the web application?

The API should include a token auto-expiration field together with a token renew API. This ensures the issued token is only valid for a certain period of time. 

#### Question 4: Are there any additional features you would like to highlight?

- All APIs are accessible through the front-end.
- Use docker-compose.

#### Question 5: Is your web application vulnerable? If yes, how and why? If not, what measures did you take to secure it?

CSRF: django by default have `CsrfViewMiddleware` enabled to prevent CSRF. We have disabled it to comply with the API requirement. 

XSS: the web app is susceptible to XSS as we did not sanitize user input at the front-end. 

#### Feedback: Is there any other feedback you would like to give?

Nil.

### Declaration

#### Please declare your individual contributions to the assignment:

1. Cao Wei
    - Back-end API implementation
2. Pan Long
    - Front-end development 
3. Zhan Yuli
    - Setup django REST boilerplate
    - Docker deployment  
4. Zhou Chuyu
    - Front-end development 

