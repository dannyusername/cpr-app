class Metronome {
    constructor(tempo = 120) {
        this.audcont = null;
        this.isRunning = false;
        this.notesInQueue = [];
        this.tempo = tempo;
        this.lookahead = 25.0;
        this.scheduleAheadTime = 0.1;
        this.nextNoteTime = 0.0;
        this.intervalID = null;

        this.soundChoice = 0;
    }

    chooseSound() {
        if (this.soundChoice == 0) {
            this.soundChoice = 1;
        }
        else {
            this.soundChoice = 0;
        }
        return this.soundChoice;
    }

    nextNote() {
        let secondsPerBeat = 60.0 / this.tempo;
        this.nextNoteTime += secondsPerBeat;
    }
    
    scheduleNote(time) {
        this.notesInQueue.push({time: time});

        const envelope = this.audcont.createGain();
        envelope.gain.value = 1;

        if (this.soundChoice == 0) {
            const tapper = this.audcont.createMediaElementSource(document.getElementById('tap'));

            tapper.connect(envelope);
            envelope.connect(this.audcont.destination);

            tapper.start(time);
            tapper.stop(time + 0.03);
        }
        else {
            const toner = this.audcont.createMediaElementSource(document.getElementById('tone'));

            toner.connect(envelope);
            envelope.connect(this.audcont.destination);
            
            toner.start(time);
            toner.stop(time + 0.03);
        }
    }

    scheduler() {
        while (this.nextNoteTime < this.audcont.currentTime + this.scheduleAheadTime) {
            this.scheduleNote(this.nextNoteTime);
            this.nextNote();
        }
    }

    start() {
        if (this.isRunning) {
            return;
        }

        if (this.audcont == null) {
            this.audcont = new (window.AudioContext || window.webkitAudioContext)();
        }
    
        this.isRunning = true;
        this.nextNoteTime = audcont.currentTime + 0.05;
    
        this.intervalID = setInterval(() => this.scheduler(), this.lookahead);
    }

    stop() {
        this.isRunning = false;
        clearInterval(this.intervalID);
    }

    startStop() {
        if (this.isRunning) {
            this.stop();
        }
        else {
            this.start();
        }
    }
}
