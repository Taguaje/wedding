function updateLogin() {
    var nameInput = document.getElementById('name');
    var secondNameInput = document.getElementById('second_name');
    document.getElementById('login_id').value = nameInput.value + secondNameInput.value;
    document.getElementById('id_password').value = secondNameInput.value;
}