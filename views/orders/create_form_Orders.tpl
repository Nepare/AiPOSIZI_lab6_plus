<!DOCTYPE html>
<html>
<head>
    <title>Create orders</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        h2 {
            text-align: center;
        }
        form {
            margin: 0 auto;
            max-width: 400px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 4px;
            background-color: green;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: darkgreen;
        }
    </style>
</head>
<body>
    <h2>Create orders</h2>
    <form action="/Orders/create/" method="post">
        <label for="user_id">UserId:</label>
        <input name="user_id" type="text" />

        <br><br>

        <label for="product_name">ProductName:</label>
        <input name="product_name" type="text" />

        <br><br>

        <label for="quantity">Quantity:</label>
        <input name="quantity" type="text" />

        <br><br>

        <input value="Create" type="submit" />
    </form>
</body>
</html>
