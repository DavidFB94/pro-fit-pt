// Remove item and reload on click
$('.remove-item').click(function (e) {
    let csrfToken = "{{ csrf_token }}";
    let compositeKey = $(this).attr('id').split('remove_')[1];
    let url = `/cart/remove/${compositeKey}/`;
    let data = { 'csrfmiddlewaretoken': csrfToken };

    $.post(url, data)
        .done(function () {
            location.reload();
        });
})