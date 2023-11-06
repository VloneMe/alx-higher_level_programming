// JavaScript script that adds, removes and clears LI
// elements from a list when the user clicks:

$(document).ready(function() {
    // Add Item
    $("#add_item").click(function() {
        const newItem = $("<li>Item</li>");

        $(".my_list").append(newItem);
    });

    // Remove Item
    $("#remove_item").click(function() {
        const lastItem = $(".my_list li:last-child");
        lastItem.remove();
    });

    // Clear List
    $("#clear_list").click(function() {
        $(".my_list li").remove();
    });
});
