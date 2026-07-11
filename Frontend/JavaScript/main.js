// =============================
// DOM Selection
// =============================

const studentName = document.getElementById("student-name");
const studentAge = document.getElementById("student-age");
const studentBranch = document.getElementById("student-branch");
const studentMarks = document.getElementById("student-marks");

const addBtn = document.getElementById("add-btn");

const studentList = document.getElementById("student-list");

const totalStudents = document.getElementById("total-students");
const averageMarks = document.getElementById("average-marks");
const topperName = document.getElementById("topper-name");

// =============================
// Local Storage
// =============================

let students = JSON.parse(localStorage.getItem("students")) || [];

displayStudents();
updateStatistics();

// =============================
// Add Student
// =============================

addBtn.addEventListener("click", () => {

    const name = studentName.value.trim();
    const age = Number(studentAge.value);
    const branch = studentBranch.value;
    const marks = Number(studentMarks.value);

    if (
        name === "" ||
        age === 0 ||
        branch === "" ||
        studentMarks.value === ""
    ) {

        alert("Please Fill All Fields");

        return;
    }

    const student = {

        id: Date.now(),

        name,

        age,

        branch,

        marks

    };

    students.push(student);

    saveData();

    displayStudents();

    updateStatistics();

    clearForm();

});

// =============================
// Display Students
// =============================

function displayStudents() {

    studentList.innerHTML = "";

    students.forEach((student) => {

        let status = "";

        let statusClass = "";

        if (student.marks >= 40) {

            status = "PASS";

            statusClass = "pass";

        } else {

            status = "FAIL";

            statusClass = "fail";

        }

        studentList.innerHTML += `

        <div class="student-card">

            <h2>${student.name}</h2>

            <p><strong>Age :</strong> ${student.age}</p>

            <p><strong>Branch :</strong> ${student.branch}</p>

            <p><strong>Marks :</strong> ${student.marks}</p>

            <p class="${statusClass}">
                <strong>Status :</strong> ${status}
            </p>

            <div class="card-buttons">

                <button
                    class="edit-btn"
                    onclick="editStudent(${student.id})">

                    Edit

                </button>

                <button
                    class="delete-btn"
                    onclick="deleteStudent(${student.id})">

                    Delete

                </button>

            </div>

        </div>

        `;

    });

}

// =============================
// Statistics
// =============================

function updateStatistics() {

    totalStudents.innerText = students.length;

    if (students.length === 0) {

        averageMarks.innerText = "0";

        topperName.innerText = "-";

        return;

    }

    let total = 0;

    let topper = students[0];

    students.forEach((student) => {

        total += student.marks;

        if (student.marks > topper.marks) {

            topper = student;

        }

    });

    averageMarks.innerText =
        (total / students.length).toFixed(2);

    topperName.innerText =
        `${topper.name} (${topper.marks})`;

}

// =============================
// Save Local Storage
// =============================

function saveData() {

    localStorage.setItem(

        "students",

        JSON.stringify(students)

    );

}

// =============================
// Clear Form
// =============================

function clearForm() {

    studentName.value = "";

    studentAge.value = "";

    studentBranch.value = "";

    studentMarks.value = "";

}


// =============================
// Delete Student
// =============================

function deleteStudent(id) {

    const confirmDelete = confirm("Are you sure you want to delete this student?");

    if (!confirmDelete) return;

    students = students.filter((student) => {

        return student.id !== id;

    });

    saveData();

    displayStudents();

    updateStatistics();

}

// =============================
// Edit Student
// =============================

function editStudent(id) {

    const student = students.find((student) => {

        return student.id === id;

    });

    if (!student) return;

    studentName.value = student.name;
    studentAge.value = student.age;
    studentBranch.value = student.branch;
    studentMarks.value = student.marks;

    // Remove old student
    students = students.filter((student) => {

        return student.id !== id;

    });

    saveData();

    displayStudents();

    updateStatistics();

}

// =============================
// Search Student
// =============================

const search = document.getElementById("search");

search.addEventListener("keyup", function () {

    const value = this.value.toLowerCase();

    const cards = document.querySelectorAll(".student-card");

    cards.forEach((card) => {

        const name = card.querySelector("h2").innerText.toLowerCase();

        if (name.includes(value)) {

            card.style.display = "block";

        } else {

            card.style.display = "none";

        }

    });

});

// =============================
// Enter Key Support
// =============================

studentMarks.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

        addBtn.click();

    }

});

// =============================
// Console Message
// =============================

console.log("Student Management System Loaded Successfully");