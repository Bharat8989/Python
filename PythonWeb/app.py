from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # index.html 
    developer_name="Bharat"
    job_title="junior python developer"
    experience_year=1
    python_skill_rating=4.3
    is_available_for_hire=True
    tech_stack=["python","flask","html","git","tailwindcss css"]
    contact_details={
        "email":"bharat@gmail.com",
        "city":"Pune , India",
        "github":"bharat8989://github.com"
    }
    return render_template(
        'index.html',
    name=developer_name,
    title=job_title,
    experience=experience_year,
    rating=python_skill_rating,
    available=is_available_for_hire,
    skill=tech_stack,
    contact=contact_details
    )

if __name__ == '__main__':
    app.run(debug=True)
