file { '/etc/default/nginx':
  ensure => file,
  content => "ULIMIT='-n 2035'\n",
}
