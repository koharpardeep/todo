# todo


####Creating a Todo : 
    url : /todo/create/
    request type : POST
    Input parameters:
    
    1. "state" : Enter 1 for "todo", 2 for "in_progress" and 3 for "done"
    2. "due_date" : Enter date in YYYY-MM-DD format (ex: 2018-01-05).
    3. "text" : Enter text with length grater than 10.
    
    Output response:
    {
    "code": 200,
    "message": "success"
    }
    In case of failue code and message will be different.
    
####Updating a Todo : 
    url : todo/update/
    request type: POST
    Input parameters:
    
    1. "id" : This will be the id of previously created todo.You can get it using GetAllTodo service described below.
    1. "state" : Enter 1 for "todo", 2 for "in_progress" and 3 for "done"
    2. "due_date" : Enter date in YYYY-MM-DD format (ex: 2018-01-05).
    3. "text" : Enter text with length grater than 10.
    
    Output Response:
    {
    "code": 200,
    "message": "success"
    }
    In case of failue code and message will be different.
    
####Get All Todos
    url : todo/getall/?orderby=both
    request type: GET
    Input parameters:
    1.orderby : "state" = Will give data order by state
                "due_date" = Will give data order by due_date
                "both" = Will give order by state and due_date
                
    Output response:
    {
    "code": 200,
    "data": [
        {
            "id": 34,
            "state": "in_progress",
            "due_date": "2018-01-05",
            "text": "Hi this is Pardeep Kumar5"
        }
    ],
    "message": "success"
    }
    In case of failue code and message will be different.
    
####Delete a todo:
    url : todo/delete/
    request type: POST
    Input parameters:
    
    1. "id" : This will be the id of previously created todo.You can get it using GetAllTodo service described above.
    
    Output Response:
    {
    "code": 200,
    "message": "success"
    }
    In case of failue code and message will be different.