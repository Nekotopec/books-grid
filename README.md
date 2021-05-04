# books-grid

## Description
Application with random generated book data. There is
author info and book info in the grid. This application provides with adding,
deleting and patching book data. For unsafe requests you must be logged in as admin.

Admin account will be created automatically when docker-compose start.
Use username **'admin'** and password **'admin'** to log in.

## Launch

1. Go to project directory.

`cd ./books-grid`

2. Launch docker-compose.

`docker-compose up --build`

3. Launch your browser on http://localhost:8080/
 
## P.S.
There is swagger in http://localhost:8080/api/swagger/
