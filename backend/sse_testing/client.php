<!DOCTYPE html>
<html>

<head>
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  <title>Client</title>
</head>

<body class="container">

  <h1 class="mb-4">Getting server updates</h1>
  <h5 class="mb-4">Ideally you should see a bunch of notes being sent repeatedly.</h5>
  <div class="ml-auto mr-auto">
  <a class="btn btn-danger m-3" href="./index.php">Home</a>
  <div id="result"></div>

  <script>
    if (typeof(EventSource) !== "undefined") {
      var source = new EventSource("./server.php");
      source.onmessage = function(event) {
        // console.log(JSON.parse(event.data)[0]);
        // console.log(JSON.parse(event.data));
        let notes = JSON.parse(event.data);
        for (let i = 0; i < notes.length; i++)
          document.getElementById("result").innerHTML += `
          <div class="card mb-3" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">${notes[i].title}</h5>
            <p class="card-text">${notes[i].content}</p>
          </div>
        </div>
      `;
        document.getElementById("result").innerHTML += "<br><br><br>";
      };
    } else {
      document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
    }
  </script>

</body>

</html>