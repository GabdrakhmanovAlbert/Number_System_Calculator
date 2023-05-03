"use strict"

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact_form');
    form.addEventListener('submit', formValidate);

    function formValidate(event) {
        let error = 0;
        let ReqFields = document.querySelectorAll('._req');

        for (let i = 0; i < ReqFields.length; i++) {
            const input = ReqFields[i];
            RemErrElandPar(input);
            if (input.getAttribute('type') === 'email') {
                if (!emailTest(input)) {
                    AddErrElandPar(input);
                    error++;
                }
            } else if (input.value === '') {
                AddErrElandPar(input);
                error++;
            }
        }
        // console.alert('validation')
        if (error > 0) {
            // console.alert('prevent')
            event.preventDefault()  // cancel form submit
            if (navigator.userAgent.indexOf('YaBrowser') === -1) {
                window.history.back()  // eq to push left arrow button in browser
            }
        }
    }

    function AddErrElandPar(el) {
        el.parentElement.classList.add('_error');
        el.classList.add('_error');
    }

    function RemErrElandPar(el) {
        el.parentElement.classList.remove('_error');
        el.classList.remove('_error');
    }

    function emailTest(email) {
        return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,8})+$/.test(email.value);
    }
})