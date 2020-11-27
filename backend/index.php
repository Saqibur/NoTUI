<html>

<body>
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() {
            function magic() {
                // alert('json');
                $.ajax({
                    url: 'data_file.json',
                    dataType: 'json',
                    success: function(data) {
                        console.log(data);

                        console.log(data.x);
                        var canvas = document.getElementById("myCanvas");
                        var ctx = canvas.getContext("2d");
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        ctx.fillStyle = "#FF0000";
                        ctx.fillRect(data.x, data.y, data.w, data.h);
                        ctx.font = "30px Arial";
                        ctx.fillText(data.label, data.x, data.y);
                        repeater = setTimeout(magic, 500);
                    }
                });
            }
            var repeater;

            magic();
        });
    </script>
    <canvas id="myCanvas" width="1000px" height="700px" style="border:1px solid #c3c3c3;">
    </canvas>

</body>

</html>