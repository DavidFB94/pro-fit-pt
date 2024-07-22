/* jshint esversion: 11, jquery: true */
// Sort services
document.getElementById('sort-selector').addEventListener('change', function() {
    const selectedValue = this.value;
    let currentUrl = new URL(window.location);

    if (selectedValue === 'reset') {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');
    } else {
        const [sort, direction] = selectedValue.split('_');
        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);
    }

    window.location = currentUrl.toString();
});
