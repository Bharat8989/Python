// Backend endpoint configuration URL
// Automatically handles access via Flask server (port 5000), Live Server (port 5500), or file://
const API_BASE = (window.location.origin.startsWith("http") && !window.location.port.includes("5500") && !window.location.port.includes("3000"))
    ? window.location.origin
    : "http://127.0.0.1:5000";

const API_URL = `${API_BASE}/api/students`;

// Helper: Display inline message to user
function showAlert(message, type = "success") {
    const alertBox = document.getElementById("alertBox");
    if (!alertBox) {
        alert((type === "success" ? "Success: " : "Error: ") + message);
        return;
    }
    alertBox.textContent = message;
    alertBox.className = `alert alert-${type}`;
    alertBox.style.display = "block";

    if (type === "success") {
        setTimeout(() => {
            alertBox.style.display = "none";
        }, 5000);
    }
}

// Helper: Escape HTML to prevent XSS injection
function escapeHtml(value) {
    if (value === null || value === undefined) return "";
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// 1. Submit Form Data to Backend via POST Request
const studentForm = document.getElementById("studentForm");
const submitBtn = document.getElementById("submitBtn");

studentForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const ageRaw = document.getElementById("age").value.trim();
    const course = document.getElementById("course").value.trim();

    // Client-side validation
    if (!name || !email || !ageRaw || !course) {
        showAlert("All fields are required.", "error");
        return;
    }

    const age = parseInt(ageRaw, 10);
    if (isNaN(age) || age < 1 || age > 120) {
        showAlert("Please enter a valid age between 1 and 120.", "error");
        return;
    }

    const studentData = { name, email, age, course };

    try {
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = "Registering...";
        }

        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(studentData)
        });

        const result = await response.json().catch(() => ({}));

        if (response.ok) {
            showAlert(result.message || "Student registered successfully!", "success");
            studentForm.reset();
            await loadStudents();
        } else {
            showAlert(result.error || "Failed to register student.", "error");
        }
    } catch (err) {
        console.error("Connection failed:", err);
        showAlert("Unable to connect to server. Please verify that your Flask backend application is running!", "error");
    } finally {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = "Submit Registration";
        }
    }
});

// 2. Fetch and Render Student Directory Listings via GET Request
async function loadStudents() {
    const tbody = document.querySelector("#studentTable tbody");
    if (!tbody) return;

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            tbody.innerHTML = `<tr><td colspan="5" class="empty-row">Failed to load records: ${escapeHtml(errData.error || 'Server error')}</td></tr>`;
            return;
        }

        const students = await response.json();

        if (!Array.isArray(students) || students.length === 0) {
            tbody.innerHTML = `<tr><td colspan="5" class="empty-row">No students registered yet.</td></tr>`;
            return;
        }

        const rowsHtml = students.map(student => `<tr>
            <td>${escapeHtml(student.id)}</td>
            <td>${escapeHtml(student.name)}</td>
            <td>${escapeHtml(student.email)}</td>
            <td>${escapeHtml(student.age)}</td>
            <td>${escapeHtml(student.course)}</td>
        </tr>`).join("");

        tbody.innerHTML = rowsHtml;
    } catch (err) {
        console.error("Error loading student records:", err);
        tbody.innerHTML = `<tr><td colspan="5" class="empty-row">Unable to connect to backend server.</td></tr>`;
    }
}

// Fire data loading immediately when DOM is ready
document.addEventListener("DOMContentLoaded", loadStudents);

