# A  file that replaces ".phpp" with ".php" file extension.

exec { 'Fixed wordpress':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => shell,
}
