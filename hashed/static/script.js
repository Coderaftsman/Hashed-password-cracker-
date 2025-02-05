async function crackPassword() {
    const hashValue = document.getElementById("hash_value").value;
    const hashType = document.getElementById("hash_type").value;

    if (!hashValue) {
        alert("Please enter a hashed password.");
        return;
    }

    const response = await fetch("/crack", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hash_value: hashValue, hash_type: hashType })
    });

    const data = await response.json();
    document.getElementById("result").innerText = `Cracked Password: ${data.password}`;
}
