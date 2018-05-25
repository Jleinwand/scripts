<!doctype html>
<html>
<head>
	<meta charset="utf-8">
	<title>Demo</title>
</head>
<body>
	<a href="http://jquery.com/">jQuery</a>
	<script src "jQuery.js"></script>
	<script>

	//CODE
	window.onload = function() {
		
		alert( "welcome" );

	$(document).ready(function() {
		var chatInterval = 250; //refresh interval in ms
		var $username = $("#userName");
		var $chatOutput = $("#chatOutput");
		var $chatInput = $("#chatInput");
		var $chatSend = $("#chatSend");

		function sendMessage() {
			var userNameString = $userName.val();
			var chatInputString = $chatInput.val();

		$.get("./write.php", {
			username: userNameString,
			text: chatInputString
		});
		
		$username.val("");
		retrieveMessages();
		}

		function retrieveMessages() {
			$.get("./read.php", function (data) {
				$chatOutput.html(data); //chatcontentoutput
		});
		}

		$chatSend.click(function () {
			sendMessage();
		});
		setInterval(function () {
			retrieveMessages();
		}, chatInterval);
	
	});	

	};

	</script>
</body>
</html>
