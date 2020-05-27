var $form = $('form#test-form'),
    url = 'https://script.google.com/macros/s/AKfycbwIwHJCdOySkNa-uz3Lj4X80ex2ZnoPBOHuhJVeEl_7q6b8qfo/exec'

$('#submit-form').on('click', function(e) {
  e.preventDefault();
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serializeObject()
  }).success(
    // do something
  );
})