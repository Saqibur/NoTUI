<?php
    header('Content-Type: text/event-stream');
    header('Cache-Control: no-cache');

    $jsonFileContents = file_get_contents("data_file.json");
    echo "data: Data From Server: {$jsonFileContents}\n\n";
    flush();
?>