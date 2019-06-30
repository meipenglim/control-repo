# Puppet

Local VM with Puppet.

![alt text](diagrams/puppet-rk10-github.png "Logo Title Text 1")

- Puppet master and agent will be in the same VM.
- rk10 will be used so we can easily organise our Puppet files in one Github repository.


## Sandbox for Puppet Master Setup

Start the VM. Make sure you are int the `puppet` folder where there is a `Vagrantfile`.

    vagrant up

When the machine is ready. Login to the machine.

    vagrant ssh

Root

    sudo su

Run the following

    rpm -Uvh https://yum.puppetlabs.com/puppet5/puppet5-release-el-7.noarch.rpm


Install what we need: puppet server package, vim and git.

    yum install -y puppetserver vim git

`vim` can be replaced with an editor of your choice.

Check puppet server config

    vim /etc/sysconfig/puppetserver

Replace the memory allocation value in `JAVA_ARGS` with what we will need for this exercise.

Foor example:

Original: `JAVA_ARGS="-Xms2g -Xmx2g -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"`

Modified: `JAVA_ARGS="-Xms512m -Xmx512m -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"`


Start puppet server

    # This might take around 1-2 minutes the first time you start it.
    systemctl start puppetserver
    systemctl enable puppetserver

Configure 

    vim /etc/puppetlabs/puppet/puppet.conf

Add the following at the bottom of the conf file. We need to tell our agent which server to use. Point to itself.

    [agent]
    server = master.puppet.vm

Edit bash_profile

    vim .bash_profile


Update the PATH value

    PATH=$PATH:/opt/puppetlabs/puppet/bin:$HOME/.local/bin:$HOME/bin

After the changes.

    source .bash_profile

`gem` should be accessible now

    gem

Install r10k. For demployment and integration with version control.

    gem install r10k


## Github public repo setup

This is the basis of the r10k control repo that we will use here: https://github.com/puppetlabs/control-repo

We will use `production` branch instead of `master` to avoid confusion with `puppet master`. Create a `sandbox` branch instead.

Setup r10k

    mkdir /etc/puppetlabs/r10k

Copy the file from [r10k/r10k.yaml](r10k/r10k.yaml)

Deploy the changes from github

    r10k deploy environment -p

Check if the code is there

    ls -al /etc/puppetlabs/code/environments/

It's best practice to version control every change to puppet changes.

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