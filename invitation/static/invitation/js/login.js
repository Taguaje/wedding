function updateLogin() {
    var nameInput = document.getElementById('name');
    var secondNameInput = document.getElementById('second_name');
    document.getElementById('login_id').value = (capitalizeFirstLetter(nameInput.value) + capitalizeFirstLetter(secondNameInput.value)).replace(/\s/g, '');
    document.getElementById('id_password').value = capitalizeFirstLetter(secondNameInput.value.replace(/\s+/g, ''));
}

function capitalizeFirstLetter(s) {
    return s[0].toUpperCase() + s.slice(1);
}