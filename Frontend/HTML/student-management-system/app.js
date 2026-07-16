// ==========================================
// 1. STATE MANAGEMENT (Our Core Data Storage Engine)
// ==========================================
let students = [
    { id: 101, name: "Alex Johnson", role: "Fullstack Dev", score: 88 },
    { id: 102, name: "Bharat Kumar", role: "UI Designer", score: 45 },
    { id: 103, name: "Somnath Patil", role: "Backend Dev", score: 92 }
];

// ==========================================
// 2. DOM CACHING (Finding HTML components)
// ==========================================
const studentForm = document.getElementById("student-form");
const nameInput = document.getElementById("student-name");
const roleInput = document.getElementById("student-role");
const scoreInput = document.getElementById("student-score");
const searchBar = document.getElementById("search-bar");

const tableBody = document.getElementById("student-table-body");
const totalCountEl = document.getElementById("total-count");
const passingCountEl = document.getElementById("passing-count");
const averageScoreEl = document.getElementById("average-score");

// ==========================================
// 3. STATISTICAL METRICS COMPILER
// ==========================================
function updateDashboardMetrics() {
    const total = students.length;
    
    // Using array filter method to discover elements matching a condition
    const passingArray = students.filter(st => st.score >= 50);
    const passingCount = passingArray.length;
    
    // Array reduce operation to compile total value metrics safely
    const sumOfScores = students.reduce((acc, curr) => acc + curr.score, 0);
    const average = total === 0 ? 0 : Math.round(sumOfScores / total);

    // Render results back out directly into dashboard metric targets
    totalCountEl.innerText = total;
    passingCountEl.innerText = passingCount;
    averageScoreEl.innerText = `${average}%`;
}

// ==========================================
// 4. DYNAMIC DOM RENDERER
// ==========================================
function renderStudentTable(dataToDisplay) {
    // Completely purge old records within viewport elements to eliminate duplicates
    tableBody.innerHTML = "";

    // Step through dataset cleanly to structure child components sequentially
    dataToDisplay.forEach((student) => {
        const isPassing = student.score >= 50;
        
        // Assemble dynamic text rows using Template Literals string injection format
        const rowHTML = `
            <tr>
                <td>#${student.id}</td>
                <td><strong>${student.name}</strong></td>
                <td>${student.role}</td>
                <td>${student.score}/100</td>
                <td>
                    <span class="badge ${isPassing ? 'badge-pass' : 'badge-fail'}">
                        ${isPassing ? 'Pass' : 'Fail'}
                    </span>
                </td>
                <td>
                    <button class="btn-delete" onclick="deleteStudent(${student.id})">Remove</button>
                </td>
            </tr>
        `;
        // Inject strings into target tables safely sequentially
        tableBody.innerHTML += rowHTML;
    });
}

// ==========================================
// 5. FUNCTIONAL APP OPERATIONS (Create & Delete)
// ==========================================

// Add student operation
studentForm.addEventListener("submit", (event) => {
    // Intercept event triggers to freeze automatic screen loops
    event.preventDefault();

    // Fabricate new student object payload metrics
    const newStudent = {
        id: Date.now(), // Creates a unique number ID based on the time stamp
        name: nameInput.value.trim(),
        role: roleInput.value.trim(),
        score: parseInt(scoreInput.value)
    };

    // Save payload into local data tracking state
    students.push(newStudent);

    // Sync views
    renderStudentTable(students);
    updateDashboardMetrics();

    // Clear input bars
    studentForm.reset();
});

// Delete student operation
function deleteStudent(targetId) {
    // Re-filter main storage array to remove the matching ID
    students = students.filter(student => student.id !== targetId);
    
    // Render the updated records list
    renderStudentTable(students);
    updateDashboardMetrics();
}

// ==========================================
// 6. FILTER LOGIC (Dynamic Search Field)
// ==========================================
searchBar.addEventListener("input", (event) => {
    const searchTerm = event.target.value.toLowerCase();
    
    // Filter student records matching the entered text keys
    const filteredResults = students.filter(student => 
        student.name.toLowerCase().includes(searchTerm) || 
        student.role.toLowerCase().includes(searchTerm)
    );

    // Refresh display nodes exclusively targeting search parameters
    renderStudentTable(filteredResults);
});

// ==========================================
// 7. INITIAL ENGINE INITIALIZATION
// ==========================================
// Run operations on boot load to pull initial mock values correctly
renderStudentTable(students);
updateDashboardMetrics();
