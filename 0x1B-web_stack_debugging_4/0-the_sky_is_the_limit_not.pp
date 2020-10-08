#0x1B-web_stack_debugging_4 
exec {'debugging':
    path    => '/bin/',
    command => 'sudo sed -i "s/-n 15/-n 4096/g" /etc/default/nginx',
}

-> exec { 'nginx':
    provider => 'shell',
    command  => 'sudo service nginx restart',
}