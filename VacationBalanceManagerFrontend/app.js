const vacationForm = document.getElementById('vacation-form');
const startDateInput = document.getElementById('start-date');
const endDateInput = document.getElementById('end-date');
const daysRequestedInput = document.getElementById('days-requested');
const vacationType = document.getElementById('vacation-type');
const annualBalanceSpan = document.getElementById('annual-balance');
const sickBalanceSpan = document.getElementById('sick-balance');


window.onload = function() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', "http://127.0.0.1:8000/balanceManager");
    
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            const response = JSON.parse(xhr.response);
            annualBalanceSpan.textContent = response[0];
            sickBalanceSpan.textContent = response[1];
        } else {
            console.error('Error:', xhr.statusText);
        }
    };
    
    xhr.send();
};


endDateInput.addEventListener('change', () => {
    event.preventDefault();

    if (endDateInput.value < startDateInput.value) {
        alert("End date cannot be earlier than the start date!");
        return;
    }
    
    const xhr = new XMLHttpRequest();
    xhr.open('POST', "http://127.0.0.1:8000/calculateDuration");
    xhr.setRequestHeader('Content-Type', 'application/json');
    
    xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        daysRequestedInput.value = JSON.parse(xhr.response);
    } else {
        console.error('Error:', xhr.statusText);
    }
    };
    xhr.send(JSON.stringify({
        startDate: startDateInput.value,
        endDate: endDateInput.value
    }));
});

vacationForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const xhr = new XMLHttpRequest();
    xhr.open('POST', "http://127.0.0.1:8000/balanceManager");
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = () => {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        console.log(JSON.parse(xhr.response)[0])
        annualBalanceSpan.textContent = JSON.parse(xhr.response)[0];
        sickBalanceSpan.textContent = JSON.parse(xhr.response)[1];

    } else {
        console.error('Error:', xhr.statusText);
    }
    };
    xhr.send(JSON.stringify({
        VacationDuration: daysRequestedInput.value,
        vacationType: vacationType.value
    }));

    vacationForm.reset();
});
