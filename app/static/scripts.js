//Add favourite for search.html
$(function() {
  $(".fav-button").bind('click', function(event) {
      const url = '/background_process_favourite/' + event.target.id;
    $.getJSON(url,
        function(data) {
      //do nothing
    });
    return false;
  });
});

//Remove favourite for favourites.html
$(function() {
  $(".remove-fav-button").bind('click', function(event) {
      const url = '/background_process_remove_favourite/' + event.target.id;
    $.getJSON(url,
        function(data) {
      //do nothing
    });
    return false;
  });
});


//Remove favourited plan for favourites.html
$(".remove-fav-button").click(function(event) {
    const planDiv = $(event.target).parent().parent()
    planDiv.html("Plan removed from favourites.")
    // planDiv.addClass("alert alert-primary")
})