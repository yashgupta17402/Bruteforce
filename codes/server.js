const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
// var a=0;
app.use(bodyParser.urlencoded({ extended: true, limit: '50mb' }));
app.use(bodyParser.json({ limit: '50mb' }));

app.use(express.static('public'));

app.post('/save', (req, res) => {
    const imgData = req.body.imgData;
    // a+=1;
    // console.log(req.body)
    const base64Data = imgData.replace(/^data:image\/png;base64,/, "");
    const filePath = path.join(__dirname, 'public', 'drawing'+'.png');

    fs.writeFile(filePath, base64Data, 'base64', (err) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error saving image');
        } else {
            res.status(200).send('Image saved successfully');
        }
    });
});

app.listen(PORT, () => {
    console.log('Server is running on http://localhost:${PORT}');
});