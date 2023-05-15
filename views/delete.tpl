<!DOCTYPE html>
<html>
<head>
    <title>Delete {{model}}</title>
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
            background-color: red;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: darkred;
        }
    </style>
</head>
<body>
    <h2>Delete {{model}}</h2>
    <form action="/{{model}}/delete/" method="post">
        <label for="id">ID:</label>
        <input name="id" type="text" />

        <br><br>

        <input value="Delete" type="submit" />
    </form>
</body>
</html>





