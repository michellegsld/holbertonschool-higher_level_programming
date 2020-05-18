window.onload = () => {
  let i = 0;
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li id=' + i + '>Item</li>');
    i++;
  });

  $('DIV#remove_item').click(function () {
    i--;
    $('#' + i).remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
    i = 0;
  });
}