# Docker

## Install Docker

- [Install Docker on Windows](https://runnable.com/docker/install-docker-on-windows-10)
- [Install Docker on Mac](https://runnable.com/docker/install-docker-on-macos)
- [Install Docker on Linux](https://runnable.com/docker/install-docker-on-linux)


## Docker Images

This image will be using [this Dockerfile](hello-world-node/Dockerfile).

Make sure you are in the `docker/hello-world-node` folder.

    cd hello-world-node

Build the image.

    # v1 tag
    docker build -t myapp:v1 .

    # Uncomment `npm install winston` from `Dockerfile` before running.
    # latest tag
    docker build -t myapp:latest .

List the available images. This will display the images IDs and names.

    docker images

Compare the file sizes between the tagged images.

Remove the image. Use the image ID and name shown after running `docker images`.

Command: `docker rmi <image name or image ID>`

    # remove a tagged image
    docker rmi myapp:v1

    # remove an images including all its tags
    docker rmi myapp

## Docker Containers

These containers will be using the images built from [this Dockerfile](hello-world-node/Dockerfile).

Make sure that you have followed the instructions in the [Docker Images](#docker-images) section.

Run the containers.

    # Run app0 in port 8080
    docker run -d -p 8080:5000 --name app0 myapp:latest

    # Run app1 in port 8081
    docker run -d -p 8081:5000 --name app1 myapp:latest    


Display the running containers

    docker ps -a

Delete the containers.

Command: `docker rmi <image name or image ID>`

    docker rm app0
    docker rm app1

## Credits
- https://github.com/nburgess/react-express-example