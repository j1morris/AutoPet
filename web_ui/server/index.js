console.log('Hello world!');

// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON

const statsDiv = document.querySelector('#statistics');

// let requestURL = 'http://mustin.workisboring.com:5000/sample.json';
let requestURL = 'http://mustin.workisboring.com:5000/stats.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
  const statistics = request.response;
  populateStatistics(statistics);
}

function populateStatistics(jsonObj) {
  let similarity = jsonObj['similarity'];
  let refid      = jsonObj['refid'];
  let detected   = jsonObj['detected'];

  for (let i = 0; i < similarity.length; i++) {
    const statsPara = document.createElement('p');
    statsPara.textContent = `${similarity[i]}, ${refid[i]}, ${detected[i]}`;
    statsDiv.appendChild(statsPara);
  }

  // const statsPara = document.createElement('p');
  // statsPara.textContent = jsonObj['hello'];
  // statsDiv.appendChild(statsPara);
}

// https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API

const record = document.querySelector('#record');
const stop = document.querySelector('#stop');
const soundClipsDiv = document.querySelector('#soundClips');

stop.disabled = true;

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  console.log('getUserMedia supported.');

  const constraints = { audio: true };
  let chunks = [];

  let onSuccess = function(stream) {
    const mediaRecorder = new MediaRecorder(stream);

    record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";

      stop.disabled = false;
      record.disabled = true;
    }

    stop.onclick = function() {
      mediaRecorder.stop();
      console.log(mediaRecorder.state);
      console.log("recorder stopped");
      record.style.background = "";

      stop.disabled = true;
      record.disabled = false;
    }

    mediaRecorder.ondataavailable = function(e) {
      console.log("MediaRecorder.ondataavailable() called.");
      chunks.push(e.data);
    }

    mediaRecorder.onstop = function(e) {
      console.log("MediaRecorder.stop() called.");

      const clipContainer = document.createElement('article');
      const audio = document.createElement('audio');

      clipContainer.classList.add('clip');
      audio.setAttribute('controls', '');

      clipContainer.style.width = "100%";
      audio.style.width = "100%";

      clipContainer.appendChild(audio);
      soundClipsDiv.appendChild(clipContainer);

      const blob = new Blob(chunks, {'type' : 'audio/ogg; codecs=opus' });
      chunks = [];
      const audioURL = window.URL.createObjectURL(blob);
      audio.src = audioURL;
    }
  } 

  let onError = function(err) {
    console.log('The following getUserMedia error occured: ' + err);
  }

  navigator.mediaDevices.getUserMedia(constraints).then(onSuccess, onError);
}

else {
  console.log('getUserMedia not supported on your browser!');
}
