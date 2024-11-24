<?php
$conn = new mysqli('localhost', 'root', '', 'school');
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$student_details = "";
if (isset($_POST['regNo'])) {
    $regNo = $_POST['regNo'];
    $sql = "SELECT * FROM students WHERE reg_no = '$regNo'";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $student_details = "<h3>Student Details</h3>
                            <p><strong>Registration Number:</strong> " . $row["reg_no"] . "</p>
                            <p><strong>Name:</strong> " . $row["name"] . "</p>
                            <p><strong>Email:</strong> " . $row["email"] . "</p>
                            <p><strong>Course:</strong> " . $row["course"] . "</p>";
    } else {
        $student_details = "No student found with the provided registration number.";
    }
}
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
</head>
<body>
    <h2>Student Details</h2>
    <?php echo $student_details; ?>
</body>
</html>
