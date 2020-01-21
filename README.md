# Smart Home

Tries to do what the title says.

## Setup
[This should work on Linux]

### To set up the environment
    cd projects_dir
    git clone <url to this project>
    cd smart-home
    virtualenv --python=python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

### To get set up the databases

! Make sure your virtualenv is activated

    cd website
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

### To run the server on your local network

! Make sure your virtualenv is activated

    python manage.py runserver 0.0.0.0:8000

To access the page from other devices on the network, find out the IP address of the server.

    ifconfig

You'll find the IP address under the appropriate network adapter. It'll typically be something like 
    
    192.168.xxx.yyy

Then you can hit the server on

    192.168.xxx.yyy:8000