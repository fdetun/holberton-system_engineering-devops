#0x1B-web_stack_debugging_4 
exec {'debugging':
    user    => root,
    provider => 'shell',
    command => 'sudo sed -i 's/ULIMIT.*/ULIMIT="-n 10000"/' /etc/default/nginx && service nginx restart',
}
