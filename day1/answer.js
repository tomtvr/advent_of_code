

const fs = require('fs');

fs.readFile('/mnt/c/Users/tomtv/Documents/Advent_Of_Code_2022/advent_of_code/day1/puzzleInput', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const sliced = data.split("\n");
    const elfMaxes = []
    let currentTotal = 0;
    sliced.forEach(element => {
        if (element.length === 0) {
            elfMaxes.push(currentTotal);
            currentTotal = 0;
        } else {
            currentTotal += parseInt(element);
        }
    });
    
    let currentMax = 0;
    elfMaxes.forEach(element => {
        const current = parseInt(element);
        if (current >= currentMax) {
            currentMax = current;
        }
    })
    console.log(currentMax)
});