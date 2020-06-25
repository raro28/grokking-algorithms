import BinarySearch from './BinarySearch.js';

const binarySearch = new BinarySearch();
const myList = [1,3,5,7,9];

console.log(binarySearch.search(myList,3));
console.log(binarySearch.search(myList,-1));