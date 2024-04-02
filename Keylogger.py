<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Key Logger</title>
    <style>
        textarea {
            width: 300px;
            height: 200px;
        }
    </style>
</head>
<body>
    <h1>Key Logger</h1>
    <textarea id="logArea" readonly></textarea>
    <button id="startButton">Start Logging</button>
    <button id="stopButton" disabled>Stop Logging</button>
    
    <script>
        let isLogging = false;
        let logArea = document.getElementById("logArea");
        let startButton = document.getElementById("startButton");
        let stopButton = document.getElementById("stopButton");

        function onKeyPress(event) {
            if (isLogging) {
                let char = event.key;
                logArea.value += char;
                // Send the logged character to the server using AJAX or WebSocket
            }
        }

        function startLogging() {
            isLogging = true;
            logArea.value = "Logging started...\n";
            startButton.disabled = true;
            stopButton.disabled = false;
        }

        function stopLogging() {
            isLogging = false;
            logArea.value += "\nLogging stopped.";
            startButton.disabled = false;
            stopButton.disabled = true;
        }

        document.addEventListener("keypress", onKeyPress);
        startButton.addEventListener("click", startLogging);
        stopButton.addEventListener("click", stopLogging);
    </script>
</body>
</html>
