let timer;
let totalSeconds = 0;
let running = false;

function updateTimerDisplay() {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    document.getElementById('timer').textContent = 
        `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    // document.getElementById('hour').textContent = 
    //     `${hours.toString().padStart(2, '0')} :`;
    // document.getElementById('minute').textContent = 
    //     `${minutes.toString().padStart(2, '0')} :`;
    // document.getElementById('second').textContent = 
    //     `${seconds.toString().padStart(2, '0')}`;
}

function startTimer() {
    if (!running) {
        running = true;
        timer = setInterval(() => {
            totalSeconds++;
            updateTimerDisplay();
        }, 1000);
        document.getElementById('start').disabled = true;
        document.getElementById('stop').disabled = false;
        document.getElementById('reset').disabled = false;
    }
}

function stopTimer() {
    if (running) {
        running = false;
        clearInterval(timer);
        document.getElementById('start').disabled = false;
        document.getElementById('stop').disabled = true;
    }
}

function resetTimer() {
    stopTimer();
    totalSeconds = 0;
    updateTimerDisplay();
    document.getElementById('reset').disabled = true;
}

document.getElementById('start').addEventListener('click', startTimer);
document.getElementById('stop').addEventListener('click', stopTimer);
document.getElementById('reset').addEventListener('click', resetTimer);

updateTimerDisplay();