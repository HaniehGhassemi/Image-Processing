const Jimp = require('jimp');

async function readImage() {
    const image = await Jimp.read('pic.jpg');
    const imageArray = [];

    image.greyscale().scan(0, 0, image.bitmap.width, image.bitmap.height, (x, y, idx) => {
        const binaryString = image.bitmap.data[idx].toString(2).padStart(8, '0');
        if (!imageArray[y]) {
            imageArray[y] = [];
        }
        imageArray[y][x] = binaryString;
    });

    console.log(imageArray);
}

readImage();