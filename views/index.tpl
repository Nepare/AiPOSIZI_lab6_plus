<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        h2 {
            text-align: center;
            margin-top: 0;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            display: inline-block;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 16px;
            border-radius: 4px;
            color: white;
            background-color: #2196F3;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        a:hover {
            background-color: #1976D2;
        }
    </style>
</head>
<body>
    <h2>Home</h2>
    <ul>
        <li><a href="/Users/get/">Users</a></li>
        <li><a href="/Products/get/">Products</a></li>
        <li><a href="/Orders/get/">Orders</a></li>
        <li><a href="/Categories/get/">Categories</a></li>
    </ul>
</body>
</html>
