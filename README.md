# Landbot Backend Challenge

## Description

The product department wants a system to be notified when a customer requests assistance from a bot. The bot will make an http call (like a webhook) with the following information:

- Topic: a string with values can be sales or pricing
- Description: a string with a description of the problem that needs assistance from.

You need to expose an API endpoint that will receive this call and depending on the selected topic will forward it to a different channel:

``` 
Topic    | Channel   
----------------------
Sales    | Slack
Pricing  | Email
```

## Notes:
- Slack and Email are suggestions. Select one channel that you like the most, the other can be a mock.
- There may be more topics and channels in the future.

## The solution should:
- Be written in your favorite language and with the tools with which you feel comfortable.
- Be coded as you do daily (libraries, style, testing...).
- Be easy to grow with new functionality.
- Be a dockerized app.


# Solution

## 📄 Description

**Notifier** is an application developed with Django and Django Rest Framework (DRF) designed to receive customer requests via a bot and forward them to different communication channels depending on the selected topic. This solution is scalable, maintainable and built following SOLID principles to ensure decoupled code that is easy to extend in the future.

## 🚀 Characteristics

- **Endpoint API RESTful**: Receive requests with the topic and a description.
- **Sending to multiple channels**: Depending on the topic (`sales` or `pricing`), notifications are sent to Slack or Email, respectively.
- **Scalable architecture**: Designed to make it easy to add new topics and channels in the future without modifying existing logic
- **Code decoupling**: Implementation of design patterns that ensure different parts of the system are separated and easily interchangeable.
- **Dockerization**: Docker containers for easy deployment and consistency between development and production environments.

## 🛠️ Technology

- **Programming Language**: Python
- **Web Framework**: Django
- **API Framework**: Django Rest Framework (DRF)
- **Task Orchestration**: Django Q
- **Message Broker**: Redis
- **Database**: SQLite (configurable to PostgreSQL or others)
- **Containers**: Docker, Docker Compose
- **Testing**: Django Test Framework
- **Version Control**: Git, GitHub

## 🏗️ Architecture

The application is designed following SOLID principles to ensure clean, modular, and maintainable code:

- **Single Responsibility Principle (SRP)**: Views handle validation and task queuing, while the orchestrator is responsible for sending notifications.

- **Open/Closed Principle**: Adding new `topics` or channels does not require changes to existing code, only the addition of new notifiers in the factory.

- **Dependency Inversion Principle**: The view depends on abstractions (interfaces), facilitating the possibility of changing the implementation without affecting the other parts of the system.

- **Factory Pattern**: Used to instantiate the different notifiers according to the `topic`, allowing easy extension to new channels.

### Simplified diagram

```
landbot-senior-sw-engineer-challenge/ 
├── api/ 
│ ├── serializers.py 
│ ├── views.py
│ ├── tests.py 
│ ├── urls.py 
│ └── views.py 
├── notifications/ 
│ ├── apps.py 
│ ├── factories.py 
│ ├── interfaces.py 
│ ├── models.py 
│ ├── notifiers.py 
│ ├── services.py 
│ ├── tasks.py 
│ └── tests.py 
├── notifier/ 
│ ├── settings.py 
│ └── urls.py 
├── manage.py 
├── Dockerfile 
├── docker-compose.yml 
└── README.md
```



## 🧩 Implemented Strategies

### 1. **Decoupling and SOLID**

- **Notifier Factory**: `NotifierFactory` manages the creation of notifiers based on the `topic`, allowing new channels to be added without modifying existing logic.

- **Notification Orchestrator**: `notification_orchestrator` manages the queuing of sending tasks.

- **Interfaces and Abstractions**: Use of interfaces to define behaviors, allowing specific implementations to be changed without affecting the rest of the system.

### 2. **Scalability**

- **Topics and Channels Extension**: The architecture makes it easy to add new `topics` and channels by simply registering new notifiers in the factory.

- **Database Configuration**: Although SQLite is used by default, the configuration allows you to easily switch to other databases without modifying the business logic.

### 3. **Automated Testing**

- **Unit Tests**: These test the individual logic of components.

- **Integration Tests**: These verify the complete flow from receiving a request to sending the notification.

- **Mocking**: Use of `unittest.mock` to simulate external behaviors.

### 4. **Dockerization**

- **Docker Compose**: Configuration to run multiple services in a simple and reproducible way.


# 🛠️ Installation

## Prerequisites
- Docker & Docker Compose installed.
- Git for version control.

## Quickstart

Clone the Repository

1. ```git clone https://github.com/diegoslorenzo/landbot-senior-sw-engineer-challenge.git```

2. ```cd landbot-senior-sw-engineer-challenge```

Build and Deploy Docker Containers

3. ```docker-compose up -d --build```



# Usage
## Send a notification
Make a POST request to the endpoint http://localhost:8000/api/notify/ with the following JSON format:
```json
{
"topic": "sales",
"description": "I need help."
}
```
Example with `curl`:
```bash
curl -X POST http://localhost:8000/api/notify/ \
-H "Content-Type: application/json" \
-d '{"topic": "sales", "description": "I need help."}'
```

# 🧪 Testing

## Running Tests
To run the tests, use the following command:
```bash
docker-compose exec web python manage.py test
```


