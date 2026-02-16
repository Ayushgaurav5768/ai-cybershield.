async function askAI() {
    const question = document.getElementById("questionInput").value;

    const response = await fetch("http://127.0.0.1:8000/assistant", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    });

    const data = await response.json();

    document.getElementById("aiResponse").innerText = data.response;
}
