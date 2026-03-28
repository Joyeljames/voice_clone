async function generateTTS() {
    let text = document.getElementById("textInput").value;

    let player = document.getElementById("audioPlayer");
    player.src = "";
    
    alert("Generating voice... ⏳");

    let formData = new FormData();
    formData.append("text", text);

    let response = await fetch("/tts/", {
        method: "POST",
        body: formData
    });

    let blob = await response.blob();

    if (blob.size === 0) {
        alert("Audio failed!");
        return;
    }

    let url = URL.createObjectURL(blob);
    player.src = url;

    document.getElementById("downloadBtn").href = url;
}