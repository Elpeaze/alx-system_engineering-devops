file { '/etc/default/nginx':
  ensure => file,
  content => "ULIMIT='-n 4069'\n",
}
