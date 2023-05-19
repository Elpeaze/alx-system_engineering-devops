file { "/etc/default/nginx":
  ensure => file,
  content => "ULIMIT-'-n 5000'\n", }
