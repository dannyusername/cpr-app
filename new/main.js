const hitButton = document.getElementById('hit-button');
const playButton = document.getElementById('play-button');
const soundChoice = document.getElementById('choice');
const choiSpan = document.getElementById('stype');

let met = new Metronome();

playButton.addEventListener('click', function() {
    met.startStop();
});

soundChoice.addEventListener('click',function() {
    if (chooseSound() == 0) {
        choiSpan = 'Tap';
    }
    else {
        choiSpan = 'Tone';
    }
})
