$(document).ready(function() {
    $(".remove-item").click(function(e) {
        e.preventDefault();
        var itemElement = $(this).closest("li");
        var itemId = itemElement.data("item-id");

        // Send an AJAX request to remove the item from the cart
        $.ajax({
            type: "POST",
            url: "{% url 'remove_from_cart' %}",
            data: {
                item_id: itemId,
                csrfmiddlewaretoken: "{{ csrf_token }}",
            },
            success: function(response) {
                if (response.success) {
                    // Remove the item from the cart and the page
                    itemElement.remove();
                }
            },
        });
    });
});

