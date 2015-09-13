<?php 
$servername = "mysql1.000webhost.com";
$username = "a8723729_sou";
$password = "12billed";
$dbname = "a8723729_Billmon";
//Create Connection 
$conn = new mysqli($servername,$username,$password,$dbname);
//Check Connection
if($conn->connect_error){
	die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT ind , status , start , end , duration , units, cost FROM DEV1";
$result = $conn->query($sql);
if($result->num_rows > 0){
	echo "<table><tr><th> IND </th> <th> STATUS </th> <th> Start </th> <th> End </th> <th> Duration </th> <th> Units </th> <th> Cost </th></tr>";
	//output data of each row
	while($row = $result->fetch_assoc()){
		echo "<tr><td>" . $row["ind"] . "</td><td>" . $row["status"] . "</td><td>" . $row["start"] . "</td><td>" . $row["end"] ."</td><td>" . $row["duration"] . "</td> <td>" . $row["units"] . "</td> <td>" . $row["cost"] . "</td></tr>"; 
	}
	echo "</table>";
}
else {
	echo "0 results";
}
$conn->close();
?>