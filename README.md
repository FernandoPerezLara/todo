<br />
<p align="center">
  <a href="https://github.com/FernandoPerezLara/todo">
    <img src="https://raw.githubusercontent.com/FernandoPerezLara/todo/main/images/icon.png" alt="Logo" width="100" height="80">
  </a>

  <h3 align="center">TODO CLI</h3>

  <p align="center">
    Manage your pending tasks
    <br />
    <a href="https://github.com/FernandoPerezLara/todo"><strong>Visit website »</strong></a>
    <br />
    <br />
    <a href="https://github.com/FernandoPerezLara/todo/tree/main">View Code</a>
    ·
    <a href="https://github.com/FernandoPerezLara/todo/issues">Report Bug</a>
  </p>
</p>
<br />

The aim of this projects is to implement a console application to manage a to-do list.

## How does it work?
TODO is an application to manage a to-do list in a simple way. From this, you can create, delete and display the tasks of your day with a series of commands:
- `todo add TEXT`: This command is used to create new tasks.
- `todo delete TEXT`: To delete an existing task, by searching for the task name instead of an identifier, you can easily delete it.
- `todo list`: You will be able to see all the tasks in your list. This command allows you to change the output format with the `--output <TYPE>` parameter, where you can choose between `txt`, `json` and `table` options.

As you can see, its use is very simple, since this application is in charge of handling errors, searching by text instead of by identifier, making the connection with the Rest API, etc.

To make this application work properly, it is necessary to have a Rest API in charge of managing all the requests with a MongoDB server.

<p align="center">
  <img src="https://raw.githubusercontent.com/FernandoPerezLara/todo/main/images/communication.png" alt="Communication">
</p>

There are two ways to test this application:
- Locally: This is explained in the section [Installation](#installation).
- Using the GitHub Actions playground: A workflow has been created to perform a series of tests [./actions/workflows/example.yml](https://github.com/FernandoPerezLara/todo/actions/workflows/example.yml).
	1. Create randomly between 10 and 100 entries.
	2. They are displayed on the screen depending on the output type specified in the workflow input (`txt`, `table` or `json`).
	3. The events created are deleted, leaving the list empty.

## Installation
To install this application on a local machine, it can be done in two ways, but in both, it is necessary to clone this repository:
```bash
git clone https://github.com/FernandoPerezLara/todo.git
cd todo
```

### Method 1. Installation with Docker (like the pros 🎩).
This method is the most recommended because the installation of packages and libraries is done automatically in a controlled environment. On the other hand, it is more secure, it does not require open ports on your local machine, since the communication is done internally between the containers.

As previously mentioned, it is necessary to have the API Rest and the MongoDB server running in the background to make the corresponding requests. To do this, the following command is launched:
```bash
cd node-todo
docker-compose up
```

This command will create a custom image for the Rest API ([Dockerfile](https://github.com/FernandoPerezLara/node-todo/blob/5d6b698913ab69e96d75f1faef8f1421d3d17158/Dockerfile)) and two containers to run the database and the Rest API ([docker-compose.yml](https://github.com/FernandoPerezLara/node-todo/blob/5d6b698913ab69e96d75f1faef8f1421d3d17158/docker-compose.yml)). This will create a network named `node-everything_server` that will connect to the application container.

Secondly, to run the application it will be enough to execute the following command, since it will automatically create the necessary images and containers:
```bash
docker-compose run todo list --output table
```

These images can be found in the folder [./docker/Docker](https://github.com/FernandoPerezLara/todo/tree/main/docker) and are orchestrated using the file [docker-compose.yml](https://github.com/FernandoPerezLara/todo/blob/main/docker-compose.yml).

### Method 2. Installation on a local machine
This way is the least recommended because it requires manually installing all the dependencies and libraries needed to run the program.

As done in the previous section, first of all, in order to be able to run the Rest API together with the MongoDB server it will be necessary to install all the necessary dependencies:
```bash
cd node-todo
npm install
node server.js
```

> It is necessary to modify the MongoDB server link in the file [./node-todo/config/database.js](https://github.com/FernandoPerezLara/node-todo/blob/5d6b698913ab69e96d75f1faef8f1421d3d17158/config/database.js) y and the file [./scripts/utils/constants.py](https://github.com/FernandoPerezLara/todo/blob/main/scripts/utils/constants.py).

Once the Rest API and database are launched, the Python libraries needed to run the program will be installed:
```bash
pip install -r requirements.txt
./todo list --output table
```

## Project structure
Inside this repository you can find the submodule [FernandoPerezLara/node-todo](https://github.com/FernandoPerezLara/node-todo/). This contains the Rest API server and the database server.

The file [todo](https://github.com/FernandoPerezLara/todo/blob/main/todo) will be in charge of executing the application and with a series of commands specified in [./scripts/commands](https://github.com/FernandoPerezLara/todo/tree/main/scripts/commands) manage al the tasks from the list. Request and error handling can be found at [./scripts/utils](https://github.com/FernandoPerezLara/todo/tree/main/scripts/utils).

LThe tests can be found in the folder [./test](https://github.com/FernandoPerezLara/todo/tree/main/test).

The configuration file for the containers is [docker-compose.yml](https://github.com/FernandoPerezLara/todo/blob/main/docker-compose.yml) and makes use of the images created in the folder [./docker](https://github.com/FernandoPerezLara/todo/tree/main/docker).

Finally, all workflows can be found at [./.github/workflows](https://github.com/FernandoPerezLara/todo/tree/main/.github/workflows).

## Contribute to the project
This repository has automated workflows for the future implementation of new features.

The `main` and `develop` branches are protected, to create a new feature or resolve a bug, it is necessary to create a new branch from `develop` and create a pull request from this branch for its later combination with `develop`.

When creating the pull request, the following workflows will be executed:
- [./actions/workflows/linter.yml](https://github.com/FernandoPerezLara/todo/actions/workflows/linter.yml): It checks that all the code is well written, if not, this branch is blocked.
- [./actions/workflows/test.yml](https://github.com/FernandoPerezLara/todo/actions/workflows/test.yml): This flow executes the tests found inside [./test](https://github.com/FernandoPerezLara/todo/tree/main/test).
	- Add between 10 and 100 new items to the list.
	- Display a list in `txt` format.
	- Display a list in `json` format.
	- Display a list in `table` format.
	- Remove a single item from the list.
	- Remove all items from the list.

If all workflows pass successfully, it will be necessary for a team member to review the changes and accept them.

Before creating the pull request it is recommended to pass these two workflows from a local machine, this can be done with the following commands:
```bash
docker-compose run linter
docker-compose run test
```

## Contributors
- [Fernando Pérez Lara](https://www.linkedin.com/in/fernandoperezlara/) ([**@FernandoPerezLara**](https://github.com/FernandoPerezLara)) for developing this project.
