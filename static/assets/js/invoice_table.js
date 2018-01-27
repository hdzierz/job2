function toggle(source) {
    checkboxes = document.getElementsByName('invoice_selection[]');
    for(var i in checkboxes)
        checkboxes[i].checked = source.checked;
}