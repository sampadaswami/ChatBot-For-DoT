from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# M.Tech Subjects data
mtech_subjects = {
    'chemical': {
        'semester 1': [
            'Mathematics for Technology (3 credits)', 
            'Advanced Design of Concrete Structures (3 credits)',
            'Construction Management (3 credits)',
            'Elective-1 (3 credits)', 'Elective-2 (3 credits)',
            'Lab Practice-1 (3 credits)', 'Seminar-1 (1 credit)'
        ],
        'semester 2': [
            'Fluid Mechanics (3 credits)', 'Design of Water & Wastewater Treatment Systems (3 credits)',
            'Elective-3 (3 credits)', 'Elective-4 (3 credits)',
            'Elective-5 (3 credits)', 'Lab Practice-2 (3 credits)', 
            'Seminar-2 (1 credit)'
        ],
        'semester 3': ['Technical Skill Development (3 credits)', 'Elective 6/Directed Study (3 credits)', 'Interim Project (10 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (16 credits)']
    },
    'civil': {
        'semester 1': [
            'Mathematics for Technology (3 credits)', 'Advanced Data Structure (3 credits)',
            'Advanced Database Systems (3 credits)', 'Elective-1 (3 credits)',
            'Elective-2 (3 credits)', 'Lab Practice-1 (3 credits)', 
            'Seminar-1 (1 credit)'
        ],
        'semester 2': [
            'Network System Design (3 credits)', 'Parallel and Distributed Algorithms (3 credits)',
            'Elective-3 (3 credits)', 'Elective-4 (3 credits)', 'Elective-5 (3 credits)', 
            'Lab Practice-2 (3 credits)', 'Seminar-2 (1 credit)'
        ],
        'semester 3': ['Technical Skill Development (3 credits)', 'Elective 6/Directed Study (3 credits)', 'Interim Project (10 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (16 credits)']
    },
    'computer': {
        'semester 1': [
            'Mathematics for Technology (3 credits)', 'Embedded Systems and Real-Time Operating Systems (RTOS) (3 credits)',
            'Advanced Digital Signal Processing (3 credits)', 'Elective-1 (3 credits)', 
            'Elective-2 (3 credits)', 'Lab Practice-1 (3 credits)', 'Seminar-1 (1 credit)'
        ],
        'semester 2': [
            'Communication Networks (3 credits)', 'Analytical Instrumentation (3 credits)',
            'Elective-3 (3 credits)', 'Elective-4 (3 credits)', 'Elective-5 (3 credits)', 
            'Lab Practice-2 (3 credits)', 'Seminar-2 (1 credit)'
        ],
        'semester 3': ['Technical Skill Development (3 credits)', 'Elective 6/Directed Study (3 credits)', 'Interim Project (10 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (16 credits)']
    },
    'electronics': {
        'semester 1': [
            'Mathematics for Technology (3 credits)', 'Advanced Stress Analysis (3 credits)', 
            'Advanced Thermofluids-I (3 credits)', 'Elective-1 (3 credits)', 'Elective-2 (3 credits)', 
            'Lab Practice-1 (3 credits)', 'Seminar-1 (1 credit)'
        ],
        'semester 2': [
            'Computer-Aided Engineering (3 credits)', 'Theory of Vibration and Noise Control (3 credits)', 
            'Elective-3 (3 credits)', 'Elective-4 (3 credits)', 'Elective-5 (3 credits)', 
            'Lab Practice-2 (3 credits)', 'Seminar-2 (1 credit)'
        ],
        'semester 3': ['Technical Skill Development (3 credits)', 'Elective 6/Directed Study (3 credits)', 'Interim Project (10 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (16 credits)']
    },
    'mechanical': {
        'semester 1': [
            'Systems and Network Security (4 credits)', 'Cryptography Advanced (4 credits)',
            'Internet Technologies and Protocols (4 credits)', 'Security Architecture (4 credits)',
            'Operating Systems Security (4 credits)'
        ],
        'semester 2': [
            'Vulnerability Assessment and Penetration Testing (4 credits)', 'Malware and Reverse Engineering (4 credits)',
            'Governance, Risk, and Compliance (4 credits)', 'Mobile Security (4 credits)', 
            'Cyber Forensics (4 credits)'
        ],
        'semester 3': ['Cyber Security - Law and Ethics (4 credits)', 'Blockchain and Cryptocurrencies (4 credits)', 'Interim Project (10 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (16 credits)']
    },
    'information security': {
        'semester 1': [
            'Aerodynamics and Flight Dynamics (3 credits)', 'Propulsion (3 credits)', 'Meteorology (3 credits)', 
            'Navigation and Instruments (3 credits)', 'Structures, Safety, and Systems (3 credits)', 
            'Lab Practice - 1 (3 credits)', 'Seminar - 1 (1 credit)'
        ],
        'semester 2': [
            'Pilot Proficiency License Program - Part 1 (PPLP1) (3 credits)', 'Pilot Proficiency License Program - Part 2 (PPLP2) (3 credits)',
            'Instrument Rating Program - Part 1 (IRP1) (3 credits)', 'Commercial Pilot License Program - Part 1 (CPLP1) (3 credits)', 
            'Commercial Pilot License Program - Part 2 (CPLP2) (3 credits)', 'Lab Practice - 2 (3 credits)', 'Seminar - 2 (1 credit)'
        ],
        'semester 3': ['Soft Skills (3 credits)', 'Federal Aviation Administration (FAA) (3 credits)', 'FAA Certification (8 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (18 credits)']
    },
    'aviation': {
        'semester 1': [
            'Mathematics for Technology (3 credits)', 'Advanced Stress Analysis (3 credits)',
            'Advanced Thermofluids-I (3 credits)', 'Elective-1 (3 credits)',
            'Elective-2 (3 credits)', 'Lab Practice-1 (3 credits)', 'Seminar-1 (1 credit)'
        ],
        'semester 2': [
            'Computer-Aided Engineering (3 credits)', 'Theory of Vibration and Noise Control (3 credits)',
            'Elective-3 (3 credits)', 'Elective-4 (3 credits)', 'Elective-5 (3 credits)', 
            'Lab Practice-2 (3 credits)', 'Seminar-2 (1 credit)'
        ],
        'semester 3': ['Technical Skill Development (3 credits)', 'Elective 6/Directed Study (3 credits)', 'Interim Project (10 credits)'],
        'semester 4': ['Final Project (Dissertation Submission) (16 credits)']
    }
}

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# API route for handling chatbot responses
@app.route('/api/message', methods=['POST'])
def message():
    user_message = request.json.get('message').lower()

    # Responses for M-Tech, PG Diploma, and Undergraduate courses
    if any(keyword in user_message for keyword in ['m-tech', 'mtech', 'master in technology']):
        bot_response = (
            "M-Tech Courses:\n\n"
            "1. M-Tech (Chemical and Biotechnology)\n"
            "2. M-Tech (Civil and Environmental Technology)\n"
            "3. M-Tech (Computer and Information Technology)\n"
            "4. M-Tech (Electronics and Electrical Technology)\n"
            "5. M-Tech (Mechanical and Materials Technology)\n"
            "6. M.Tech (Information Security)\n"
            "7. M.Tech Aviation Technology"
        )

    elif any(keyword in user_message for keyword in ['pg diploma', 'post graduate diploma','pg','PG']):
        bot_response = (
            "PG Diploma Courses:\n\n"
            "1. P.G. Diploma in Water Technology and Management\n"
            "2. P.G. Diploma in Data Science and AI\n"
            "3. P.G. Diploma in Clinical Data Management & Pharmacovigilance\n"
            "4. P.G. Diploma in Electric Mobility\n"
            "5. P.G. Diploma in Advanced Network Security\n"
            "6. P.G. Diploma in Clinical Research Technology\n"
            "7. P.G. Diploma in Industry 4.0 Based Mechatronics & Robotics"
        )

    elif any(keyword in user_message for keyword in ['undergraduate', 'ug', 'UG']):
        bot_response = (
            "Undergraduate Courses:\n\n"
            "1. B.Sc. Animation and VFX\n"
            "2. B.Tech. (Aviation)\n"
            "3. B.Tech. (Data Science)\n"
            "4. B.Sc. Data Science"
        )

        # Additional response for "thank you" or similar phrases
    elif any(keyword in user_message for keyword in ['thank you', 'thanks', 'appreciate it']):
        bot_response = "You're welcome! Please provide your feedback. https://forms.gle/ivfqJatEswdSa1r78"

        # Additional response for "events" or similar phrases
    elif any(keyword in user_message for keyword in ['Events', 'dot events', 'event', 'events','appreciate it']):
        bot_response = "To see event photos, click on this Telegram link: https://t.me/+bORnt37xEMxiYTY1"

       ## Additional response for "Telephone" or similar phrases
    elif any(keyword in user_message for keyword in ['Telephone', 'telephone', 'Telephone No', 'Contact Number', 'appreciate it']):
        bot_response = "+91-020-25622632/33"

       ## Additional response for "Email" or similar phrases
    elif any(keyword in user_message for keyword in ['Email', 'email', 'Email ID', 'Mail', 'appreciate it']):
        bot_response = "hodtech@unipune.ac.in"

      ## Additional response for "Address" or similar phrases
    elif any(keyword in user_message for keyword in ['Address', 'address', 'Location', 'location', 'appreciate it']):
        bot_response = """
    Department of Technology,
    SPPU,
    Ganeshkhind Road,  
    Pune - 411 007  
    Maharashtra State,  
    India.  

    Location  
    https://goo.gl/maps/3Uy4NfXhYesAwwEe6
    """

      ## Additional response for "Adjunct Faculty" or similar phrases
    elif any(keyword in user_message for keyword in ['adjunct faculty', 'adjunct professor', 'faculty', 'staff']):
        bot_response = "Adjunct Faculty here: https://drive.google.com/file/d/1-dM98YIDl8g04UsSTDISOwKLw-fp1TXN/view?usp=sharing"

    elif any(keyword in user_message for keyword in ['visiting faculty', 'visiting professor', 'staff']):  
        bot_response = "Visiting Faculty here: https://drive.google.com/file/d/1xU33RQLBR93PuwKXD4jCzqboF5CuhZlx/view?usp=sharing"
 
    # If the user asks for subjects in a specific M-Tech course
    elif 'subject' in user_message and any(course in user_message for course in mtech_subjects.keys()):
        course = None
        for key in mtech_subjects:
            if key in user_message:
                course = key
                break

        if course:
            # Checking for the semester
            if 'semester' in user_message:
                semester = [sem for sem in ['semester 1', 'semester 2', 'semester 3', 'semester 4'] if sem in user_message]
                if semester:
                    bot_response = f"Subjects for {course.title()} - {semester[0].replace('semester', 'Semester')}:\n\n" + "\n".join(mtech_subjects[course][semester[0]])
                else:
                    bot_response = "Please specify the semester (1, 2, 3, or 4)!"
            else:
                bot_response = "Please specify the semester you want to know about!"
        else:
            bot_response = "Please mention the correct M-Tech course!"
    else:
        bot_response = "Please specify if you want information about M-Tech, PG Diploma, or Undergraduate courses!"

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

