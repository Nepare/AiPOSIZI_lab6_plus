<!DOCTYPE html>
<html>
<head>
    <title>Edit order</title>
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
    <h2>Edit order</h2>
    <form action="/orders/edit/" method="post">
        <label for="id">ID:</label>
        <input name="id" type="text" />

        <br><br>

        <label for="new_user_id">NewUserId:</label>
        <input name="new_user_id" type="text" />

        <br><br>

        <label for="new_product_name">NewProductName:</label>
        <input name="new_product_name" type="text" />

        <br><br>

        <label for="new_quantity">NewQuantity:</label>
        <input name="new_quantity" type="text" />

        <br><br>

        <input value="Edit" type="submit" />
    </form>
</body>
</html>
