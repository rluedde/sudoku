/*
// INIT
var myString   = "blablabla Card game bla";
var myPassword = "myPassword";

// PROCESS
var encrypted = CryptoJS.AES.encrypt(myString, myPassword);
var decrypted = CryptoJS.AES.decrypt(encrypted, myPassword);
console.log(decrypted.toString(CryptoJS.enc.Utf8));
*/


var testGrid = [[1,2,3,3,3,3,3,3,3],[3,4,4,4,4,4,4,4,4],[3,6,1,1,1,1,1,1,1]]

function getGridString(grid) {
    const singleArray = grid.reduce(function(accum, arr) {
        accum.push(...arr)
        return accum
    }) 
    const gridString = singleArray.reduce((accum, num) => accum + String(num))
    return gridString
}

function getGrid(gridstring) {
    const gridArr = gridstring.split("").map(element => parseInt(element))
    const grid = []
    gridArr.forEach(function(_, index){
        if (index % 9 === 0) {
            grid.push(gridArr.slice(index, index + 9))
        }
    })
    return grid
}

function getAccessToken(gridstring) {
    var gridString = getGridString(grid) 
}


var gs = getGridString(testGrid)
var grid = getGrid(gs)

console.log(gs, grid)
/* 
// Encrypt
var ciphertext = CryptoJS.AES.encrypt('gridstring', 'secret key 123').toString();
 
// Decrypt
var bytes  = CryptoJS.AES.decrypt(ciphertext, 'secret key 123');
console.log(bytes)
var originalText = bytes.toString(CryptoJS.enc.Utf8);
 
console.log(originalText);
*/