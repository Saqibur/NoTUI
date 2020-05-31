<?php

$oldNotes = json_decode(file_get_contents("notes.json"), true);
$newNote = ['title' => $_GET["title"], 'content' => $_GET["note"]];
array_push($oldNotes, $newNote);
file_put_contents("notes.json", json_encode($oldNotes));
header('Location: input.php');
?>
