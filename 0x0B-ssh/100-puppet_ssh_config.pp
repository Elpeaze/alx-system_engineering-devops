#!/usr/bin/puppet
# This file configures ssh with puppet.

include stdlib

file_line {'no pwd':
    ensure => pressent,
    line   => 'PasswordAuthentication no',
    path   => '/etc/ssh/ssh_config',
    }
file_line {'identity':
    ensure => present,
    line   => 'IdentityFile ~/.ssh/school',
    path   => '/etc/ssh/ssh_config',
    }
