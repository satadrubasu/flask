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
 
 ### Model Layer   
 