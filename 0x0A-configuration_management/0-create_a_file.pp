# Create file in /cs_puppet

file { '/tmp/school':
ensure  => file,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => "I love Puppet\n", }
