<?php include('config.php'); ?>
<!DOCTYPE html>
<html>
<head>
<title>Browse HIV Data</title>
<style>
table {border-collapse: collapse; width: 100%;}
th, td {border: 1px solid #ccc; padding: 6px; text-align: left;}
</style>
</head>
<body>
<h2>All HIV Cases</h2>
<table>
<thead>
<tr><th>ID</th><th>Region</th><th>Gender</th><th>Age</th><th>HIV Status</th></tr>
</thead>
<tbody>
<?php
$query = "SELECT p.patient_id, p.region, p.gender, p.age, h.hiv_status
          FROM patients p
          JOIN hiv_testing h ON p.patient_id = h.patient_id
          LIMIT 100";
$result = pg_query($conn, $query);
while ($row = pg_fetch_assoc($result)) {
    echo "<tr><td>{$row['patient_id']}</td><td>{$row['region']}</td><td>{$row['gender']}</td><td>{$row['age']}</td><td>{$row['hiv_status']}</td></tr>";
}
?>
</tbody>
</table>
</body>
</html>
