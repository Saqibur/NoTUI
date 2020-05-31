<?php
    header('Content-Type: text/event-stream');
    header('Cache-Control: no-cache');

    $jsonFileContents = file_get_contents("notes.json");
    echo "data: {$jsonFileContents}\n\n";
    flush();
?>