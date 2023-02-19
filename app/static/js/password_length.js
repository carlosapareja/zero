let rangeInput = document.getElementById('password-len');
let rangeValue = document.getElementById('range-value');

rangeValue.textContent = rangeInput.value;

rangeInput.addEventListener('input', () => {
    rangeValue.textContent = rangeInput.value;
})

function copyPassword() {
    let passwordValue = document.getElementById('password-value');
    passwordValue.select();
    let temp = passwordValue.value;
    navigator.clipboard.writeText(temp);
}