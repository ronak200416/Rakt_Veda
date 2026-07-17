<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blood Report Analysis</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tesseract.js@4/dist/tesseract.min.js"></script>
    <style>
        :root {
            --primary-color: #e63946;
            --secondary-color: #457b9d;
            --dark-color: #1d3557;
            --light-color: #f1faee;
            --accent-color: #a8dadc;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            margin: 0;
            padding: 0;
            color: var(--dark-color);
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .header {
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
        }
        
        .header h1 {
            color: var(--primary-color);
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }
        
        .header p {
            color: var(--secondary-color);
            font-size: 1.1rem;
        }
        
        .chat-container {
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            overflow: hidden;
            margin-bottom: 2rem;
        }
        
        .input-group {
            display: flex;
            padding: 1rem;
            background-color: var(--light-color);
            border-radius: 0 0 15px 15px;
        }
        
        #userInput {
            flex: 1;
            padding: 0.8rem 1.2rem;
            border: none;
            border-radius: 30px;
            font-size: 1rem;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        #userInput:focus {
            outline: none;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
        }
        
        #askButton {
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 0 1.5rem;
            margin-left: 0.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 500;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        #askButton:hover {
            background-color: #c1121f;
            transform: translateY(-2px);
        }
        
        #askButton i {
            margin-right: 0.5rem;
        }
        
        #response {
            padding: 1.5rem;
            min-height: 200px;
            max-height: 400px;
            overflow-y: auto;
            background-color: white;
        }
        
        .response-card {
            background-color: var(--light-color);
            border-left: 4px solid var(--secondary-color);
            padding: 1rem;
            border-radius: 0 8px 8px 0;
            margin-bottom: 1rem;
            animation: fadeIn 0.5s ease;
        }
        
        .loading {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1rem;
            color: var(--secondary-color);
        }
        
        .loading i {
            margin-right: 0.5rem;
            animation: spin 1s linear infinite;
        }
        
        .error-message {
            background-color: #ffebee;
            border-left: 4px solid #f44336;
            padding: 1rem;
            border-radius: 0 8px 8px 0;
            color: #c62828;
        }
        
        .upload-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1rem;
            background-color: var(--accent-color);
            border-radius: 15px 15px 0 0;
        }
        
        .upload-btn-wrapper {
            position: relative;
            overflow: hidden;
            display: inline-block;
            margin-bottom: 1rem;
        }
        
        .btn {
            border: 2px dashed var(--secondary-color);
            color: var(--dark-color);
            background-color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .btn:hover {
            background-color: var(--light-color);
        }
        
        .upload-btn-wrapper input[type=file] {
            font-size: 100px;
            position: absolute;
            left: 0;
            top: 0;
            opacity: 0;
            cursor: pointer;
        }
        
        .preview-image {
            max-width: 100%;
            max-height: 200px;
            margin-top: 1rem;
            border-radius: 8px;
            display: none;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Markdown styling */
        #response h1, #response h2, #response h3 {
            color: var(--dark-color);
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }
        
        #response p {
            margin-bottom: 1rem;
            line-height: 1.6;
        }
        
        #response ul, #response ol {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
        }
        
        #response li {
            margin-bottom: 0.5rem;
        }
        
        #response strong {
            color: var(--primary-color);
        }
        
        #response code {
            background-color: var(--accent-color);
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: monospace;
        }
        
        #response pre {
            background-color: var(--accent-color);
            padding: 1rem;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-flask"></i> Blood Report Analysis</h1>
            <p>Upload your blood test report or enter values to get detailed analysis</p>
        </div>
        
        <div class="chat-container">
            <div class="upload-container">
                <div class="upload-btn-wrapper">
                    <button class="btn">
                        <i class="fas fa-upload"></i> Upload Blood Report Image
                    </button>
                    <input type="file" id="fileUpload" accept="image/*" />
                </div>
                <img id="previewImage" class="preview-image" alt="Preview of uploaded blood report">
                <p id="uploadStatus">No image selected</p>
            </div>
            
            <div id="response">
                <div class="response-card">
                    <h3>Welcome to Blood Report Analysis</h3>
                    <p>Upload your blood test report image or enter your values manually to get a detailed analysis.</p>
                    <p>Example: "My hemoglobin is 12.5 g/dL, RBC is 4.2 million cells/mcL. Is this normal?"</p>
                </div>
            </div>
            
            <div class="input-group">
                <input
                    type="text"
                    id="userInput"
                    placeholder="Enter your blood test values or question..."
                    onkeypress="handleKeyPress(event)">
                <button id="askButton" onclick="sendMessage()">
                    <i class="fas fa-paper-plane"></i> Analyze
                </button>
            </div>
        </div>
    </div>

    <script>
        // Handle Enter key press
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        // Image upload handling
        document.getElementById('fileUpload').addEventListener('change', function(event) {
            const file = event.target.files[0];
            const previewImage = document.getElementById('previewImage');
            const uploadStatus = document.getElementById('uploadStatus');
            
            if (file) {
                // Check if the file is an image
                if (!file.type.match('image.*')) {
                    uploadStatus.textContent = 'Please select an image file';
                    uploadStatus.style.color = 'var(--primary-color)';
                    return;
                }
                
                // Show preview
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImage.src = e.target.result;
                    previewImage.style.display = 'block';
                    uploadStatus.textContent = `Selected: ${file.name}`;
                    uploadStatus.style.color = 'var(--secondary-color)';
                    
                    // Extract text from image
                    extractTextFromImage(e.target.result);
                };
                reader.readAsDataURL(file);
            } else {
                previewImage.style.display = 'none';
                uploadStatus.textContent = 'No image selected';
                uploadStatus.style.color = 'inherit';
            }
        });
        
        function extractTextFromImage(imageSrc) {
            const responseDiv = document.getElementById('response');
            
            // Add loading indicator
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'loading';
            loadingDiv.innerHTML = '<i class="fas fa-spinner"></i> Extracting text from blood report...';
            responseDiv.appendChild(loadingDiv);
            responseDiv.scrollTop = responseDiv.scrollHeight;
            
            Tesseract.recognize(
                imageSrc,
                'eng',
                { logger: m => console.log(m) }
            ).then(({ data: { text } }) => {
                // Remove loading indicator
                responseDiv.removeChild(loadingDiv);
                
                // Show extracted text
                const extractedDiv = document.createElement('div');
                extractedDiv.className = 'response-card';
                extractedDiv.style.borderLeftColor = 'var(--accent-color)';
                extractedDiv.innerHTML = `<strong>Extracted Text:</strong><br>${text}`;
                responseDiv.appendChild(extractedDiv);
                
                // Set the extracted text as input
                document.getElementById('userInput').value = `Here is my blood report:\n${text}\nPlease analyze it and tell me if anything is abnormal, what deficiencies I might have, and what I can do to improve my levels.`;
                
                responseDiv.scrollTop = responseDiv.scrollHeight;
            }).catch(error => {
                // Remove loading indicator
                responseDiv.removeChild(loadingDiv);
                
                // Add error message
                const errorDiv = document.createElement('div');
                errorDiv.className = 'error-message';
                errorDiv.innerHTML = `<i class="fas fa-exclamation-triangle"></i> Error extracting text: ${error.message}`;
                responseDiv.appendChild(errorDiv);
                
                responseDiv.scrollTop = responseDiv.scrollHeight;
            });
        }

        async function sendMessage() {
            const input = document.getElementById('userInput').value.trim();
            const responseDiv = document.getElementById('response');
            
            if (!input) {
                const errorDiv = document.createElement('div');
                errorDiv.className = 'error-message';
                errorDiv.innerHTML = '<i class="fas fa-exclamation-circle"></i> Please enter your blood test values or upload a report image';
                responseDiv.appendChild(errorDiv);
                responseDiv.scrollTop = responseDiv.scrollHeight;
                return;
            }
            
            // Add user message
            const userDiv = document.createElement('div');
            userDiv.className = 'response-card';
            userDiv.style.borderLeftColor = 'var(--primary-color)';
            userDiv.innerHTML = `<strong>You:</strong> ${input}`;
            responseDiv.appendChild(userDiv);
            
            // Add loading indicator
            const loadingDiv = document.createElement('div');
            loadingDiv.className = 'loading';
            loadingDiv.innerHTML = '<i class="fas fa-spinner"></i> Analyzing your blood report...';
            responseDiv.appendChild(loadingDiv);
            
            // Clear input
            document.getElementById('userInput').value = '';
            responseDiv.scrollTop = responseDiv.scrollHeight;
            
            try {
                const response = await fetch(
                    'https://openrouter.ai/api/v1/chat/completions',
                    {
                        method: 'POST',
                        headers: {
                            Authorization: 'Bearer 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',
                            'HTTP-Referer': 'https://www.sitename.com',
                            'X-Title': 'Blood Report Analysis',
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            model: 'deepseek/deepseek-r1:free',
                            messages: [{ 
                                role: 'system', 
                                content: 'You are a medical assistant specialized in analyzing blood test reports. Provide detailed analysis of the blood report values, identify any abnormalities or deficiencies, explain their potential causes, and suggest dietary or lifestyle changes to improve the levels. Be professional but use simple language.' 
                            }, { 
                                role: 'user', 
                                content: input 
                            }],
                        }),
                    }
                );
                
                const data = await response.json();
                console.log(data);
                
                // Remove loading indicator
                responseDiv.removeChild(loadingDiv);
                
                // Add bot response
                const botDiv = document.createElement('div');
                botDiv.className = 'response-card';
                const markdownText = data.choices?.[0]?.message?.content || 'No response received.';
                botDiv.innerHTML = `<strong>Analysis:</strong><br>${marked.parse(markdownText)}`;
                responseDiv.appendChild(botDiv);
                
                responseDiv.scrollTop = responseDiv.scrollHeight;
            } catch (error) {
                // Remove loading indicator
                responseDiv.removeChild(loadingDiv);
                
                // Add error message
                const errorDiv = document.createElement('div');
                errorDiv.className = 'error-message';
                errorDiv.innerHTML = `<i class="fas fa-exclamation-triangle"></i> Error: ${error.message}`;
                responseDiv.appendChild(errorDiv);
                
                responseDiv.scrollTop = responseDiv.scrollHeight;
            }
        }
    </script>
</body>
</html>