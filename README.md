# DevOps

DevOps notes and resources

- Cloud 
  - AWS
  - Azure
  - Google Cloud
- IaC
  - Ansible
  - Terraform
  - Chef 
- Containers
 - Docker
 - Kubernetes

## Terminal setup

Windows users: [Install PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-windows-powershell)


## Compare VMs and Containers side by side

### Pre-requisites

- Docker: [Installation reference](docker/README.md)
- Vagrant: [Installation reference](vagrant/README.md)

### Container
- SSH in a running container.

    ```
    docker run -it --rm busybox
    ```
    - Pulls the busybox Docker image.
    - Runs it as a container.
- Run the following commands in the box.
    
    Check the files.
    ```
    ls -a
    ```

    Show the running processes.
    ```
    top
    ``` 

### Virtual Machine

- Provision the machine using Vagrant