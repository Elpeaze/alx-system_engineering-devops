# Using Puppet, install flask from pip3

package { 'pip3':
  ensure   => 'installed',
 }

exec { 'install-flask':
  command  => '/usr/bin/pip3 install flask==2.1.0',
  creates  => '/usr/local/lib/python3.8/dist-packages/flask''
}
