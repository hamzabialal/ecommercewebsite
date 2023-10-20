var cart = {}; // Declare cart at the global level

if (localStorage.getItem('cart') !== null) {
  cart = JSON.parse(localStorage.getItem('cart'));
  updateCartDisplay();
}

$('.cart').click(function () {
  console.log('clicked');
  var idstr = this.id.toString();
  console.log(idstr);

  if (cart[idstr] != undefined) {
    cart[idstr].qty += 1; // Increase the quantity if the product already exists
  } else {
    // If the product doesn't exist in the cart, fetch the product details
    getItemDetails(idstr, function (itemData) {
      var qty = 1;
      var name = itemData.name;
      var image = itemData.image;
      var price = itemData.price;
      cart[idstr] = { qty: qty, name: name, image: image, price: price }; // Add the product to the cart
      localStorage.setItem('cart', JSON.stringify(cart)); // Save the updated cart
      console.log('Product Name for ID ' + idstr + ': ' + name); // Log the actual product name
      updateCartDisplay(); // Update the cart display after fetching details
    });
  }
});




function getItemDetails(itemId, callback) {
  $.ajax({
    url: 'http://127.0.0.1:1200/mybackend/',
    method: 'GET',
    data: { itemId: itemId },
    success: function (data) {
      callback(data);
    },
    error: function (error) {
      console.error('Error fetching item details', error);
      callback({ name: 'Item Name', price: '$Item price' });
    },
  });
}
function updateCartDisplay() {
  document.getElementById('cart').innerHTML = Object.keys(cart).length;
  document.getElementById('shopping').innerHTML = Object.keys(cart).length;

  $('#popcart ul.cart-item').empty();

  for (var itemId in cart) {
    if (cart.hasOwnProperty(itemId)) {
      (function (itemId) {
        getItemDetails(itemId, function (itemData) {
//          console.log(itemData.discount_percentage);

          var cartItem = document.createElement('li');

          cartItem.innerHTML = `
            <div class="cart-item-image"><img src="${itemData.image}" alt="" /></div>
            <div class="cart-item-info">
              <h4>${itemData.name}</h4>

              <p class="price">${itemData.price}</p>
            </div>
            <div class="cart-item-close">
              <a href="#" data-toggle="tooltip" data-title="Remove" class="remove-item" data-itemid="${itemId}">&times;</a>
            </div>`;

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