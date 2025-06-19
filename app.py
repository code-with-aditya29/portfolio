from flask import Flask, render_template, send_from_directory
import gunicorn
app = Flask(__name__)

# Profile data for the portfolio
profile_data = {
    "name": "Aditya Ajit Tawade",
    "title": "Full Stack Developer",
    "about": "Experienced full stack developer skilled in Python, Flask, and MySQL. Passionate about building scalable web apps.",
    "education": [
        {
            "degree": "BSc-IT",
            "institution": "Shankar Narayan College of Arts and Commerce",
            "year": "2022 - 2025"
        },
        {
            "degree": "12th Grade",
            "institution": "Shankar Narayan College of Arts and Commerce",
            "year": "2020 - 2022"
        }
    ],
    "projects": [
        {
            "title": "Portfolio Website",
            "description": "A responsive personal portfolio with animations and backend integration.",
            "github": "https://github.com/yourusername/portfolio"
        },
        {
            "title": "Chatbot for Healthcare",
            "description": "An AI chatbot to answer health-related queries using predefined Queries.",
            "github": "https://github.com/code-with-aditya29/HealthInkAdvisor"
        },
        {
            "title": "Simple Weather App",
            "description": "A weather forecasting app using API.",
            "github": "https://github.com/code-with-aditya29/weather_app"
        },
        {
            "title": "Jarvis",
            "description": "A fully developed personal voice assistant using Python and APIs from OpenAI & Weather.",
            "github": "https://github.com/code-with-aditya29/aditya_jarvis"
        }
    ]
}

# Route for the single-page portfolio
@app.route('/')
def index():
    return render_template("single_page.html", profile=profile_data)

# Route to download resume
@app.route('/download_resume')
def download_resume():
    return send_from_directory('static', 'resume.pdf', as_attachment=True)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
