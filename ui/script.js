// This file contains basic UI JS

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let img = new Image();

async function loadImage() {
    const fileInput = document.getElementById('formFile');
    const file = fileInput.files[0];

    img.src = URL.createObjectURL(file);

    img.onload = function() {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0);
    }
}

let startX, startY, endX, endY;
let dragging = false;

function getCanvasCoords(e) {
    const rect = canvas.getBoundingClientRect();

    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    return {
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY
    };
}

canvas.addEventListener("mousedown", e => {
    const pos = getCanvasCoords(e);

    startX = pos.x;
    startY = pos.y;

    dragging = true;
});

canvas.addEventListener("mousemove", e => {
    if (!dragging) return;

    const pos = getCanvasCoords(e);

    endX = pos.x;
    endY = pos.y;

    const x = Math.min(startX, endX);
    const y = Math.min(startY, endY);
    const w = Math.abs(endX - startX);
    const h = Math.abs(endY - startY);

    // Clear canvas and draw original image
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0);

    // Draw dark overlay over entire canvas
    ctx.fillStyle = 'rgba(0,0,0,0.2)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw the selection area from the image on top of overlay
    ctx.drawImage(img, x, y, w, h, x, y, w, h);

    // Draw selection border
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 1;
    ctx.strokeRect(x-1, y-1, w+2, h+2);
});

canvas.addEventListener("mouseup", e => {
    dragging = false;
});

async function cropImage() {
    let width = endX - startX;
    let height = endY - startY;

    const cropped = document.createElement("canvas");
    cropped.width = width;
    cropped.height = height;

    const croppedCtx = cropped.getContext("2d");

    croppedCtx.drawImage(
        canvas,
        startX, startY, width, height,
        0, 0, width, height
    );

    const blob = await new Promise(resolve => cropped.toBlob(resolve));

    const arrayBuffer = await blob.arrayBuffer();
    const bytes = Array.from(new Uint8Array(arrayBuffer));

    const savedPath = await window.pywebview.api.save_temp_image(bytes, "cropped.png");

    console.log(savedPath);
}