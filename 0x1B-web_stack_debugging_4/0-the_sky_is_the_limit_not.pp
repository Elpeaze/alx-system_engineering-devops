# Ensure the nginx default configuration file is present with the specified content
file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT='-n 4069'\n",
}
