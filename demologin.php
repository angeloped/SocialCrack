<?php
if(isset($_POST["user"]) && isset($_POST["pass"]))){
	if($_POST["user"] == "admin" && $_POST["pass"] == "myloves2/3/21"){
		die("Nice try! Success.")
	}else{
		die("Error");
	}
}
?>
