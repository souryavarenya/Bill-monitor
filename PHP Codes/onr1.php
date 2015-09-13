<?php
$mysql_host = "mysql1.000webhost.com";
$mysql_database = "a8723729_Billmon";
$mysql_user = "a8723729_sou";
$mysql_password = "12billed";

$conn = mysqli_connect($mysql_host, $mysql_user, $mysql_password, $mysql_database);

// Create connection
//$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
echo "<br>";

	$ind = $_POST['7'];

	$str_user_timezone = 'Asia/Kolkata';
	$str_server_timezone = 'UTC';
	$str_server_dateformat = 'Y/m/d-H:i:s';

	date_default_timezone_set($str_server_timezone);
	$date = new DateTime('now');
	$date->setTimezone(new DateTimeZone($str_user_timezone));
	$str_server_now = $date->format($str_server_dateformat);
	//var = echo $str_server_now;

$sqlon = sprintf("INSERT INTO DEV1 (ind, status, start) VALUES (%d, 1,'%s')",(int)$ind, $str_server_now);


if (mysqli_query($conn, $sqlon)) {
	echo "New record created successfully";
} else {
	echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

$arrang = "ALTER TABLE DEV1 ORDER BY ind ASC";

if (mysqli_query($conn, $arrang)) {
	echo "arranged";
} else {
	echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

$conn->close();
?>

