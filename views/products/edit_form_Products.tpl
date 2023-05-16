<!DOCTYPE html>
<html>
<head>
    <title>Edit product</title>
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
    <h2>Edit product</h2>

    <form action="/products/edit/" method="post">
        <label for="id">ID:</label>
        <input name="id" type="text" />

        <br><br>

        <label for="new_name">New Name:</label>
        <input name="new_name" type="text" />

        <br><br>

        <label for="new_price">New Price:</label>
        <input name="new_price" type="text" />

        <br><br>

        <label for="new_category">New Category:</label>
        <input name="new_category" type="text" />

        <br><br>

        <input value="Edit" type="submit" />
    </form>
</body>
</html>