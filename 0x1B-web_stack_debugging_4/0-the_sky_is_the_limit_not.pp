# Configures nginx server request limit to accomodate large requests

file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT='-n 4069'\n",
  notify  => Service['nginx'],
}
