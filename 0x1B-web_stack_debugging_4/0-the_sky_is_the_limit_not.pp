#0x1B-web_stack_debugging_4 
exec {'debugging':
    user    => root,
    path    => '/bin/',
    command => 'sudo sed -i "s/-n 10000/-n 4096/g" /etc/default/nginx',
}

-> exec { 'nginx':
    user     => root,
    provider => 'shell',
    command  => 'sudo service nginx restart',
}