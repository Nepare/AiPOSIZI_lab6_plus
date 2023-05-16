<!DOCTYPE html>
<html>
<head>
    <title>List of {{ model }}</title>
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
        h1 {
            text-align: center;
            margin-top: 0;
        }
        table {
            width: 33%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            border-radius: 4px;
            color: white;
            background-color: #2196F3;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #1976D2;
        }
        .button-create {
            background-color: #4CAF50;
        }
        .button-edit {
            background-color: #FFC107;
        }
        .button-delete {
            background-color: #F44336;
        }
        .button-home {
            background-color: #9E9E9E;
        }
    </style>
</head>
<body>
    <h2>List of {{ model }}</h2>

    <table>
        <tbody>
            % for data in data_list.values():
                <tr>
                    % for x in data.values():
                        % if x != data["id"]:
                            <td>{{ x }}</td>
                        % end
                    % end
                </tr>
            % end
        </tbody>
    </table>

    <div>
        <a href="/{{ model }}/create/" class="button button-create">Create</a>
        <a href="/{{ model }}/edit/" class="button button-edit">Edit</a>
        <a href="/{{ model }}/delete/" class="button button-delete">Delete</a>
    </div>

    <br><br>

    <a href="/" class="button button-home">Home</a>
</body>
</html>
