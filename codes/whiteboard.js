// document.addEventListener("DOMContentLoaded", () => {
//     const canvas = document.getElementById('canvas');
//     const ctx = canvas.getContext('2d');
//     let drawing = false;
//     canvas.addEventListener('mousedown', () => {
//         drawing = true;
//     });

//     canvas.addEventListener('mouseup', () => {
//         drawing = false;
//         ctx.beginPath();
//     });

//     canvas.addEventListener('mousemove', draw);

//     function draw(event) {
//         if (!drawing) return;

//         ctx.lineWidth = 5;
//         ctx.lineCap = 'round';
//         ctx.strokeStyle = 'black';

//         ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
//         ctx.stroke();
//         ctx.beginPath();
//         ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
//     }

//     document.getElementById('saveBtn').addEventListener('click', () => {
//         const imgData = canvas.toDataURL('image/png');

//         fetch('/save', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ imgData: imgData })
//         })
//         .then(response => response.text())
//         .then(data => {
//             alert(data);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('Error: ' + error.message);
//         });
//     });
// });

// new code
// document.addEventListener("DOMContentLoaded", () => {
//     const canvas = document.getElementById('canvas');
//     const ctx = canvas.getContext('2d');
//     let drawing = false;

//     // Function to set canvas background color
//     function setCanvasBackground() {
//         ctx.fillStyle = 'white'; // Set your desired background color here
//         ctx.fillRect(0, 0, canvas.width, canvas.height);
//     }

//     // Initialize the canvas with a white background
//     setCanvasBackground();

//     canvas.addEventListener('mousedown', () => {
//         drawing = true;
//     });

//     canvas.addEventListener('mouseup', () => {
//         drawing = false;
//         ctx.beginPath();
//     });

//     canvas.addEventListener('mousemove', draw);

//     function draw(event) {
//         if (!drawing) return;

//         ctx.lineWidth = 5;
//         ctx.lineCap = 'round';
//         ctx.strokeStyle = 'black';

//         ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
//         ctx.stroke();
//         ctx.beginPath();
//         ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
//     }

//     document.getElementById('saveBtn').addEventListener('click', () => {
//         // Temporarily set the background to white before saving
//         setCanvasBackground();

//         const imgData = canvas.toDataURL('image/png');

//         fetch('/save', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ imgData: imgData })
//         })
//         .then(response => response.text())
//         .then(data => {
//             alert(data);
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('Error: ' + error.message);
//         });
//     });
// });
document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let drawing = false;

    canvas.width = 800; // Set the canvas width
    canvas.height = 600; // Set the canvas height

    // Function to set canvas background color
    function setCanvasBackground() {
        // Create a temporary canvas to draw the background and current canvas content
        const tempCanvas = document.createElement('canvas');
        const tempCtx = tempCanvas.getContext('2d');
        tempCanvas.width = canvas.width;
        tempCanvas.height = canvas.height;

        // Fill the temporary canvas with white background
        tempCtx.fillStyle = 'white';
        tempCtx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);

        // Draw the current canvas content on the temporary canvas
        tempCtx.drawImage(canvas, 0, 0);

        // Get the data URL of the temporary canvas
        return tempCanvas.toDataURL('image/png');
    }

    canvas.addEventListener('mousedown', () => {
        drawing = true;
    });

    canvas.addEventListener('mouseup', () => {
        drawing = false;
        ctx.beginPath();
    });

    canvas.addEventListener('mousemove', draw);

    function draw(event) {
        if (!drawing) return;

        ctx.lineWidth = 5;
        ctx.lineCap = 'round';
        ctx.strokeStyle = 'black';

        ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
    }

    document.getElementById('saveBtn').addEventListener('click', () => {
        // Get the data URL of the canvas with a white background
        const imgData = setCanvasBackground();

        fetch('/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ imgData: imgData })
        })
        .then(response => response.text())
        .then(data => {
            alert(data);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error: ' + error.message);
        });
    });
});

