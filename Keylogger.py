<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Key Logger</title>
</head>
<body>
    <h1>Web Key Logger</h1>
    <textarea id="logArea" rows="10" cols="50" readonly></textarea>
    <button id="startButton">Start Logging</button>
    <button id="stopButton">Stop Logging</button>

    <script>
        let isLogging = false;
        let logArea = document.getElementById('logArea');
        let startButton = document.getElementById('startButton');
        let stopButton = document.getElementById('stopButton');

        startButton.addEventListener('click', function() {
            isLogging = true;
            logArea.value = 'Logging started...\n';
            startButton.disabled = true;
            stopButton.disabled = false;
        });

        stopButton.addEventListener('click', function() {
            isLogging = false;
            logArea.value += '\nLogging stopped.';
            startButton.disabled = false;
            stopButton.disabled = true;
        });

        document.addEventListener('keydown', function(event) {
            if (isLogging) {
                let char = event.key;
                if (char.length === 1) {
                    logArea.value += char;
                }
            }
        });
    </script>
</body>
</html>
