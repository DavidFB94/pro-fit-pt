function calculateTotalPrice() {
    var select = document.getElementById("id_service_quantity");
    if (!select.value || select.value === "Select amount") {
        document.getElementById("total_price").innerText = "0.00 $";
        return;
    }
    
    var selectedOption = select.options[select.selectedIndex];
    var quantity = parseInt(selectedOption.getAttribute("data-quantity"));
    var pricePerUnit = parseFloat(selectedOption.getAttribute("data-price"));
    var totalPrice = quantity * pricePerUnit;
    document.getElementById("total_price").innerText = totalPrice.toFixed(2) + " $";
}