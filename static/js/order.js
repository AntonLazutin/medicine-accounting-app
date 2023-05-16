let container = document.querySelector("#order-form");
let item_form = document.querySelectorAll(".orderitem-form");
let total_forms = document.getElementById("id_order_items-TOTAL_FORMS");
let add_button = document.getElementById("add");

let formNum = 0;


add_button.addEventListener('click', event => {
    event.preventDefault();

    let formRegex = RegExp(`order_items-(\\d){1}-`,'g');
    let new_form = item_form[0].cloneNode(true);

    formNum++;
    new_form.innerHTML = new_form.innerHTML.replace(formRegex, `order_items-${formNum}-`);
    container.appendChild(new_form); 
    container.insertBefore(new_form, document.getElementById('buttons'));

    total_forms.setAttribute('value', `${formNum+1}`)
});
