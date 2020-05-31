<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    <title>Save Note</title>
</head>

<body class="">
    <form class="form-group col-md-3 mr-auto ml-auto text-center border border-solid mt-4" action="./save.php" method="GET">
        <h1 class="display-4 mb-3">Save a note</h1>
        <input class="form-control mb-3" name="title" type="text" placeholder="Note Title">
        <input class="form-control mb-3" name="note" type="text" placeholder="Note">
        <button class="btn btn-info m-3 mr-auto ml-auto" type="submit">Save Note</button>
        <a class="btn btn-success" href="./client.php">All Notes</a>
    </form>
</body>

</html>