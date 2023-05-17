# A  file that replaces ".phpp" with ".php"

service { 'apache2':
  ensure => running,
  enable => true,
}

package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'This is the correct page.',
  require => Package['apache2'],
}

file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => present,
  content => template('module/site.conf.erb'),
  notify  => Service['apache2'],
  require => Package['apache2'],
}

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%=File.read("/var/www/html/wp-settings.php").gsub(/\\.phpp/,".php") %>'),
  notify  => Service['apache2'],
  require => Package['apache2'],
}

file { '/var/www/html/wp-settings.php':
  4   ensure  => present,
  5   content => inline_template('<%=File.read("/var/www/html/wp-settings.php").gsub(/\\.phpp/,".php") %>'),
  6   notify  => Service['apache2'],
  7 }
