# flask

Lightweight and limited components

### Features included:

 * __Jinja 2 template engine__ ( Building HTML ) - similar to DJANGO
 * __Werkzeug__  ( HTTP and routing )
 * Development server and debugger
 * Unit testing support
 
 
 Installing the flask dependency
  > python -m pip install flask
 
### Setting up two environment variables :

* Which module can my find my app(Unix) :
  > export FLASK_APP=flashcards.py  
  
* What environment  ( dev enables debugger )
  > export FLASK_ENV=development  
                       
* Start Command
  > flask run                

### How to add some images / css / javascript

 subfolder static/
 
___
## Model Template View Pattern
 
 * View - Functions already defined by @app.route functions  
 
 * Jinja Templates   
   - Display data to users  
   - Generating HTML  
   - Calling templates from views(func)  
   - Passing Data from view to template  
   - Jinja variables  
 
 * Data Model ( DB side )  
   - model layer
 
 ### Jinja Templates 
 
 1) import the render_template and pass the template name  
    > return render_template("welcome.html")  
     
 2) __/templates__ folder is where the scan happens  
 
 3) __{{message}}__ : Jinja variable in the html for eval  
    Value passed from the view(function)    
     > return render_template("welcome.html" , message="<messageContent>")
 
 ### Model Layer [ DB] 
   Refer to the model.py module
   
   
## Logic Handling

  * View(Function) Logic
     - Take Arg from Url   
       > @app.route('/card/<int:index>')
         
     - Return HTTP Error  
       > import abort -- abort(404)  
         
     - Serving Data as REST API    
     
  *  Template Logic
    - Jinja For and IF statements 
       > refer to card.html  
   - Creating Links to Cards
 
 
 ## Rest API ( Data )
 
 refer to @app.route('/api/**) in flashcards.py
 refer how __jsonify__ is used on List obejcts
 
 
 ## Deploying to Production ( best practice )
 
  1. Not to Use flask server
    Use popular pythin httpserver : __gunicorn__
 
  2. Run behind a Reverse Proxy
     (nginx)
     
 ### Setup on Ubuntu
  
   apt install the following packages
    - nginx
    - python3 , python3-pip
    
   1. git clone <the project>   
   2. sudo apt install gunicorn3 ( at system level and not pip )   
      pip3 install -r requirements.txt ( use Venv )
   3. gunicorn3 flashcards:app
   
   This makes the server listen on port 8000 , but we want it to be on 80 on public ip
   
   4. Use nginx ( webserver runs on port 80 ) ( prevents DDOS )
     Now run in Daemon mode after logout as well
      > gunicorn3 -D flashcards:app  
                                                                                                                       
 ### Nginx configuration     
   
   Remove the default home page of the webserver at :  
   > cd /etc/nginx/sites-available  
   > sudo rm default  
     
   Create a new Site ( refer to e.g config from gunicorn.org)
   > vi default   
 
   ```
    server {
    listen 80;
    server_name example.org;
    access_log  /var/log/nginx/example.log;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
  }  
  ```

  Restart the nginx service  
  > sudo service nginx restart
  
## Prometheus Flask Exporter
 In your venv install the prometheus-flask-exporter  
 > pip install prometheus-flask-exporter  



