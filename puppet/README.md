# Puppet

- Puppet master and agent will be in the same VM.
- rk10 will be used so we can easily organise our Puppet files in one Github repository.

![alt text](diagrams/puppet-rk10-github.png)"Logo Title Text 1")

## Sandbox for Puppet Master Setup

Start the VM.
    
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

We will use `production` branch instead of `master` to avoid confusion with `puppet master`.