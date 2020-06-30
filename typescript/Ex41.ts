export default class Ex41 {
    iterativeSum(array: number[]): number {
        let result: number = 0;

        for (let item of array) {
            result += item;
        }

        return result;
    }

    recursiveSum(array: number[]): number {
        if (array.length == 0) {
            return 0;
        }

        if (array.length == 1) {
            return array[0];
        }

        return (array.shift() || 0) + this.recursiveSum(array);
    }
}