const delayedColorChange = (newColor, delay, doNext) => {
    setTimeout(() => {
        document.body.style.backgroundColor = newColor;
        doNext && doNext();
    }, delay);
};

// STILL A LOT OF NESTING!!!
/*
Callback Hell: Callback Hell is essentially nested callbacks stacked below one another forming a pyramid structure. Every callback
depends/waits for the previous callback, thereby making a pyramid structure that affects the readability and maintainability of the
code. Callback Hell is also know as "Pyramid of Doom".
*/
delayedColorChange("red", 1000, () => {
    delayedColorChange("orange", 1000, () => {
        delayedColorChange("yellow", 1000, () => {
            delayedColorChange("green", 1000, () => {
                delayedColorChange("blue", 1000, () => {
                    
                });
            });
        });
    });
});




// searchMoviesAPI('amadeus', () => {
//     saveToMyDB(movies, () => {
//         //if it works, run this:
//     }, () => {
//         //if it doesn't work, run this:
//     })
// }, () => {
//     //if API is down, or request failed
// })