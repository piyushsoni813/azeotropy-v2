// debug-borders.js

function addDebugBorders() {
    const colors = [
      "border-red-500",
      "border-orange-500",
      "border-yellow-500",
      "border-green-500",
      "border-blue-500",
      "border-indigo-500",
      "border-purple-500",
      "border-pink-500",
    ];
  
    let colorIndex = 0;
  
    function traverse(element, level) {
      if (element.tagName === "DIV") {
        element.classList.add("border-2", colors[colorIndex % colors.length]);
        colorIndex++;
      }
  
      for (let child of element.children) {
        traverse(child, level + 1);
      }
    }
  
    const root = document.getElementById("smooth-content");
    if (root) {
        traverse(root, 0);
    } else {
      console.warn("Could not find element with ID #smooth-content. Using body as fallback.");
      traverse(document.body, 0);
    }
  }
  
  // Run the function when the DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addDebugBorders);
  } else {
    addDebugBorders();
  }