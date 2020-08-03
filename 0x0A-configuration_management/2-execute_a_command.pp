#task 3

exec { 'pkill -f killmenow':
    path => '/usr/bin'
}
