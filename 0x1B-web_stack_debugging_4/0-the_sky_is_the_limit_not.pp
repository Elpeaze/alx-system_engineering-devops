# Configures nginx server request limit to accomodate large requests

file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT='-n 4069'\n",
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}
# Nginx configuration template (nginx.conf.erb)
$nginx_conf_content = @("EOF"/L)
worker_processes auto;
events {
    worker_connections 1024;  # Allows each worker to handle 1024 connections
    multi_accept on;  # Accept multiple connections at once
}
