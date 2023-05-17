# A  file that replaces ".phpp" with ".php"

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%=File.read("/var/www/html/wp-settings.php").gsub(/\\.phpp/,".php") %>'),
}

