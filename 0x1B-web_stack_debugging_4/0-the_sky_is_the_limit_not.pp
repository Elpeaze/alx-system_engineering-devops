# Configures nginx server request limit to accomodate large requests

file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT='-n 1024'\n",
  notify  => Service['nginx'],
}
