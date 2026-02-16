const API_BASE = "http://127.0.0.1:8000";

let chartInstance = null;

async function loadDashboard() {
    try {
        const response = await fetch(`${API_BASE}/dashboard`);
        const data = await response.json();

        document.getElementById("totalScans").innerText = data.total_scans;
        document.getElementById("phishingCount").innerText = data.phishing_count;
        document.getElementById("safeCount").innerText = data.safe_count;

        createChart(data.phishing_count, data.safe_count);

        loadRecentScans();

    } catch (error) {
        console.error("Error fetching dashboard data:", error);
    }
}

function createChart(phishing, safe) {
    const ctx = document.getElementById("threatChart").getContext("2d");

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Phishing", "Safe"],
            datasets: [{
                data: [phishing, safe],
                backgroundColor: ["#ef4444", "#22c55e"]
            }]
        },
        options: {
            responsive: true
        }
    });
}

async function loadRecentScans() {
    try {
        const response = await fetch(`${API_BASE}/recent-scans`);
        const data = await response.json();

        const tableBody = document.querySelector("#scanTable tbody");
        tableBody.innerHTML = "";

        data.forEach(scan => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${scan.url}</td>
                <td style="color:${scan.prediction === "Phishing" ? "red" : "green"}">
                    ${scan.prediction}
                </td>
                <td>${scan.risk_score}%</td>
                <td>${new Date(scan.created_at).toLocaleString()}</td>
            `;

            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error("Error loading recent scans:", error);
    }
}

window.onload = loadDashboard;
