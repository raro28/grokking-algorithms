import { BinarySearch } from './BinarySearch.js';

let binarySearch: BinarySearch = new BinarySearch();

const myList: number[] = [1,3,5,7,9];

console.log(binarySearch.search(myList, 3));
console.log(binarySearch.search(myList, -1));