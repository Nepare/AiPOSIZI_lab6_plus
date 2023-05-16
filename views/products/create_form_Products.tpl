<!DOCTYPE html>
<html>
<head>
    <title>Create products</title>
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
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h2>Create products</h2>

    <form action="/products/create/" method="post">
        <label for="name">Name:</label>
        <input name="name" type="text" />

        <br><br>

        <label for="price">Price:</label>
        <input name="price" type="text" />

        <br><br>

        <label for="category_name">Category Name:</label>
        <input name="category_name" type="text" />

        <br><br>

        <input value="Create" type="submit" />
    </form>
</body>
</html>