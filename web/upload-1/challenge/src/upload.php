<?php
session_start();

if (isset($_FILES['file'])) {
    if ($_FILES['file']['size'] < 1024) {
        if (isset($_SESSION['id'])) 
            $random = $_SESSION['id'];
        else {
            $random = bin2hex(random_bytes(16));
            $_SESSION['id'] = $random;
        }

        $dir = 'uploads/' . $random; 
        if (!is_dir($dir)) 
            mkdir($dir, 0777, true);

        $name = $_FILES['file']['name'];
        $temp_path = $_FILES['file']['tmp_name'];
        if (!exif_imagetype($temp_path)) {
            die("Unsafe file");
        }

        $path = $dir .'/'. $name;
        if (move_uploaded_file($temp_path, $path)) {
            echo '<!DOCTYPE html><html>
<head>
<link rel="stylesheet" href="static/bootstrap.css">
<link rel="stylesheet" href="static/stylesheet.css">
<title>ShareFile</title>
</head>
<body>
<div class="align-middle well">
<div class="container my-5 px-4">
    <h3>ShareFile</h3>
    <p>File has been uploaded successfully... You can find it at <a href="'. $path . '">here</a></p>
</div>
</div>
</body>
</html> ';
        }
    } else {
        die("File too large, this service is meant for small files only");
    }
}
else 
    echo "No file sent";


?>

 


