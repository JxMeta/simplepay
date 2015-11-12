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

#Commands to start up
$ vagrant up <br/>
$ vagrant ssh <br/>

$ cd /var/www/simplepay/ <br/>
$ python manage.py runserver [::]:8000 <br/>


There are two functions in this test. <br/>
1. Display the records with navigation of tags <br/>
http://192.168.33.10:8000/persons <br/>
2. Admin to operate the records <br/>
http://192.168.33.10:8000/admin

Admin User: admin <br/>
Admin Password: 12345

#Unit Test 
Cases are drafted in
./simplepay/wwwroot/simplepay/persons/tests.py

There are 4 cases to be tested.<br/>
1. test the function of admin login <br/>
2. view the index page of ‘Persons’ app <br/>
3. view the tag page of ‘Persons’ app <br/>
4. view the person page of ‘Persons’ app <br/>

Run the command to test in site root directory.<br/>
$ python manage.py test persons<br/>
<br/>
...<br/>
Ran 4 tests in 0.099s<br/>
<br/>
FAILED (errors=2)<br/>
...<br/>
<br/>
The case of 3 and 4 are failed and caused by some setting problem. Pending to fix.
