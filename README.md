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

### Run the following in each terminal window
In each of the terminal window opened above for the container and VM, run the following commands.

```
# Compare the disk space sizes
du - sh

# Compare the processes
top

# Show what you can find a process
ls -al /proc/1/ns
```