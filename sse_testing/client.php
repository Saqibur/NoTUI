<!DOCTYPE html>
<html>
  <head>
    <title>Client</title>
  </head>
<body>

<h1>Getting server updates</h1>
<h5>Ideally you should see a bunch of notes being sent repeatedly.</h5>
<div id="result"></div>

<script>
if(typeof(EventSource) !== "undefined") {
  var source = new EventSource("http://127.0.0.1:6969/server.php");
  source.onmessage = function(event) {
    // console.log(JSON.parse(event.data)[0]);
    // console.log(JSON.parse(event.data));
    let notes = JSON.parse(event.data);
    for (let i = 0; i < notes.length; i++)
      document.getElementById("result").innerHTML += `
        <h1>${notes[i].title}</h1>
        <h5>${notes[i].content}</h1>
        <br><hr>
      `;
      document.getElementById("result").innerHTML += "<br><br><br>";
  };
} else {
  document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
}
</script>

</body>
</html>

