# Games_Center
This project is a web-based game platform that uses Flask, saves scores to a MySQL database and can be deployed using Docker and Helm. It is built following best practices and design patterns.

# Game Platform

This project is a web-based implementation of various games, with the added functionality of saving user scores to a database. The project is built using Python and utilizes the Flask framework for building web applications. The games are divided into different web pages, and classes and their implementations are reused. 

## Deployment

The project uses Docker to containerize the application and make it easy to deploy. The Docker-compose file is also included, which allows you to easily spin up the application and its dependencies. The project also includes Helm chart, which allows for easy deployment to a Kubernetes cluster.

## Database

The game's scoring system is implemented using a MySQL database, and the database is also containerized. Additionally, the project includes a number of end-to-end tests (Selenium) to test the game functionality.

## Best Practices & Design Patterns

The project is organized in a way that follows best practices and design patterns. It is separated into different packages for games, scores, and testing.
