const playButton = document.getElementById('play-button');
const soundChoice = document.getElementById('choice');
const choiSpan = document.getElementById('stype');

let met = new Metronome();
let taOrTo = 0;

playButton.addEventListener('click', function() {
    met.startStop();
});

soundChoice.addEventListener('click',function() {
    met.chooseSound();
    if (met.soundChoice == 0) {
        choiSpan.textContent = "Tap";
    }
    else {
        choiSpan.textContent = "Tone";
    }
})
