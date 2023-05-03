const fset = document.getElementById('info-404');

function manageParas() {
    console.log(fset);
    console.dir(fset);
    for (el of fset.elements) {
        if (el.checked) {
            console.dir(el.parentElement.parentElement.children[2]);
            el.parentElement.parentElement.children[2].classList.remove('_hidden');
            // for (p of el.labels[0].children) {
            //     p.classList.remove('hidden-p');
            // }
        }
        else {
            el.parentElement.parentElement.children[2].classList.add('_hidden')
            // for (p of el.labels[0].children) {
            //     p.classList.add('hidden-p');
            // }
        }
    }
}

fset.addEventListener('change', manageParas);