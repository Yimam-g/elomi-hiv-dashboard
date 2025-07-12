<?php
$host = "localhost";
$dbname = "elomicon_wp602";
$user = "your_pgsql_user";
$password = "your_pgsql_password";
$conn = pg_connect("host=$host dbname=$dbname user=$user password=$password");
if (!$conn) {
    die("Connection failed: " . pg_last_error());
}
?>
