#task 4
exec { 'task4':
  command  => 'echo -e "\tPasswordAuthentication no \n \tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
