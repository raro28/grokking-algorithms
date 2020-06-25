export default class SelectionSort {
    findSmallest(array) {
        let smallest = array[0];
        let smallestIndex = 0;
        for (let i = 1; i < array.length; i++) {
            if (array[i] < smallest) {
                smallest = array[i];
                smallestIndex = i;
            }
        }

        return smallestIndex;
    }

    sort(array) {
        const result = [];
        while (array.length > 0) {
            result.push(array.splice(this.findSmallest(array), 1)[0]);
        }

        return result;
    }
}