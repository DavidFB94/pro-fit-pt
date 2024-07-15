// Add/edit/remove pricingtier from service with FormSet
document.addEventListener('DOMContentLoaded', function () {
    var formsetContainer = document.getElementById('formset-container');
    var addFormsetButton = document.getElementById('add-formset');
    var totalForms = document.getElementById('id_pricingtier_set-TOTAL_FORMS');

    addFormsetButton.addEventListener('click', function () {
        var newFormIndex = totalForms.value;
        var formTemplate = document.querySelector('.formset-item').outerHTML;

        // Replace __prefix__ with the new form index
        var newFormHtml = formTemplate.replace(/__prefix__/g, newFormIndex);

        // Create a new div for the form and set its inner HTML
        var newForm = document.createElement('div');
        newForm.innerHTML = newFormHtml;

        // Update the formset item IDs and names
        newForm.innerHTML = newForm.innerHTML.replace(/id="(\S+)-(\d+)-(\S+)"/g, 'id="$1-' + newFormIndex + '-$3"');
        newForm.innerHTML = newForm.innerHTML.replace(/name="(\S+)-(\d+)-(\S+)"/g, 'name="$1-' + newFormIndex + '-$3"');
        newForm.innerHTML = newForm.innerHTML.replace(/for="(\S+)-(\d+)-(\S+)"/g, 'for="$1-' + newFormIndex + '-$3"');

        // Append the new form to the formset container
        formsetContainer.appendChild(newForm.firstElementChild);

        // Increment the total forms count
        totalForms.value = parseInt(totalForms.value) + 1;
    });
});
