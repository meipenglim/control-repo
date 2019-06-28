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

## Compare a Virtual Machine and a Container side by side

### Pre-requisites

- Docker: [Installation reference](docker/README.md)
- Vagrant: [Installation reference](vagrant/README.md)

### Container

Open this in a separate terminal window from the Virtual Machine.

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

Open this in a separate terminal window from the Container.

- Provision the machine using Vagrant. This might take a while.

    ```
    cd vagrant
    vagrant up
    ```
- After the VM is fully provisioned. SSH into the VM

    ```
    vagrant ssh
    ```

- While ssh'ed in the VM, show the running processes.
    ```
    top
    ```