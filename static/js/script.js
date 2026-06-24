(function() {
  const blurProperty = gsap.utils.checkPrefix("filter"),
      blurExp = /blur\((.+)?px\)/,
      getBlurMatch = (target) =>
      (gsap.getProperty(target, blurProperty) || "").match(blurExp) || [];

  gsap.registerPlugin({
      name: "blur",
      get(target) {
          return +(getBlurMatch(target)[1]) || 0;
      },
      init(target, endValue) {
          let data = this,
              filter = gsap.getProperty(target, blurProperty),
              endBlur = "blur(" + endValue + "px)",
              match = getBlurMatch(target)[0],
              index;
          if (filter === "none") {
              filter = "";
          }
          if (match) {
              index = filter.indexOf(match);
              endValue =
                  filter.substr(0, index) + endBlur + filter.substr(index + match.length);
          } else {
              endValue = filter + endBlur;
              filter += filter ? " blur(0px)" : "blur(0px)";
          }
          data.target = target;
          data.interp = gsap.utils.interpolate(filter, endValue);
      },
      render(progress, data) {
          data.target.style[blurProperty] = data.interp(progress);
      },
  });
})();


gsap.registerPlugin(ScrollTrigger, ScrollSmoother, SplitText);

// let smoother = ScrollSmoother.create({
//     smooth: 2,
//     wrapper: "#smooth-wrapper",
//     content: "#smooth-content",
// });

document.addEventListener("DOMContentLoaded", function () {
    const elementsToAnimate = [];
    const classElements = document.querySelectorAll(".blur-element");

    // Media query to disable blur animation on small screens
    const isLargeScreen = window.matchMedia("(min-width: 1410px)").matches;

    if (isLargeScreen) {
        classElements.forEach((element) => {
            elementsToAnimate.push({
                element: element,
            });
            gsap.set(element, {
                blur: 0, // Initialize blur to 0
            });
        });

        elementsToAnimate.forEach((item) => {
            gsap.to(item.element, {
                ease: "power4.out",
                scrollTrigger: {
                    trigger: item.element,
                    start: "top 100%",
                    end: "bottom 7%",
                    scrub: 2,
                    markers: false,
                    toggleActions: "play none none reverse",
                    onUpdate: (self) => {
                        let blurAmount;
                        if (self.progress < 0.5) {
                            blurAmount = gsap.utils.mapRange(0, 0.2, 4, 0, self.progress);
                        } else {
                            blurAmount = gsap.utils.mapRange(0.8, 1, 0, 4, self.progress);
                        }
                        gsap.set(item.element, {
                            blur: blurAmount,
                        });
                    },
                },
            });
        });
    }
});


document.addEventListener("DOMContentLoaded", function() {
  const introTextElements = document.querySelectorAll(".introtext");

  introTextElements.forEach(textEl => {
      const splitText = new SplitText(textEl, {
          type: "chars"
      }); // Use SplitText from GSAP
      gsap.set(textEl, {
          autoAlpha: 1
      });

      const tl = gsap.timeline({
          scrollTrigger: {
              trigger: textEl,
              start: "top 70%",
              toggleActions: "play none none reverse",
              markers: false
          }
      });

      tl.from(splitText.chars, {
          autoAlpha: 0,
          scale: 1,
          yPercent: 0,
          ease: "power2.out",
          duration: 1.5,
          stagger: 0.05
      }).from(
          textEl, {
              letterSpacing: "0.2em",
              filter: "blur(20px)",
              duration: 1.5,
              ease: "power1.out"
          },
          "<"
      );

      //
  });
});

gsap.registerPlugin(ScrollTrigger);

// --- Gooey Text Animation ---
function animateGooeyText(text) {
  const filterId = text.getAttribute('data-filter');
  const feBlur = document.querySelector(`#${filterId} feGaussianBlur`);

  if (!feBlur) {
      console.warn(`Filter with ID ${filterId} not found for element`, text);
      return;
  }

  // Apply the filter to the element's style
  text.style.filter = `url(#${filterId})`;

  gsap.set(text, { opacity: 0 });

  let primitiveValues = { stdDeviation: 0 };

  const animationTimeline = gsap.timeline({
      defaults: {
          duration: 2,
          ease: 'expo'
      },
      onUpdate: () => {
          feBlur.setAttribute('stdDeviation', primitiveValues.stdDeviation);
      },
      scrollTrigger: {
          trigger: text,
          start: 'center bottom'
      }
  })
  .to(primitiveValues, {
      startAt: { stdDeviation: 50 },
      stdDeviation: 0
  }, 0)
  .to(text, {
      startAt: {
          opacity: 0
      },
      opacity: 1
  }, 0);
}

// Select and animate the h2 elements with the gooey effect
const gooeyTextElements = document.querySelectorAll('h2[data-filter="goo-1"]');
gooeyTextElements.forEach(animateGooeyText);

let mySplitText = new SplitText("#split-stagger", { type: "words,chars" });
let chars = mySplitText.chars;
chars.forEach((char, i) => {
    smoother.effects(char, { speed: 8, lag: (i + 1) * 0.4 });
   });

// document.addEventListener("DOMContentLoaded", function () {
//     const navbarLinks = document.querySelectorAll(".menu a");

