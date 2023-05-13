const vacationForm = document.getElementById('vacation-form');
const startDateInput = document.getElementById('start-date');
const endDateInput = document.getElementById('end-date');
const daysRequestedInput = document.getElementById('days-requested');
const vacationType = document.getElementById('vacation-type');
const annualBalanceSpan = document.getElementById('annual-balance');
const sickBalanceSpan = document.getElementById('sick-balance');




endDateInput.addEventListener('change', () => {
    event.preventDefault();

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


//   const xhr = new XMLHttpRequest();
//   xhr.open('POST', '/submit');
//   xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
//   xhr.send(`vacation-type=${vacationType.value}&start-date=${startDate.value}&end-date=${endDate.value}`);
//   const vacationType = document.getElementById('vacation-type').value;
//   const startDate = new Date(startDateInput.value);
//   const endDate = new Date(endDateInput.value);
//   let daysRequested = parseInt(daysRequestedInput.value);

//   // Deduct vacation days
//   let balance = parseInt(balanceSpan.textContent);
//   balance -= daysRequested;
//   balanceSpan.textContent = balance;

  // Reset form
  vacationForm.reset();
});
