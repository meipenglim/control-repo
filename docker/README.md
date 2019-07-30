# Docker

Simple docker app.

## Pre-requisites:
- Docker
- Clone this repo: [https://github.com/ardydedase/devops](https://github.com/ardydedase/devops)

## Install Docker

- [Install Docker on Windows](https://runnable.com/docker/install-docker-on-windows-10)
- [Install Docker on Mac](https://runnable.com/docker/install-docker-on-macos)
- [Install Docker on Linux](https://runnable.com/docker/install-docker-on-linux)


## Build the Docker Images

This image will be using [this Dockerfile](hello-world-node/Dockerfile).

1. Make sure you are in the `docker/hello-world-node` folder.

    ```
    cd hello-world-node
    ```

1. Build the image.

    ```
    # v1 tag
    docker build -t myapp:v1 .
    ```

1. Uncomment `npm install winston` and `COPY ./ecs-compose.yml ./` from `Dockerfile` before running.

    ```    
    # latest tag
    docker build -t myapp:latest .
    ```

1. List the available images. This will display the images IDs and names.
    ```
    docker images
    ```

1. Compare the file sizes between the tagged images that you see in the list. Observe which image has a bigger file size.

1. Remove the image. Use the image ID and name shown after running `docker images`. Command: `docker rmi <image name or image ID>`

    ```
    # Remove a tagged image
    docker rmi myapp:v1

    # Remove an image including all its tags
    docker rmi myapp
    ```

## Run the Docker Containers

These containers will be using the images built from [this Dockerfile](hello-world-node/Dockerfile).

Make sure that you have followed the instructions in the [Docker Images](#docker-images) section.

1. Run the containers.

    ```
    # Run app0 in port 8080
    docker run -d -p 8080:5000 --name app0 myapp:latest

    # Run app1 in port 8081
    docker run -d -p 8081:5000 --name app1 myapp:latest    
    ```

1. Display the running containers and take note of their IDs or names.

    ```
    docker ps -a
    ```

1. Delete the containers. Command: `docker rm -f <container name or ID>`. 
The parameter `-f` is used to force remove the container without stopping it.

    ```
    docker rm -f app0
    docker rm -f app1
    ```

## Run the container with docker compose

1. Run the containers using docker compose.

    ```
    docker-compose up
    ```

1. Attempt to run multiple containers exposed through different ports e.g. ports `5000`, `5001` and `5002`.

## Credits
- [https://github.com/nburgess/react-express-example](https://github.com/nburgess/react-express-example)