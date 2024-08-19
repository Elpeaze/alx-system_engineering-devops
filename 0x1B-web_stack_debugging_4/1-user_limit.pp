# Change the OS configuration so that it is possible to login 
# with the holberton user and open a file without any error message.

exec { 'change_value_to_50':
  command => "/bin/sed -i 's/5/50/g' /etc/security/limits.conf",
}

exec { 'change_value_to_40':
  command => "/bin/sed -i 's/4/40/g' /etc/security/limits.conf",
}
