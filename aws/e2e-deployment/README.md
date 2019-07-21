# End to end DevOps Engineering and Automation

This will help you set up a setup a set of AWS tools capable of DevOps operation from committing a code change to a repository, to build and deployment.

## Credits and references
- [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html)
- [Deploying Docker Containers Using an AWS CodePipeline for DevOps](https://www.infoq.com/articles/aws-codepipeline-deploy-docker/)


## Pre-requisites

- AWS Account
- GitHub Account
- Any Docker image that has a source code repo
- A temporary [Docker hub account](https://hub.docker.com/)

## Environment and code setup

1. Create your GitHub code repository.
1. Add your Dockerfile. [Use this repository](https://github.com/ardydedase/devops/tree/master/docker/hello-world-node) as a reference. 
1. Add a build spec file for AWS CodeBuild. Please be aware that this will need you to specify your docker username and password in this configuration file. *We should use a temporary password for this exercise, replace your docker hub password afterwards.*

    Replace the variables `<variable-format>` accordingly:

    ```
    --- 
    phases: 
    build: 
        commands: 
        - "echo Build started on `date`"
        - "echo Building the Docker image..."
        - "docker build -t <yourdockerusername>/hello-world-node ."
        - "docker tag <yourdockerusername>/hello-world-node <yourdockerusername>/hello-world-node:latest"
    post_build: 
        commands: 
        - "echo Build completed on `date`"
        - "echo Pushing the Docker image..."
        - "docker push <yourdockerusername>/hello-world-node:latest"
    pre_build: 
        commands: 
        - "echo Logging in to Docker Hub..."
        - "docker login --username=\"<yourusername>\" --password=\"<yourpassword>\""
    version: 0.1
    ```
1. Add an image definitions file for AWS CodePipeline:

    Replace the variables `<variable-format>` accordingly:

    ```
    [
        {
            "name": "hello-world-node",
            "imageUri": "<yourusername>/hello-world-node"
        }
    ]    
    ```

## AWS Setup

### Create a task definition in ECS. 

1. [Open this URL and log in if not already logged in](https://console.aws.amazon.com/ecs). 
1. Click on Get started to access the ECS Console. 
1. Click on Task Definitions in the navigation margin. In the Task Definitions click on Create new Task Definition. In the Create new Task Definition select launch type compatibility as Fargate. 
1. Click on Next step. Next, configure task and container definitions. 
1. In the Add container dialog specify a Container name (hello-world-node) and specify Image as <yourusername>/hello-world-node.

### Configure Task Subnets
We need to add a route that allows access to all networks.s

1. [Open the VPC Dashboard](https://console.aws.amazon.com/vpc). 
1. Check the Route Table that lists the routes.
1. Add a route with a destination as 0.0.0.0/0. 
1. Select Target as internet gateway.

### Create and test the container service

1. Create an ECS container service in the default cluster.
1. Copy the Public IP of the task, which is the same as the Public IP of the Elastic Network Interface, from either the task Details page Network section or the ENI Console. 
1.  Open the URL <Public IP of Task>:5000 in a browser to invoke the Node Service application.
1. You should see the "Hello World" message from the app by now.

## Setting up the build and deployment pipeline

Please refer to the "Creating a CodeBuild Project" section and onwards in [this walkthrough to set up the Deployment Pipeline in AWS](https://www.infoq.com/articles/aws-codepipeline-deploy-docker/).
