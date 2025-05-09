const countSpan = document.getElementById('count');
const perfSpan = document.getElementById('perfect');
const earlySpan = document.getElementById('early');
const lateSpan = document.getElementById('late');
const scoreSpan = document.getElementById('score');
const hitButton = document.getElementById('hit-button');

let counter = 0;
let perfect = 0;
let early = 0;
let late = 0;
let score = 0;

hitButton.addEventListener('click', function() {
    counter++;
    countSpan.textContent = counter;
    scoreSpan.textContent = (perfect * 5) + (early * 1) + (late * 1);
})
