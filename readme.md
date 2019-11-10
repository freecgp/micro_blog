### TODO LIST
    handle exceptions
    handle log

### API
    1./api/user
        method: POST
        req: 
            
            {
                "name": "lili",
                "password": "cgp"
            }
         
         response:
            {
                "id": 2
            }
    
    2./api/blog
        method: POST
        req:
            {
                "title": "lilihello1",
                "text": "hello",
                "user_id": 1
            }
            
        response:
            {
                "id": 5
            }
    
    3. /api/follow
        method: POST
        req:
            {
                "follower_id": 2,
                "followed_id": 1
            }
        response:
            {}
            
    4. /api/unfollow
    method: PUT
    req:
        {
            "follower_id": 2,
            "followed_id": 1
        }
    response:
        {}
        
    5. /api/users/<user_id>/news_feed
    method: GET
    response:
        [
            {
                "title": "lilihello1",
                "id": 5,
                "user_id": 1,
                "create_time": "2019-11-10 06:25:26",
                "update_time": "2019-11-10 06:25:26",
                "text": "hello"
            },
            {
                "title": "hello4",
                "id": 4,
                "user_id": 2,
                "create_time": "2019-11-10 06:19:43",
                "update_time": "2019-11-10 06:19:43",
                "text": "hello"
            },
            {
                "title": "hello3",
                "id": 3,
                "user_id": 2,
                "create_time": "2019-11-10 06:19:37",
                "update_time": "2019-11-10 06:19:37",
                "text": "hello"
            }
]