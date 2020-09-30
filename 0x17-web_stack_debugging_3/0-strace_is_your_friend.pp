#fixing wp-settings.php file 
exec {'fix wordpress setting file':
    user    => root,
    path    => '/bin',
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
}
exec {'restart apache2':
    user    => root,
    path    => '/bin',
    command => 'sudo service apache2 restart',
}
