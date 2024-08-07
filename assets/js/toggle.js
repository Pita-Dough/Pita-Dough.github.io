document.addEventListener("DOMContentLoaded", function() {
    // Get references to all toggle buttons and toggle blocks
    var toggleButtons = document.querySelectorAll('[id*="toggleButton"]');
    var toggleBlocks = document.querySelectorAll('[id*="toggleBlock"]');

    console.log(toggleButtons);
    console.log(toggleBlocks);

    // Add a click event listener to each toggle button
    toggleButtons.forEach(function(button, index) {
        button.addEventListener("click", function() {
            // Toggle the "hidden" class on the corresponding toggle block
            // toggleBlocks[index].classList.toggle("hidden");

            // if (toggleBlocks[index].style.display=="none") {
            //     toggleBlocks[index].style.display="block";
            //     button.textContent = "Abstract−"; // this minus sign is of equal length as +  
            // } else {
            //     toggleBlocks[index].style.display="none";
            //     button.textContent = "Abstract+";
            // }
            if (toggleBlocks[index].style.maxHeight){
                toggleBlocks[index].style.maxHeight = null;
                button.innerHTML = "Abstract <i class='btn btn-sm z-depth-0' role='button' target='_blank' style='font-size:12px;cursor:pointer;color:#000d12;background-color:#fffaf2;'><i class='fas fa-chevron-down' style='font-size:12px;color:#2086c9;background-color:#fffaf2;'></i>"; // this − minus sign is of equal length as +  
              } else {
                toggleBlocks[index].style.maxHeight = toggleBlocks[index].scrollHeight + "px";
                button.innerHTML = "Abstract <i class='btn btn-sm z-depth-0' role='button' target='_blank' style='font-size:12px;cursor:pointer;color:#000d12;background-color:#fffaf2;'><i class='fas fa-chevron-up' style='font-size:12px;color:#2086c9;background-color:#fffaf2;'></i>"; 
              }

        });
    });
});

