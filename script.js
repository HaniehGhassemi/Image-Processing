// بارگیری تصویر از سیستم کاربر
const inputImage = document.getElementById('input-image');
const Image = document.getElementById('image');

inputImage.addEventListener('change', function(e) {
    Image.src = URL.createObjectURL(e.target.files[0]);
    
},false);
Image.onload= function(){
    const img = cv.imread(Image);
    cv.imshow('image-container', img);
    img.delete();
}
// ذخیره تصویر در محل دیگری از سیستم
const saveBtn = document.getElementById('save-btn');

saveBtn.addEventListener('click', function() {
  const canvas = document.getElementsByTagName('canvas')[0];
  const link = document.createElement('a');
  link.download = 'output.png';
  link.href = canvas.toDataURL();
  link.click();
});