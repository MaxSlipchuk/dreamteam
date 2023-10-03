const video = document.querySelector("video");


function startPreview() {
  video.muted = true;
  video.currentTime = 1;
  video.volume = 1.0;
  video.muted = false;
  
//   video.playbackRate = 0.5;

  video.play();
}

function stopPreview() {
  video.currentTime = 0;
  video.playbackRate = 1;
  video.pause();
}

let previewTimeout = null;

video.addEventListener("mouseenter", () => {
  startPreview();
  previewTimeout = setTimeout(stopPreview, 35000);
});

video.addEventListener("mouseleave", () => {
  clearTimeout(previewTimeout);
  previewTimeout = null;
  stopPreview();
});