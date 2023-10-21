document.addEventListener("DOMContentLoaded", function () {
  let testimonials = document.querySelectorAll(".testimonial-card");
  let windowHeight = window.innerHeight;

  function animateTestimonials() {
    testimonials.forEach(function (testimonial) {
      let bounding = testimonial.getBoundingClientRect();
      if (bounding.top >= 0 && bounding.top <= windowHeight) {
        testimonial.classList.add("show");
      }
    });
  }

  window.addEventListener("scroll", animateTestimonials);
  window.addEventListener("resize", animateTestimonials);

  // Initial check to show testimonials if already in the viewport
  animateTestimonials();
});

// Image Zoom
$(".img-zoom").hover(
  function () {
    $(this).addClass("transition");
  },
  function () {
    $(this).removeClass("transition");
  }
);

// Smooth Scrolling
$(document).ready(function () {
  // Add smooth scrolling to all links
  $("a").on("click", function (event) {
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash (#)
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area (the speed of the animation)
      $("html, body").animate(
        {
          scrollTop: $(hash).offset().top - 100,
        },
        800,
        function () {
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        }
      );
    } // End if
  });
});

AOS.init();




