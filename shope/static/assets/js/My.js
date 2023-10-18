console.log('working');

var cart = {};

if (localStorage.getItem('cart') !== null) {
  cart = JSON.parse(localStorage.getItem('cart'));
  updateCartDisplay();
}

$('.cart').click(function () {
  console.log('clicked');
  var idstr = this.id.toString();
  console.log(idstr);

  if (cart[idstr] != undefined) {
    cart[idstr] = cart[idstr] + 1;
  } else {
    cart[idstr] = 1;
  }

  console.log(cart);
  localStorage.setItem('cart', JSON.stringify(cart));
  updateCartDisplay();
});
// Define a function to make an AJAX request to the server to fetch item details
function getItemDetails(itemId, callback) {
  $.ajax({
    url: 'http://127.0.0.1:1200/mybackend/', // Replace with your backend endpoint
    method: 'GET',
    data: { itemId: itemId },
    success: function (data) {
      callback(data);
    },
    error: function (error) {
      console.error('Error fetching item details', error);
      callback({ name: 'Item Name', price: '$Item Price' }); // Provide default values
    },
  });
}
function updateCartDisplay() {
  document.getElementById('cart').innerHTML = Object.keys(cart).length;
  document.getElementById('shopping').innerHTML = Object.keys(cart).length;

  // Clear the existing cart items
  $('#popcart ul.cart-item').empty();

  // Iterate through the cart items and add them to the cart dropdown
  for (var itemId in cart) {
    if (cart.hasOwnProperty(itemId)) {
      // Use a closure to capture itemId for this iteration
      (function (itemId) {
        getItemDetails(itemId, function (itemData) {
          // Create the structure for each cart item using the retrieved item data
          var cartItem = document.createElement('li');
          cartItem.innerHTML = `
            <div class="cart-item-image"><img src="${itemData.image}" alt="" /></div>
            <div class="cart-item-info">
              <h4>${itemData.name}</h4>
              <p class="price">${itemData.discount_percentage}</p>
            </div>
            <div class="cart-item-close">
              <a href="#" data-toggle="tooltip" data-title="Remove" class="remove-item" data-itemid="${itemId}">&times;</a>
            </div>`;

          // Add the cart item to the cart dropdown
          $('#popcart ul.cart-item').append(cartItem);
        });
      })(itemId);
    }
  }


 $('#popcart').on('click', '.remove-item', function () {
  var itemIdToRemove = $(this).data('itemid');
  if (cart[itemIdToRemove] > 1) {
    cart[itemIdToRemove] -= 1;
  } else {
    delete cart[itemIdToRemove];
  }
  localStorage.setItem('cart', JSON.stringify(cart));
  updateCartDisplay();
});
}