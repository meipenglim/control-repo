# Infrastructure as Code with Puppet

This exercise is meant to help you understand how Infrastructure works with Puppet as an example.

## Pre-requisites

- A GitHub account.
- You have cloned this repo locally: https://github.com/ardydedase/devops
- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Install [Vagrant](https://www.vagrantup.com/downloads.html)
    - Note that Windows users might need to logout and login again.

## High level design

- Puppet master and agent will be in the same VM.
- rk10 will be used so we can easily organise our Puppet files in one Github repository.

    ![Puppet in local VM](diagrams/puppet-rk10-github.png "Puppet in local VM")

## Sandbox for Puppet Master Setup

- Make sure you are in the `puppet` directory of the repository.

    ```
    cd puppet
    ```

- Start the VM. Make sure you are int the `puppet` folder where there is a `Vagrantfile`. This will take a while if you are running it for the first time.

    ```
    vagrant up
    ```

- When the machine is ready after it has finished booting up. Login / ssh to the machine.

    ```
    vagrant ssh
    ```

- Switch to root user.

    ```
    sudo su
    ```

- Install what we need: Puppet server package, vim and git. `vim` can be replaced with an editor of your choice.

    ```
    rpm -Uvh https://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm

    yum install -y puppetserver vim git
    ```

- Open the puppet the server configuration.

    ```
    vim /etc/sysconfig/puppetserver
    ```

- Replace the memory allocation value in `JAVA_ARGS` with what we will need for this exercise.

    Original `JAVA_ARGS` value:

    ```
    JAVA_ARGS="-Xms2g -Xmx2g -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"
    ```

    Modified `JAVA_ARGS` value:

    ```
    JAVA_ARGS="-Xms512m -Xmx512m -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"
    ```

- Start puppet server. This might take around 1-2 minutes the first time you start it.

    ```
    systemctl start puppetserver
    systemctl enable puppetserver
    ```

- Configure the puppet server host. Edit the `puppet.conf` file.

    ```
    vim /etc/puppetlabs/puppet/puppet.conf
    ```

- Add the following at the bottom of the conf file. We need to tell our agent which server to use. For this exercise, it should point to itself. `master.puppet.vm` matches our Vagrant hostname.

    ```
    [agent]
    server = master.puppet.vm
    ```

- Edit bash_profile to update the `PATH` value.

    ```
    vim .bash_profile
    ```

- The updated `PATH` value should look like the following.

    ```
    PATH=$PATH:/opt/puppetlabs/puppet/bin:$HOME/.local/bin:$HOME/bin
    ```

- Load the changes in the current terminal session.

    ```
    source .bash_profile
    ```

- `gem` should be accessible by now.

    ```
    gem --help
    ```

- Install `r10k`. This will be used for deployment and integration with our version control.

    ```
    gem install r10k
    ```

## GitHub public repo setup

It's best practice to version control every change to puppet changes. This exercise is meant to demonstrate a common good practice in provisioning servers using Puppet.

This is the basis of the r10k control repo that we will use here: https://github.com/puppetlabs/control-repo.

- Create your own `contro-repo` in GitHub using its web interface. Add a `README.md` file. We will use `production` branch instead of `master` to avoid confusion with puppet's `master`. Make sure that this repository is public.

- Configure your `r10k`. Copy the file from [r10k/r10k.yaml](r10k/r10k.yaml) into the directory you have created.

    ```
    mkdir /etc/puppetlabs/r10k
    ```
- Create the r10k configuration file.

    ```
    touch /etc/puppetlabs/r10k/r10k.yaml
    vim /etc/puppetlabs/r10k/r10k.yaml
    ```
    Paste the following cofiguration to the `r10k.yaml` file. 
    Replacing the `$YOUR_GITHUB_USERNAME$` with your own GitHub username.

    ```
    ---
    # Cached git repos
    :cachedir: '/var/cache/r10k'

    # Repos. clones git repo
    :sources:
    # branch => environment  mapping in /etc/puppetlabs/code/environments
    # replace username with your github username
    :my-org:
        remote: 'https://github.com/$YOUR_GITHUB_USERNAME$/control-repo.git'
        basedir: '/etc/puppetlabs/code/environments'    
    ```

- Update the remote git repository to point to the git repository that you have created above e.g. You can try to edit the `README.md` file for now to test if it works with our setup.

- Deploy the changes from GitHub.

    ```
    r10k deploy environment -p
    ```

- Check if the code is there. Ensure that the `README.md` file is present in the directory.

    ```
    ls -al /etc/puppetlabs/code/environments/
    ```

- Create `manifests/site.pp` in Github repo. We can edit directly from GitHub's web interface. Paste the code below to the file. Commit your changes.

    ```
    node default {
        file { '/root/README.md':
            ensure  => file,
            content => 'This should exist',
            owner   => 'root',
        }
    }
    ```

- Run the following commands to deploy your changes.

    ```
    r10k deploy environment -p

    puppet agent -t
    ```

- Check if the file is present in your VM:

    ```
    cat /root/README.md
    ```

## Try to break the deployment
- Add the code below in to the default node and redeploy your control-repo with r10k.

    ```
    file { '/root/README.md':
        owner   => 'root',
    }
    ```

- So your default node will look like this.

    ```
    node default {
        file { '/root/README.md':
            ensure  => file,
            content => 'This should exist',
            owner   => 'root',
        }
        file { '/root/README.md':
            owner   => 'root',
        }        
    }
    ```

- Re-deploy your changes.

    ```
    r10k deploy environment -p
    puppet agent -t
    ```

You should get an error at this point. Revert your changes in GitHub and re-deploy.

## Puppet modules

- Create a `Puppetfile` in the root directory of your control-repo. Commit your changes.

    ```
    mod 'puppet/nodejs'
    mod 'puppet/mongodb'
    mod 'puppetlabs/stdlib'
    mod 'puppetlabs/apt'
    ```

- Deploy your changes from your repo to your virtual machine.

    ```
    r10k deploy environment -p
    puppet agent -t
    ```

- Check if your modules were successfully provisioned.

    ```
    ls -al /etc/puppetlabs/code/environments/production/modulesls mo
    ```

- Create a `node.pp` file in the manifests folder of your control repo with the following class to install nodejs using Puppet:

    ```
    class { 'nodejs': }
    ```

- Deploy your changes from repo to your virtual machine.

    ```
    r10k deploy environment -p
    puppet agent -t
    ```

- Check that your nodejs application is installed.

    ```
    node --version
    ```

More learning resources in: https://learn.puppet.com/