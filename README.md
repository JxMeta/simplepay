# simplepay
SimplePay Task

#Platform: 
CentOS 7

#Prerequisites: 
apache2,
vagrant,
virtualbox,
python-pip,
django,
git,


$ vagrant up
$ vagrant ssh

$ cd /var/www/simplepay/
$ python manage.py runserver [::]:8000


There are two functions in this test.
1. Display the records with navigation of tags
http://192.168.33.10:8000/persons
2. Admin to operate the records
http://192.168.33.10:8000/admin

Admin User: admin
Admin Password: 12345

#Unit Test 
Cases are drafted in
./simplepay/wwwroot/simplepay/persons/tests.py

There are 4 cases to be tested.
test the function of admin login
view the index page of ‘Persons’ app
view the tag page of ‘Persons’ app
view the person page of ‘Persons’ app

Run the command to test in site root directory.
$ python manage.py test persons

...
Ran 4 tests in 0.099s

FAILED (errors=2)
...

The case of 3 and 4 are failed and caused by some setting problem. Pending to fix.
