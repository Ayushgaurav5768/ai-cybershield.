let gaugeChart = null;

document.addEventListener("DOMContentLoaded", () => {

    const button = document.getElementById("scanBtn");

    button.addEventListener("click", async (event) => {

        event.preventDefault(); // HARD STOP any submission

        const url = document.getElementById("urlInput").value.trim();

        if (!url) {
            alert("Please enter a URL");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/scan", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ url })
            });

            const data = await response.json();

            document.getElementById("result").innerText =
                "Prediction: " + data.prediction;

            createGauge(data.risk_score);

        } catch (err) {
            console.error(err);
        }
    });
});

function createGauge(score) {

    const ctx = document.getElementById("riskGauge").getContext("2d");

    if (gaugeChart) gaugeChart.destroy();

    let color = "#22c55e";
    if (score > 60) color = "#ef4444";
    else if (score > 30) color = "#f59e0b";

    gaugeChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            datasets: [{
                data: [score, 100 - score],
                backgroundColor: [color, "#1f2937"],
                borderWidth: 0
            }]
        },
        options: {
            cutout: "80%",
            plugins: { tooltip: { enabled: false } }
        }
    });

    animateCounter(score);
}

function animateCounter(target) {

    const el = document.getElementById("riskPercent");
    let count = 0;

    const interval = setInterval(() => {
        if (count >= target) {
            clearInterval(interval);
        }
        el.innerText = count + "%";
        count++;
    }, 10);
}
