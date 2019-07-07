# Puppet

Local VM with Puppet.

![alt text](diagrams/puppet-rk10-github.png "Logo Title Text 1")

- Puppet master and agent will be in the same VM.
- rk10 will be used so we can easily organise our Puppet files in one Github repository.


## Sandbox for Puppet Master Setup

Make sure you are in the `puppet` directory of the repository.

    cd puppet

Start the VM. Make sure you are int the `puppet` folder where there is a `Vagrantfile`. This will take a while if you are running it for the first time.

    vagrant up

When the machine is ready, after it has finished booting up. Login / ssh to the machine.

    vagrant ssh

Switch to root user.

    sudo su

Install what we need: puppet server package, vim and git. `vim` can be replaced with an editor of your choice.

    rpm -Uvh https://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm

    yum install -y puppetserver vim git

Open the puppet the server configuration.

    vim /etc/sysconfig/puppetserver

Replace the memory allocation value in `JAVA_ARGS` with what we will need for this exercise.

Original `JAVA_ARGS` value

    JAVA_ARGS="-Xms2g -Xmx2g -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"

Modified `JAVA_ARGS` value

    JAVA_ARGS="-Xms512m -Xmx512m -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"

Start puppet server. This might take around 1-2 minutes the first time you start it.

    systemctl start puppetserver
    systemctl enable puppetserver

Configure the puppet server host. Edit the `puppet.conf` file.

    vim /etc/puppetlabs/puppet/puppet.conf

Add the following at the bottom of the conf file. We need to tell our agent which server to use. For this exercise, it should point to itself.

    [agent]
    server = master.puppet.vm

Edit bash_profile to update the PATH value.

    vim .bash_profile

The new path value will look like the following.

    PATH=$PATH:/opt/puppetlabs/puppet/bin:$HOME/.local/bin:$HOME/bin

Load your bash profile the changes.

    source .bash_profile

`gem` should be accessible by now.

    gem

Install `r10k`. This will be used for deployment and integration with our version control.

    gem install r10k


## Github public repo setup

It's best practice to version control every change to puppet changes. This exercise is meant to demonstrate a common good practice in provisioning servers using Puppet.

This is the basis of the r10k control repo that we will use here: https://github.com/puppetlabs/control-repo

Create your own `contro-repo` in GitHub using its web interface. Add a `README.md` file.

We will use `production` branch instead of `master` to avoid confusion with puppet's `master`.

Configure your `r10k`. Copy the file from [r10k/r10k.yaml](r10k/r10k.yaml) into the directory you have created.

    mkdir /etc/puppetlabs/r10k

Update the remote git repository to point to the git repository that you have created above e.g. you can try to edit the `README.md` file for now to test if it works with our setup.

Deploy the changes from GitHub.

    r10k deploy environment -p

Check if the code is there,.

    ls -al /etc/puppetlabs/code/environments/

Ensure that the README.md file is present.

Create `manifests/site.pp` in Github repo.
We can edit directly from GitHub's web interface.

Paste the following into your code

    node default {
        file { '/root/README.md':
            ensure  => file,
            content => 'This should exist',
            owner   => 'root',
        }
    }

Run 

    r10k deploy environment -p

    puppet agent -t


Check file

    cat /root/README.md

## Try to break the deployment
Add the code below in to the default node and redeploy your control-repo with r10k.

    file { '/root/README.md':
        owner   => 'root',
    }

So your default node will look like this

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

Re-deploy your changes

    r10k deploy environment -p
    puppet agent -t

You should get an error. 
Revert your changes in GitHub and re-deploy.


## Puppet modules

https://forge.puppet.com

search for docker

Create a `Puppetfile` in the root director of your control-repo. 

    mod 'puppet/nodejs'
    mod 'puppet/mongodb'
    mod 'puppetlabs/stdlib'
    mod 'puppetlabs/apt'

Commit your changes.

Deploy changes to repo.

    r10k deploy environment -p
    puppet agent -t

Classes contains -> Nodes

Roles and profiles
Profiles Can be grouped into roles Roles 

Profiles
- bits and pieces
- e.g. web server, db server


ROles
- Buisness role of a machine e.g. this is a production app server or a developer workstation.


Create a new file

Create the following file in Github: `site/profile/manifests/web.pp`

    class profile::web {
        include 
    }



Create the file `site/role/manifests/app.pp`

    class role::app {
        include profile:web
    }