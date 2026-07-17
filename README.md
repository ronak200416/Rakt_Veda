# 🩸 Rakt Veda - Blood Test Analysis

Rakt Veda is a multilingual blood test analysis web application that uses AI to analyze blood test reports. Users can either manually enter their blood test values or upload an image of their report for automatic text extraction and analysis.

## 🌐 Live Demo

<img width="1252" height="634" alt="Screenshot 2026-07-18 025817" src="https://github.com/user-attachments/assets/5231fa55-6ea2-45b3-827f-8571c0b4cb71" />
<img width="1328" height="657" alt="Screenshot 2026-07-18 025905" src="https://github.com/user-attachments/assets/9ffd0e8d-f52b-4204-940c-04d226e18bab" />
<img width="1333" height="665" alt="Screenshot 2026-07-18 030025" src="https://github.com/user-attachments/assets/62254ec0-d0cf-4c20-8d0b-9832e296bd9e" />
<img width="1186" height="275" alt="Screenshot 2026-07-18 030107" src="https://github.com/user-attachments/assets/a070c0bd-1ad0-4895-b489-9283af5473a2" />
<img width="1301" height="52" alt="Screenshot 2026-07-18 030323" src="https://github.com/user-attachments/assets/33cec5b4-02ad-4757-b2c6-b6a55258c52d" />
<img width="1289" height="378" alt="Screenshot 2026-07-18 030405" src="https://github.com/user-attachments/assets/da3fa25d-5d0c-44c2-a246-17fc95bc215a" />

## ✨ Features

- **📊 AI-Powered Analysis**: Uses Groq API (Llama 3.3, Llama 3.1, Gemma 2) for intelligent blood test analysis
- **📸 Image Upload with OCR**: Upload blood test report images using Tesseract.js for text extraction
- **🌍 Multilingual Support**: Available in 6 languages
  - हिन्दी (Hindi)
  - বাংলা (Bangla)
  - অসমীয়া (Assamese)
  - मराठी (Marathi)
  - ગુજરાતી (Gujarati)
  - ਪੰਜਾਬੀ (Punjabi)
- **🔐 Secure Login**: Simple authentication system
- **🎨 Modern UI**: Glassmorphism design with dark gradient background
- **📱 Responsive**: Fully responsive for all screen sizes
- **⚡ Fast**: Real-time analysis with auto-fallback between AI models
## 🛠️ Technologies Used

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with glassmorphism effects
- **JavaScript**: Core functionality
- **Font Awesome**: Icons
- **Google Fonts**: Hind Siliguri, Montserrat

### APIs & Libraries
- **Groq API**: AI-powered blood test analysis
  - `llama-3.3-70b-versatile`
  - `llama-3.1-8b-instant`
  - `gemma2-9b-it`
- **Tesseract.js**: OCR for image text extraction
- **Marked.js**: Markdown parsing for formatted responses
## 📁 Project Structure
rakt-veda/
├── index.html # Login page
├── hindi.html # Hindi version
├── bangla.html # Bangla version
├── axomiya.html # Assamese version
├── marathi.html # Marathi version
├── gujrati.html # Gujarati version
├── punjabi.html # Punjabi version
├── README.md # Project documentation
└── assets/ # Images, icons, etc.


## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari)
- Active internet connection for API calls
- (Optional) Web server for local development

### Installation

1. **Clone the repository**

git clone https://github.com/ronak200416/rakt-veda.gitcd rakt-veda

2. Get a Groq API Key
Visit the Groq Console
Sign up for a free account
Generate a new API key

3. Update the API Key
Open the HTML files.
Find the following line:
  const API_KEY = 'your-api-key-here';
Replace your-api-key-here with your actual Groq API key.

4. Run the Application
