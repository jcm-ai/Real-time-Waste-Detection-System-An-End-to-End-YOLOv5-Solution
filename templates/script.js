document.getElementById('uploadBtn').addEventListener('click', () => {
    document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('imagePreview').src = e.target.result;
            document.getElementById('imagePreview').style.display = "block";
            document.getElementById('video').style.display = "none";
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('predictBtn').addEventListener('click', function() {
    const imageElement = document.getElementById('imagePreview');
    if (!imageElement.src) {
        alert("Please upload an image first.");
        return;
    }

    document.getElementById('loading').style.display = "flex"; // Show loading spinner

    const base64Data = imageElement.src.split(',')[1];

    fetch("../predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: base64Data }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `<img class="preview" src="data:image/jpeg;base64,${data.image}" />`;
        document.getElementById('loading').style.display = "none"; // Hide loading spinner
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('result').innerText = "Prediction failed!";
        document.getElementById('loading').style.display = "none";
    });
});

// Dark Mode Toggle
document.getElementById('themeToggle').addEventListener('click', () => {
    document.body.classList.toggle("dark-mode");
});
