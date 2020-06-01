export default function getInputArray() {
    const row = document.getElementById('row').value;
    const col = document.getElementById('col').value;
    const value = document.getElementById('value').value;
    console.log(row,col,value);
    return [row - 1, col - 1, value];
}

