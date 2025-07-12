<?php include('config.php'); ?>
<!DOCTYPE html>
<html>
<head><title>Upload HIV Data</title></head>
<body>
<h2>Upload HIV Epidemiological CSV</h2>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="csvfile" required>
    <input type="submit" name="upload" value="Upload">
</form>
<?php
if (isset($_POST["upload"])) {
    $file = $_FILES["csvfile"]["tmp_name"];
    $handle = fopen($file, "r");
    fgetcsv($handle); // skip header
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $query = "INSERT INTO patients (household_id, region, gender, age, age_category, marital_status, education_status, wealth_quintile)
                  VALUES ($1, $2, $3, $4, $5, $6, $7, $8)";
        pg_query_params($conn, $query, array(
            $data[0], $data[1], $data[2], $data[3], $data[4],
            $data[5], $data[6], $data[7]
        ));
    }
    echo "Data imported successfully!";
}
?>
</body>
</html>
