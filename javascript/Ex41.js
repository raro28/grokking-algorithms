export default class Ex41 {
    iterativeSum(array) {
        let result = 0;

        for (let item of array) {
            result += item;
        }

        return result;
    }

    recursiveSum(array) {
        if (array.length == 0) {
            return 0;
        }
        if (array.length == 1) {
            return array[0];
        }

        return array.shift() + this.recursiveSum(array);
    }
}