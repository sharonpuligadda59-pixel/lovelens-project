LOVELENS — AI RELATIONSHIP HEALTH ANALYZER (STARTER PROJECT)
===========================================================

WHAT THIS PROJECT INCLUDES
- Home page
- Relationship questionnaire (12 questions)
- Rule-based reflection results
- Healthy relationship advice page
- English / Telugu language switch
- Privacy page and clear-session control
- Responsive pastel pink + lavender design

IMPORTANT
This is a student demo, not a clinical assessment or a validated AI model.
The scoring rules are simple examples to demonstrate project functionality.
It does not diagnose anyone or definitively label a relationship.
The website does not save answers to a database.

HOW TO RUN ON WINDOWS / ASUS LAPTOP
1. Install Python 3.10+ from https://www.python.org/downloads/
   During setup, tick "Add Python to PATH".
2. Extract lovelens_project.zip to a folder, for example Desktop\lovelens_project.
3. Open that folder in File Explorer.
4. Click the address bar, type cmd, and press Enter.
5. Run:
       py -m venv venv
       venv\Scripts\activate
       py -m pip install -r requirements.txt
       py app.py
   If the "py" command does not work, try "python" instead.
6. Open this address in Chrome:
       http://127.0.0.1:5000
7. To stop the server, return to Command Prompt and press Ctrl+C.

PROJECT STRUCTURE
lovelens_project/
  app.py
  requirements.txt
  README.txt
  templates/
    base.html
    index.html
    checkin.html
    results.html
    advice.html
    privacy.html
  static/
    style.css
    app.js

CUSTOMIZATION
- Change questions and basic scoring in app.py.
- Change layout in templates/.
- Change colors and styles in static/style.css.
- Change progress-bar behavior in static/app.js.

SECURITY NOTE
The Flask development server is for local development only. Do not expose it publicly.
Before production deployment, set a strong random secret key, disable debug mode,
review privacy and security requirements, and test the application thoroughly.
