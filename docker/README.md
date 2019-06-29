# Docker

## Install Docker

- [Install Docker on Windows](https://runnable.com/docker/install-docker-on-windows-10)
- [Install Docker on Mac](https://runnable.com/docker/install-docker-on-macos)
- [Install Docker on Linux](https://runnable.com/docker/install-docker-on-linux)


## Docker Images

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


## Credits
- https://github.com/nburgess/react-express-example