//     navbarLinks.forEach((link) => {
//         link.addEventListener("click", function (event) {
//             event.preventDefault();
//             const sectionId = this.getAttribute("href").slice(1);
//             const targetSection = document.getElementById(sectionId);

//             if (targetSection) {
//                 // Use GSAP to scroll with a custom easing effect
//                 gsap.to(window, {
//                     duration: 2, // Duration of the scroll animation
//                     scrollTo: {
//                         y: targetSection,
//                         autoKill: true, // Stops the scroll animation if the user intervenes
//                     },
//                     ease: "power2.out", // Custom easing
//                 });
//             }
//         });
//     });
// });


// ScrollTrigger.defaults({
//     markers: true // Enable markers to debug trigger points
// });

const smoother = ScrollSmoother.create({
    wrapper: "#smooth-wrapper",
    content: "#smooth-content",
    smooth: 1.5,
    normalizeScroll: true, 
    ignoreMobileResize: true, 
    effects: true,
    preventDefault: true
   });
   
   
   
   //Horizontal Scroll Galleries
   if (document.getElementById("portfolio")) {
       const horizontalSections = gsap.utils.toArray('.horiz-gallery-wrapper')
   
       horizontalSections.forEach(function (sec, i) {
   
         const pinWrap = sec.querySelector(".horiz-gallery-strip");
   
         let pinWrapWidth;
         let horizontalScrollLength;
         
         function refresh() {
           pinWrapWidth = pinWrap.scrollWidth;
           horizontalScrollLength = pinWrapWidth - window.innerWidth;
        //    console.log("pinWrapWidth:", pinWrap.scrollWidth);
         }
   
         // window.addEventListener("load", function () {
           refresh();
           // Pinning and horizontal scrolling
           let scrollTween = gsap.to(pinWrap, {
             scrollTrigger: {
               scrub: true,
               trigger: sec,
               pin: sec,
               start: "center center",
               end: () => `+=${pinWrapWidth}`,
               invalidateOnRefresh: true
             },
             x: () => -horizontalScrollLength,
             ease: "none"
           });
         
         pinWrap.querySelectorAll("[data-speed-x]").forEach((el, i) => {
           let speed = parseFloat(el.getAttribute("data-speed-x"));
           gsap.to(el, {
             x: () => (1 - speed) * (window.innerWidth + el.offsetWidth),
             ease: "none",
             scrollTrigger: {
               containerAnimation: scrollTween,
               trigger: el,
               onRefresh: self => {
                 let start = Math.max(0, self.start);
                 self.setPositions(start, start + (self.end - self.start) / Math.abs(speed)); // adjust for how long it'll stay in view
                 self.animation.progress(0);
               },
               scrub: true
             }
           });
         });
         
   
           ScrollTrigger.addEventListener("refreshInit", refresh);
         // });
       });
   }
   
// Function to wrap elements (not used in this specific effect, but might be useful for others)
const wrapElements = (elems, wrapType, wrapClass) => {
    elems.forEach(char => {
        const wrapEl = document.createElement(wrapType);
        wrapEl.classList = wrapClass;
        char.parentNode.appendChild(wrapEl);
        wrapEl.appendChild(char);
    });
}
//----------------About Azeotropy-----------------//
// Initialize Splitting.js
Splitting();

// Target only the title with data-effect8
const fx8Titles = [...document.querySelectorAll('.content__title[data-splitting][data-effect8]')];

// Letters and symbols for the scramble effect
const lettersAndSymbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', ';', ':', '<', '>', ','];

fx8Titles.forEach(title => {
    const chars = title.querySelectorAll('.char');

    chars.forEach((char, position) => {
        let initialHTML = char.innerHTML;

        gsap.fromTo(char, {
            opacity: 0
        },
        {
            duration: 0.03,
            innerHTML: () => lettersAndSymbols[Math.floor(Math.random() * lettersAndSymbols.length)],
            repeat: 1,
            repeatRefresh: true,
            opacity: 1,
            repeatDelay: 0.03,
            delay: (position+1)*0.01,
            onComplete: () => gsap.set(char, {innerHTML: initialHTML, delay: 0.03}),
            scrollTrigger: {
                trigger: title,
                start: "top bottom",
                end: "bottom center",
                toggleActions: "play resume resume reset",
                onEnter: () => gsap.set(char, {opacity: 0})
            }
        });
    });
});

//-----------------counter---------------//
document.addEventListener("DOMContentLoaded", function () {
    // ... (Your existing code for ScrollSmoother, navigation, intro text animation, etc.)
  
    // --- Number Counter Animation ---
    const counters = document.querySelectorAll(".count-up");
  
    counters.forEach((counter) => {
      const target = +counter.textContent; // Get the target number and convert to number type
      let count = 0;
      const duration = 2000; // Animation duration in milliseconds
      const increment = Math.ceil(target / (duration / 16)); // Calculate increment based on duration and refresh rate (assuming ~60fps)
  
      const updateCount = () => {
        if (count < target) {
          count += increment;
          if (count > target) count = target; // Prevent overshooting
          counter.textContent = count;
          requestAnimationFrame(updateCount);
        } else {
          counter.textContent = target;
        }
      };
  
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              updateCount();
              observer.unobserve(entry.target); // Stop observing once triggered
            }
          });
        },
        { threshold: 0.5 } // Trigger when 50% of the element is visible
      );
  
      observer.observe(counter);
    });
  });