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
                button.innerHTML = "ABSTRACT <i class='btn btn-sm z-depth-0' type='button' target='_blank' style='font-size:12px'></i>"; // this − minus sign is of equal length as +  
              } else {
                toggleBlocks[index].style.maxHeight = toggleBlocks[index].scrollHeight + "px";
                button.innerHTML = "ABSTRACT <i class='btn btn-sm z-depth-0' type='button' target='_blank' style='font-size:12px'></i>"; 
              }
            
        });
    });
});
